# Project Architecture

TrustGuard follows the Medallion Architecture.

The data moves through three main layers:

Raw Layer → Clean Layer → Final Layer


## 1. Raw Layer

The Raw Layer stores the data exactly as it comes from the source. No cleaning or transformation is done in this layer.

This layer is useful because it keeps the original data safe. If something goes wrong in later steps, we can always come back to the raw data and process it again.

Table created in this layer:

raw_transactions


## 2. Clean Layer

The Clean Layer is where the main data quality work happens.

In this layer, the pipeline performs:

- Missing value checks
- Duplicate record removal
- Date standardization
- Payment method standardization
- City name correction
- Gender value standardization
- Type casting
- Amount validation
- Invalid record separation

Tables created in this layer:

clean_transactions
clean_customers
rejected_records
dq_report


## 3. Final Layer

The Final Layer contains clean and analysis-ready data. This layer is used for business reporting and SQL analysis.

Tables created in this layer:


final_transactions
customer_summary
city_sales_report
payment_method_report
product_category_report
anomaly_log
pipeline_log


## Simple Flow


Raw CSV Dataset
      ↓
Raw Delta Table
      ↓
Data Quality Checks
      ↓
Cleaned Data + Rejected Records
      ↓
Final Tables
      ↓
SQL Reports and Logs


This architecture makes the project easy to understand, maintain, and explain.
