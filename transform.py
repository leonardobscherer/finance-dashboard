from categories import convenience_words,expense_categories,salary_senders,payback,tax_reimbursement,investment_withdraw,income_categories,investment_deposit,non_expense_categories
import pandas as pd
import streamlit as st
        
def map_category(line): 
    #Maps key-words for each category
    description = str(line['Descrição']).lower()
    value = float(line['Valor'])

    #categorizing positive values
    if value > 0:
        if any(term in description for term in salary_senders):
            return 'Salary'

        if any(term in description for term in payback):
            return 'Pay back'

        if any(term in description for term in tax_reimbursement):
            return 'Tax reimbursement'

        if any(term in description for term in investment_withdraw):
            return 'Investment withdraw'

        if value == 230 and 'margarete' in description:
            return 'Post Graduation reimbursement'
     
        return 'Other income'


    #Categorizing negative values
    #Categorizes convenience expenses based on value, considering gas station expenses. (Cigarretes basically)
    if any(term in description for term in convenience_words):
        if abs(value) < 50:
            return 'Convenience'   
        else: 
            return 'Transport'
    #Categorizes investment deposits that are not true expenses
    if any(term in description for term in investment_deposit):
        return 'Investment'
    #Search the remaining categories
    for category, key_words in expense_categories.items():
        if any(term in description for term in key_words):
            return category
    return 'Others'

def create_negative_value_table(df):
    #Creates a new table with only negative values
    negative_value_df = df[df['Valor'] < 0].copy()
    negative_value_df['Valor'] = negative_value_df['Valor'].abs()
    return negative_value_df
    
def categorize_expenses(df):
    df['Category'] = df.apply(map_category, axis=1)
    return df
    
def convert_date(df):
    df['Data'] = pd.to_datetime(df['Data'],dayfirst=True)
    return df

def create_month_column(df):
    df["Month"] = df["Data"].dt.strftime("%Y-%m")
    return df

def expense_totals_by_month_and_category(df):
    expense_df = create_negative_value_table(df)
    expense_df = expense_df[~expense_df["Category"].isin(["Investment",'Investment withdraw'])]


    monthly_expenses = (expense_df.groupby(["Month", "Category"])["Valor"]
                        .sum()
                        .sort_values(ascending=False)
                        .unstack(level="Month",fill_value=0)
                        .reset_index()
                        )
    
    return monthly_expenses

def create_indicators(df):
    months = df["Month"].unique()

    #Quanto eu ganhei em cada mês?	Receita total
    total_income_by_month = None
    total_income_by_month = df[df['Category'].isin(income_categories)].groupby('Month')['Valor'].sum()
    total_income_by_month = total_income_by_month.reindex(months,fill_value=0)

    #Quanto eu gastei em cada mês?	Despesa total
    total_expense_by_month = df[~df['Category'].isin(non_expense_categories)].groupby('Month')['Valor'].sum().abs()
    total_expense_by_month = total_expense_by_month.reindex(months,fill_value=0)

    #Quanto sobrou?	Saldo
    remaining = total_income_by_month - total_expense_by_month

    #Quanto investi?	Total investido
    invested = df[df['Category'].isin(["Investment", "Investment withdraw"])].groupby('Month')['Valor'].sum()
    invested = invested * -1
    invested = invested.reindex(months,fill_value=0)          
    
    return {
    "income": total_income_by_month,
    "expense": total_expense_by_month,
    "remaining": remaining,
    "invested" : invested
}

def investment_evolution(df):
    months = sorted(df["Month"].unique())
    
    investment_evolution = df[df['Category'].isin(["Investment", "Investment withdraw"])].groupby('Month')['Valor'].sum()
    investment_evolution = investment_evolution * -1
    investment_evolution = investment_evolution.reindex(
    months,
    fill_value=0
)
    investment_evolution = investment_evolution.cumsum()

    return investment_evolution

def compare_months(df,first_month,second_month):
    #Estou gastando mais do que no mês passado?	Variação (%)
        expense_totals = expense_totals_by_month_and_category(df)
        expense_totals = expense_totals.set_index("Category")       
        
        difference = ((expense_totals[second_month] - expense_totals[first_month]) / (expense_totals[first_month]) * 100).round(2)

        zero_first_month = expense_totals[first_month] == 0

        difference[zero_first_month] = float("nan")


        comparison = pd.DataFrame({
        
            first_month: expense_totals[first_month],
            second_month: expense_totals[second_month],
            "Difference (%)": difference,
            })

        return comparison