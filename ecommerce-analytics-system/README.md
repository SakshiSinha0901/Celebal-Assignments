# E-Commerce Order Analytics System

## Project overview

This project is an end-to-end e-commerce analytics system built with Python, Pandas, SQL, and SQLite. It starts by generating realistic customer, product, order, and order-item data. The raw data intentionally contains quality issues so that the cleaning process can demonstrate practical handling of null values, duplicates, invalid records, and broken relationships.

After cleaning, the data is loaded into a relational SQLite database with primary keys, foreign keys, `NOT NULL` rules, and validation checks. SQL queries are then used to produce revenue reports, product performance, customer rankings, monthly trends, cohort retention, and customer segments. A command-line interface allows these reports to be run directly from the terminal.

## Why SQLite is used

SQLite is used because it works locally, requires no separate database server, and is easy for a reviewer to run from VS Code. MySQL or PostgreSQL would also work, but they would require installation, configuration, credentials, and a running service. For this assignment, SQLite provides all required features, including joins, CTEs, window functions, constraints, and database connectivity from Python.

## System flow

Python data generation
        ↓
Raw CSV files with intentional issues
        ↓
Pandas cleaning and integrity validation
        ↓
Cleaned CSV files
        ↓
SQLite database with PK/FK constraints
        ↓
SQL analytics and segmentation
        ↓
CLI reports and saved sample outputs

## Folder structure

ecommerce-analytics-system/
├── data/
│   ├── raw/                 # Generated source data with intentional issues
│   └── cleaned/             # Final validated CSV files
├── database/
│   └── ecommerce_analytics.db
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   ├── report_cli.py
│   ├── export_sample_reports.py
│   └── run_all.py
├── sql/
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── window_functions.sql
│   ├── cohort_analysis.sql
│   └── customer_segmentation.sql
├── output/
│   ├── sample_reports/
│   └── screenshots/
├── tests/
│   └── test_edge_cases.py
├── requirements.txt
└── README.md

## Tools required

- VS Code
- Python 3.10 or later
- VS Code Python extension
- SQLite is included with Python, so a separate database installation is not required

## Setup and execution

Open this project folder in VS Code and run the following commands in the terminal.

### 1. Create a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the complete pipeline

python scripts/run_all.py

This command performs data generation, cleaning, database loading, integrity verification, and sample-report export.

## Run individual reports

python scripts/report_cli.py --report revenue
python scripts/report_cli.py --report top_customers --limit 10
python scripts/report_cli.py --report top_products --limit 10
python scripts/report_cli.py --report retention --limit 20
python scripts/report_cli.py --report segments --limit 15

Supported report names are:

- `revenue`
- `top_customers`
- `top_products`
- `retention`
- `segments`

CSV output can also be printed in the terminal:

python scripts/report_cli.py --report top_customers --limit 10 --format csv

## Data-quality issues intentionally included

The raw datasets include missing emails and cities, duplicated IDs, negative prices and stock, invalid and future dates, invalid quantities and discounts, and customer/order/product references that do not exist. These records are handled before loading data into SQL.

The cleaning process applies the following checks:

1. Removes duplicate primary-key records.
2. Standardizes text and fills selected missing values.
3. Converts dates and numeric columns safely.
4. Removes invalid prices, quantities, stock values, and discounts.
5. Removes future or unreadable order dates.
6. Validates customer IDs in orders.
7. Validates order and product IDs in order items.
8. Exports a cleaning summary showing raw, clean, and removed row counts.

## SQL analytics covered

- Revenue by customer, category, and month
- Top products by quantity and revenue
- Average order value by customer segment
- Customer lifetime-value ranking using `RANK()` and `DENSE_RANK()`
- Running revenue total and three-month moving average
- Month-over-month revenue growth using CTEs and `LAG()`
- Customer cohorts based on first purchase month
- Monthly cohort-retention percentages
- One-time, repeat, and churned customer identification
- Frequency, spend-tier, and RFM-style segmentation

## Edge-case handling

The CLI validates report names and limits, checks whether the database file exists, catches SQLite connection errors, and prints a readable message when a query returns no rows.

Run the included checks with:

python tests/test_edge_cases.py

## Main deliverables

- Raw CSV datasets
- Cleaned CSV datasets
- SQLite database
- Python scripts for generation, cleaning, loading, and reporting
- SQL schema and analytics queries
- Sample report files in CSV and text formats
- Edge-case tests
- Execution screenshots

## Conclusion

The project demonstrates a complete analytics workflow rather than only a collection of SQL queries. It shows how raw data can be generated, checked, cleaned, stored with relational rules, analyzed for business insights, and exposed through a simple reporting interface.
