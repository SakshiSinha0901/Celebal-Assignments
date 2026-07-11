# Raw Data

This folder contains the original raw dataset used in the project.

The file `trustguard_retail_transactions.csv` contains retail transaction data with intentional data quality issues such as missing values, duplicate transaction IDs, inconsistent payment methods, city spelling mistakes, invalid quantities, and incorrect total amounts.

This file is used as the input source for the TrustGuard pipeline. The data is first uploaded to Databricks and then processed through the Raw, Clean, and Final layers.
