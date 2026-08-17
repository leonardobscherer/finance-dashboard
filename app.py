import streamlit as st
import pandas as pd
from file_picker import upload_csv_files
from extract import load_csv
from transform import (convert_date, 
                       create_month_column, 
                       categorize_expenses,
                       create_indicators,
                       prepare_indicators,
                       expense_totals_by_month_and_category,
                       investment_evolution,
                       compare_months,
                       prepare_df_for_plotting,
                       create_transactions_df,                  
                       )
from graphs import  expense_comparison_chart,pie_chart,monthly_evolution_chart,month_comparison_chart


st.set_page_config(
    page_title="Personal Finance Dashboard",
    layout="wide"
)


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
        categories = totals_by_month_and_category["Category"].unique()
        
        
        selected_month = st.selectbox(
                "Select month",
                options=months,
                format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                key="indicators",
                )

        st.header('Indicators')
       
        if selected_month == None:
            st.write('Select a month to display')
        else:
            indicators = create_indicators(df)
            income, expense, remaining, invested = prepare_indicators(indicators,selected_month)
    
            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
            with metric_col1:
                st.metric(
            label="Income",
            value=f"R$ {income:.2f}",
            border=True,
        )
            with metric_col2:
                st.metric(
            label="Expense",
            value=f"R$ {expense:.2f}",
            border=True,
        )
            with metric_col3:
                st.metric(
            label="Remaining",
            value=f"R$ {remaining:.2f}",
            border=True,
        )
            with metric_col4:
                st.metric(
                    label="Invested",
                    value=f"R$ {invested:.2f}",
                    border=True,
                )

        st.header('Transactions')
        transaction_categories = df['Category'].unique()

        transactions_selected_categories = st.multiselect(
                "Select categories",
                options=transaction_categories,
                default=transaction_categories,
                key= 'transactions categories'
                )

        transactions_df = create_transactions_df(df,selected_month,transactions_selected_categories)

        st.dataframe(
    transactions_df,
    width="stretch",
    height=420,
    hide_index=True,
    column_config={
        "Data": st.column_config.DateColumn(
            "Date",
            format="DD/MM/YYYY"
        ),
        "Descrição": st.column_config.TextColumn(
            "Description",
            width="large"
        ),
        "Valor": st.column_config.NumberColumn(
            "Value",
            format="R$ %.2f"
        ),
        "Category": st.column_config.TextColumn(
            "Category",
            width="medium"
        ),
        "Month": None
    }
)

        st.header('Expenses by category')
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:

            pie = pie_chart(totals_by_month_and_category,selected_month)    
            st.plotly_chart(pie,use_container_width=True,config={"displayModeBar": False})

        with chart_col2:          

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
                default=selected_month
                )
                if selected_months == []:
                    st.write('Select at least one period to display')

            if selected_months and selected_categories:
                filtered_df = totals_by_month_and_category[totals_by_month_and_category['Category'].isin(selected_categories)]
                filtered_df = filtered_df[['Category'] + selected_months]
                            
                fig = expense_comparison_chart(filtered_df) 
                st.plotly_chart(fig,config={"displayModeBar": False})

                monthly_totals, average_spend, highest_spend_month, highest_spend_value =  prepare_df_for_plotting(filtered_df,selected_months)                

                if len(selected_categories) == 1 and len(selected_months) != 1:
                    metriccol1, metriccol2 = st.columns(2)
                    with metriccol1:
                        st.metric(
                        label=f"Average Monthly Expense on {selected_categories[0]}",
                        value=f"R$ {average_spend:.2f}",
                        border=True,
                        )

                    with metriccol2:
                         st.metric(
                              label=f'The largest value spent  {selected_categories[0]} is  ',
                              value=f'R$ {highest_spend_value} in {highest_spend_month}',
                            border=True,
                        )
                         
                elif len(selected_categories) > 1 or len(selected_months) > 1:
                                    st.metric(
                    label=f"Average Monthly Expense on the selected categories",
                    value=f"R$ {average_spend:.2f}",
                    border=True,
                    )

        st.header('Investment Evolution')

        evolution = investment_evolution(df)
        evolution_fig = monthly_evolution_chart(evolution)
        st.plotly_chart(evolution_fig,config={"displayModeBar": False})


        st.header('Month Comparison')
        col1, col2 = st.columns(2)

        with col1:
            first_month = st.selectbox(
                    "Select reference month",
                    options=months,
                    format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                    key="first_month",
                    index = len(months) - 2
                    )
        with col2:
            second_month = st.selectbox(
                    "Select most recent month",
                    options=months,
                    format_func=lambda month: pd.to_datetime(month).strftime("%B - %Y"),
                    key="second_month",
                    index = len(months) - 1
                    )
        comparison = compare_months(df,first_month,second_month)
        month_comparison_fig = month_comparison_chart(comparison)

        col1, col2 = st.columns(2)
        with col1:    
            st.dataframe(comparison,
                         hide_index=True                                                 
                         )
        with col2:
            st.plotly_chart(month_comparison_fig,config={"displayModeBar": False})





    





        






        
        


