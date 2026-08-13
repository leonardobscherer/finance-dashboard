import plotly.express as px
import pandas as pd

def pie_chart(df,month):
    type = 'pie'
    formatted_month = pd.to_datetime(month).strftime("%B - %Y")

    fig = px.pie(df,
        values=month, 
        names='Category',
        title= f"Expenses by category - {formatted_month}",
        color='Category',
        )
    
    fig.update_traces(
        textposition='inside', 
        texttemplate='%{percent:.1%}<br>R$ %{value:,.2f}',
        hovertemplate='%{label}<br>%{percent}',
        marker=dict(line=dict(color='#000000', width=2)),
        textfont=dict(
        family="Arial, sans-serif",  
        size=22,                    
        color="white"                
        )
    )

    update_chart_layout(fig)
    return fig



def expense_comparison_chart(df):
    type='3 months bar'
    chart_df = df.copy()

    month_columns = [str(header) for header in chart_df.columns if header != 'Category']
    

    fig = px.bar(
        chart_df,
        x="Category",
        y=month_columns,
        barmode="group",
        title="Monthly expenses by category",
        labels={
            "Category": "Category",
            "value": "",
            "variable": "Month",
        }
    )
    fig.update_traces(
        textposition='outside',
        texttemplate='R$ %{y:,.2f}',                      
    )

    fig.update_yaxes(
        tickprefix="R$ ",
        tickformat=",.2f",
        showgrid=True
    )
     
    update_chart_layout(fig)
    return fig

def monthly_evolution_chart(series):
    series = series.reset_index()
    series["Formatted Month"] = pd.to_datetime(
    series["Month"]
).dt.strftime("%B - %Y")

    fig = px.line(
        series,
        x='Formatted Month',
        y='Valor',
        markers=True,
        title= 'Investment Evolution',
           labels={
        "Valor": "Value",
        "Formatted Month": "Month"
    }
    )
    update_chart_layout(fig)

    fig.update_yaxes(
        tickprefix="R$ ",
        tickformat=",.2f",
        showgrid=True        

    )
    return fig

def month_comparison_chart(df):
    df=df.reset_index()
    fig = px.bar(df, 
                 x='Difference (%)', 
                 y="Category", 
                 orientation='h',
                 title= 'Difference (%)')

    return fig

     



def update_chart_layout(fig):
        fig.update_layout(
        separators=',.',
        title_x=0.5,
        title_xanchor='center',
        title_font=dict(
        family="Arial, sans-serif",
        size=24,            
        color="#2c3e50"     
        )
    )

        