# Output Tables

This file explains the output tables created by the TrustGuard pipeline.

## 1. raw_transactions

This table stores the original uploaded retail transaction data with metadata columns such as `run_id`, `load_timestamp`, and `source_file_name`.

## 2. dq_report

This table stores the data quality check results. It shows how many records passed and failed each check.

## 3. rejected_records

This table stores invalid records that failed important quality checks. Each record has a `rejection_reason` column so that the issue can be reviewed later.

## 4. clean_transactions

This table stores cleaned transaction records after applying standardization, validation, and deduplication rules.

## 5. clean_customers

This table stores unique customer records extracted from clean transaction data.

## 6. final_transactions

This is the main final table. It contains clean transaction data joined with customer information. This table is used for reporting and analysis.

## 7. customer_summary

This table gives customer-level summary information such as total orders, total spend, average order value, first purchase date, and last purchase date.

## 8. city_sales_report

This table shows city-wise and month-wise sales performance. It includes total orders, total revenue, and average order value.

## 9. payment_method_report

This table shows how many transactions and how much revenue came from each payment method.

## 10. product_category_report

This table shows sales performance by product category.

## 11. anomaly_log

This table stores transactions that look unusual, such as very high quantity or very high total amount.

## 12. pipeline_log

This table tracks the pipeline run details. It shows how many records entered each layer, how many came out, how many were rejected, and whether the step completed successfully.
