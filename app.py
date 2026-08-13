import streamlit as st
import pandas as pd
from file_picker import upload_csv_files
from extract import load_csv
from transform import (convert_date, 
                       create_month_column, 
                       categorize_expenses,
                       create_indicators,
                       expense_totals_by_month_and_category,
                       investment_evolution,
                       compare_months
                       
                       
                       
                       )
from graphs import  expense_comparison_chart,pie_chart,monthly_evolution_chart,month_comparison_chart



st.title('Finance Dashboard')
files = upload_csv_files()
if files is None:
    st.write('No file selected.')
else:
    df = load_csv(files)
    if df is None:
        st.write('Failed to load file.')
    else:
        df = convert_date(df)
        df = create_month_column(df)
        df = categorize_expenses(df)
        totals_by_month_and_category = expense_totals_by_month_and_category(df)
        months =  sorted(df["Month"].unique())

    
        st.header('Indicators')

        selected_month = st.selectbox(
        "Select month",
        options=months,
        format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
        key="indicators",
       
        )

        if selected_month == None:
            st.write('Select a month to display')
        else:
            indicators = create_indicators(df)
            income = indicators["income"].loc[selected_month].round(2)
            expense = indicators["expense"].loc[selected_month].round(2)
            remaining = indicators["remaining"].loc[selected_month].round(2)
            invested = indicators["invested"].loc[selected_month].round(2)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(
            label="Income",
            value=f"R$ {income:.2f}"
        )
            with col2:
                st.metric(
            label="Expense",
            value=f"R$ {expense:.2f}"
        )
            with col3:
                st.metric(
            label="Remaining",
            value=f"R$ {remaining:.2f}"
        )
            with col4:
                st.metric(
                    label="Invested",
                    value=f"R$ {invested:.2f}"
                )


        st.header('Expenses by category')

        selected_expense_month = st.selectbox(
        "Select month",
        options=months,
        format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
        key="expense_month",
        
    )
        expense_month_df = totals_by_month_and_category[['Category',selected_expense_month]]

        pie = pie_chart(expense_month_df,selected_expense_month)    
        st.plotly_chart(pie) 

    
        st.header('Investment Evolution')

        evolution = investment_evolution(df)
        evolution_fig = monthly_evolution_chart(evolution)
        st.plotly_chart(evolution_fig)


        st.header('Month Comparison')
        col1, col2 = st.columns(2)

        with col1:
            first_month = st.selectbox(
                    "Select first month",
                    options=months,
                    format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                    key="first_month",
                    index = len(months) - 1
                    )
        with col2:
            second_month = st.selectbox(
                    "Select second month",
                    options=months,
                    format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                    key="second_month",
                    index = len(months) - 2
                    )
        comparison = compare_months(df,first_month,second_month)
        month_comparison_fig = month_comparison_chart(comparison)

        col1, col2 = st.columns(2)
        with col1:    
            st.write(comparison)
        with col2:
            st.plotly_chart(month_comparison_fig)



        st.header('Expenses by category')

        categories = totals_by_month_and_category["Category"].unique()

        col1, col2 = st.columns(2)
        with col1:
            selected_categories = st.multiselect(
            "Select categories",
            options=categories,
            default=categories
            )
            if selected_categories == []:
                st.write('Select at least one category to display')
        with col2:
            selected_months = st.multiselect(
            "Select months",
            options=months,
            format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
            default=months
            )
            if selected_months == []:
                st.write('Select at least one period to display')

        if selected_months and selected_categories:
            filtered_df = totals_by_month_and_category[totals_by_month_and_category['Category'].isin(selected_categories)]
            filtered_df = filtered_df[['Category'] + selected_months]
                        
            fig = expense_comparison_chart(filtered_df) 
            st.plotly_chart(fig)

            monthly_totals = filtered_df[selected_months].sum().mean()

            st.metric(
            label=f"Average Monthly Expense",
            value=f"R$ {monthly_totals:.2f}"
        )

    
        st.header('Transactions')

        col1, col2 = st.columns(2)

        with col1:
            transactions_month = st.selectbox(
                    "Select month",
                    options=months,
                    format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                    key="transactions month",
                
                    )
        with col2:
            transactions_selected_categories = st.multiselect(
                "Select categories",
                options=categories,
                default=categories,
                key= 'transactions categories'
                )

        transactions_df = df[['Data','Descrição','Valor','Category','Month']]
        transactions_df = transactions_df[transactions_df['Month'] == transactions_month]
        transactions_df = transactions_df[transactions_df['Category'].isin(transactions_selected_categories)]
        transactions_df = transactions_df[["Data", "Descrição", "Valor", "Category"]]
        transactions_df = transactions_df.sort_values(by="Data",ascending=True)

        st.dataframe(transactions_df)




        






        
        


