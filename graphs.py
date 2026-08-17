import plotly.express as px
import pandas as pd




def pie_chart(df,month):
    formatted_month = pd.to_datetime(month).strftime("%B - %Y")
    df = df[df[month] > 0]
    total = df[month].sum()
    expense_month_df = df[['Category',month]]

    fig = px.pie(expense_month_df,
        values=month, 
        names='Category',
        title= f'{formatted_month}',
        color='Category',
        color_discrete_sequence=px.colors.cyclical.IceFire
        )
    
    fig.update_traces(
        textposition='auto', 
        textinfo='label+percent',
        hovertemplate='%{label}<br>%{percent}',
        hole=0.5,
        automargin=True,
        textfont=dict(
        family="Arial, sans-serif",  
        size=20,                    
        color="white"                
        ),
        
        insidetextorientation='radial',
        rotation=90
    )

    fig.add_annotation(
    x=0.5,
    y=0.5,
    text=f'Total Expenses<br><b>R$ {total:,.2f}</b>',
    showarrow=False,
    font=dict(size=24)
    )

    base_chart_layout(fig)

    fig.update_layout(    
        showlegend=False,
        height=700
    )

    return fig



def expense_comparison_chart(df):
    chart_df = df.copy()    
    month_columns = [str(header) for header in chart_df.columns if header != 'Category']
    formatted_columns = {
    month: pd.to_datetime(month).strftime("%B - %Y")
    for month in month_columns
}
    chart_df = chart_df.rename(columns=formatted_columns)
    month_columns = list(formatted_columns.values())

    fig = px.bar(
        chart_df,
        x="Category",
        y=month_columns,
        barmode="group",
        title="Expense comparison",
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

    fig.update_layout(
    legend_title_text="Month",
    bargap=0.2,
    height=500
)
    base_chart_layout(fig)
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
    base_chart_layout(fig)

    fig.update_yaxes(
        tickprefix="R$ ",
        tickformat=",.2f",
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)" ,
        rangemode='tozero',
    )

    fig.update_traces(
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Value: R$ %{y:,.2f}"
        "<extra></extra>"
    )
)

    fig.update_layout(
    height=420
)
    
    return fig

def month_comparison_chart(df):
    df=df.reset_index()
    fig = px.bar(df, 
                 x='Difference (%)', 
                 y="Category", 
                 orientation='h',
                 title= 'Difference (%)')

    fig.update_layout(
    margin=dict(t=20),
    height=380
)

    return fig

     



def base_chart_layout(fig):
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

        