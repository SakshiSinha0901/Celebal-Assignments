# Project Summary

TrustGuard is a data quality pipeline created for retail transaction data. The project focuses on identifying and handling common data issues such as missing values, duplicate records, inconsistent formats, invalid quantities, incorrect total amounts, and spelling mistakes in city names.

The project is built using Databricks, PySpark, SQL, and Delta Lake. It follows the Medallion Architecture, where data moves from the Raw Layer to the Clean Layer and then to the Final Layer.

## Raw Layer

In the Raw Layer, the dataset is stored without making any changes. This helps preserve the original source data. If any issue happens in later steps, the raw data can be used again for reprocessing.

## Clean Layer

In the Clean Layer, different cleaning rules are applied. The pipeline standardizes dates, payment methods, city names, gender values, and active status values. It also checks for invalid quantities, missing IDs, and incorrect amount calculations.

## Rejected Records

Records that fail important checks are moved to the rejected records table. This makes the pipeline transparent because no bad record is silently removed.

## Final Layer

In the Final Layer, clean and reliable tables are created for business analysis. These tables are used to generate customer summaries, city-wise sales reports, payment method reports, and product category reports.

## Monitoring

The project also includes a data quality report, anomaly log, and pipeline log to track the health and status of the pipeline.

## Final Result

At the end of the pipeline, the raw retail dataset is converted into clean, consistent, and analysis-ready tables that can be used for reporting and decision-making.
