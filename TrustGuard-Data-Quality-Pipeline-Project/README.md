# TrustGuard: Data Quality Pipeline for Retail Data

## Project Overview

TrustGuard is an end-to-end data quality pipeline built for retail transaction data. The main purpose of this project is to take raw and inconsistent retail data, check it for common data quality problems, clean it properly, and prepare final tables that can be used for reporting and analysis.

The project is built using Python, PySpark, SQL, Delta Lake, and Databricks. It follows the Medallion Architecture, where the data moves through three layers:

```text
Raw Layer → Clean Layer → Final Layer
```

This layered structure helps keep the original data safe, apply cleaning rules step by step, and create reliable datasets for business use.

## Business Problem

Retail data usually comes from different systems such as stores, online orders, customer platforms, and payment systems. Because of this, the data can contain issues like missing values, duplicate records, different date formats, incorrect total amounts, and inconsistent values such as `UPI`, `upi`, `U.P.I.`, `Cash`, and `CASH`.

If these issues are not handled, business reports like revenue, customer count, product sales, and city-wise sales can become incorrect. TrustGuard solves this by validating and cleaning the data before it is used for analysis.

## Tech Stack Used

- Python
- PySpark
- SQL
- Delta Lake
- Databricks
- VS Code
- GitHub

## Architecture

The project follows a simple three-layer architecture.

### 1. Raw Layer

The Raw Layer stores the data exactly as it is received from the source. No cleaning or transformation is done in this layer. This helps preserve the original dataset for audit, debugging, and reprocessing.

### 2. Clean Layer

The Clean Layer applies data quality checks and cleaning rules. In this layer, missing values are handled, duplicate records are removed, dates are standardized, text values are cleaned, and invalid records are separated.

### 3. Final Layer

The Final Layer contains clean and analysis-ready data. This layer is used to generate business reports such as customer summary, city sales report, payment method report, and product category report.

## Dataset Used

The dataset used in this project is:

```text
trustguard_retail_transactions.csv
```

It contains retail transaction records with intentional data quality issues such as:

- Missing product categories
- Missing customer details
- Duplicate transaction IDs
- Incorrect total amount values
- Mixed date formats
- Inconsistent payment method values
- City spelling mistakes
- Invalid quantity values

These issues make the dataset suitable for building and testing a data quality pipeline.

## Main Pipeline Steps

1. Load raw retail transaction data.
2. Validate the schema.
3. Store raw data in the Raw Layer.
4. Run data quality checks.
5. Clean and standardize the data.
6. Move invalid records to rejected records.
7. Create clean transaction and customer tables.
8. Build final analysis-ready tables.
9. Generate SQL reports.
10. Create anomaly log and pipeline log.

## Output Tables

The project creates the following tables:

- `raw_transactions`
- `dq_report`
- `rejected_records`
- `clean_transactions`
- `clean_customers`
- `final_transactions`
- `customer_summary`
- `city_sales_report`
- `payment_method_report`
- `product_category_report`
- `anomaly_log`
- `pipeline_log`

## Folder Structure

```text
TrustGuard-Data-Quality-Pipeline/
│
├── data/
│   └── raw/
│       └── trustguard_retail_transactions.csv
│
├── docs/
├── notebooks/
├── outputs/
├── screenshots/
├── README.md
├── COMMANDS_TO_RUN.md
└── requirements.txt
```

## Final Outcome

After running the pipeline, the final data becomes clean, consistent, and ready for analysis. Invalid records are not deleted silently. They are stored separately with proper rejection reasons, which makes the pipeline more transparent and easier to debug.

This project helped me understand how a real data engineering pipeline works using Databricks, PySpark, SQL, Delta Lake, and Medallion Architecture.

## Output Storage Note

The main project execution was done on Databricks. Because Databricks runs in the cloud, the output tables are created and stored inside Databricks as Delta tables, not directly inside the local VS Code outputs folder.

The local outputs folder has been kept in the project structure to represent the expected output categories such as data quality reports, rejected records, final reports, anomaly logs, and pipeline logs.

The actual output results can be verified through:

- The exported Databricks notebook
- The screenshots added inside the screenshots folder
- The Delta tables created in Databricks under the trustguard_db schema