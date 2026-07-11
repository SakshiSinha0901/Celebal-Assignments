# Outputs

This folder represents the expected output structure for the TrustGuard pipeline.

The project was executed mainly on Databricks, so the actual outputs were created as Delta tables inside Databricks instead of being directly saved into this local folder.

The main output tables created in Databricks are:

- raw_transactions
- dq_report
- rejected_records
- clean_transactions
- clean_customers
- final_transactions
- customer_summary
- city_sales_report
- payment_method_report
- product_category_report
- anomaly_log
- pipeline_log

The output results are shown in the exported Databricks notebook and screenshots folder.

This folder is kept to show the planned output organization for the project.