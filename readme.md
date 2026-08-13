# Personal Finance Dashboard

A personal finance dashboard built with Python and Streamlit to transform raw bank transaction data into useful financial insights.

The project started as a way to analyze my own bank statements and evolved into a modular application capable of processing multiple monthly CSV files, categorizing transactions, comparing expenses across periods, and tracking investment evolution.

> The repository does not contain real financial data. Personal bank statements are excluded from version control.

## Features

### Financial Indicators

View the main financial indicators for a selected month:

- Total income
- Total expenses
- Remaining balance
- Net amount invested

### Expenses by Category

Analyze spending across different categories and periods.

The dashboard allows users to:

- Select one or multiple expense categories
- Select one or multiple months
- Compare spending between periods
- View average monthly expenses for the selected filters

### Investment Evolution

Tracks the cumulative evolution of investments over time, considering both:

- Investment deposits
- Investment withdrawals

Months without investment activity are also included in the timeline.

### Month Comparison

Compare expenses between any two available months.

The comparison includes:

- Expense by category for each month
- Percentage change between the selected periods
- Visual comparison through charts

### Transactions

Explore individual transactions using filters for:

- Month
- Category

This provides a detailed view behind the aggregated dashboard indicators.

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly

## Project Structure

```text
finance-dashboard/
│
├── app.py
├── categories.py
├── extract.py
├── file_picker.py
├── graphs.py
├── transform.py
├── validation.py
├── .gitignore
└── README.md
```

### `app.py`

Main Streamlit application and user interface.

### `extract.py`

Handles CSV loading and data extraction.

### `validation.py`

Validates imported files before processing.

### `transform.py`

Contains data transformation, aggregation and financial indicator logic.

### `categories.py`

Contains the rules used to categorize transactions.

### `graphs.py`

Contains Plotly chart functions used by the dashboard.

## Data Pipeline

The basic processing flow is:

```text
Bank CSV files
      ↓
File validation
      ↓
Data extraction
      ↓
Date and data transformation
      ↓
Transaction categorization
      ↓
Financial aggregation
      ↓
Streamlit dashboard
```

This structure separates data processing from visualization and interface logic.

## Running the Project

Clone the repository:

```bash
git clone git@github.com:leonardobscherer/finance-dashboard.git
cd finance-dashboard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install pandas streamlit plotly
```

Run the application:

```bash
streamlit run app.py
```

## Data Privacy

This project was developed using personal banking data.

For privacy and security reasons, real financial CSV files are excluded from the repository through `.gitignore`.

Users should provide their own compatible CSV files when running the application.

## What I Practiced

This project was developed as part of my transition into the data field and gave me practical experience with:

- Data cleaning and transformation with Pandas
- DataFrame filtering and aggregation
- `groupby`, `isin`, `reindex`, `cumsum` and other Pandas operations
- Working with time-based financial data
- Building reusable Python functions
- Separating extraction, transformation and visualization logic
- Interactive data visualization with Plotly
- Building a dashboard with Streamlit
- Git and GitHub version control

## Future Improvements

Possible future improvements include:

- Editable transaction categories
- Improved error handling
- Additional financial indicators
- Better dashboard layout and styling
- Automated tests
- Configuration files for category rules
- Deployment with Streamlit Community Cloud

## Author

**Leonardo Scherer**

Mechanical Engineer transitioning into Data Analytics and Data Engineering, with experience in engineering, technical support, process analysis and automation.

This project is part of my data portfolio.