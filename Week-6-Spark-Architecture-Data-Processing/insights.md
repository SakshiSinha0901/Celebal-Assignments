# Week 6 Assignment Insights

## Overview

This assignment focused on understanding Spark architecture and performing efficient data processing using Spark DataFrames.

The work included both theoretical concepts and practical implementation using PySpark.

The main focus areas were Spark architecture, Lazy Evaluation, DAG/Lineage Graph, transformations, actions, schema handling, filtering, CSV vs Parquet, Predicate Pushdown, and safe handling of large datasets.

## 1. Spark Architecture

Spark applications mainly work through three important components:

1. Driver
2. Cluster Manager
3. Executors

The Driver controls the application and prepares the execution plan.

The Cluster Manager provides resources such as CPU and memory.

Executors perform the actual data processing tasks.

This structure allows Spark to process large datasets in a distributed and scalable way.

## 2. Driver, Cluster Manager, and Executor Roles

The Driver acts like the main controller of the Spark application. It creates the SparkSession and coordinates the complete job.

The Cluster Manager is responsible for resource allocation. It decides how much CPU and memory should be provided to the application.

Executors run the actual tasks on data partitions and return the results back to the Driver.

This separation of responsibilities makes Spark suitable for large-scale data processing.

## 3. Lazy Evaluation

Spark uses Lazy Evaluation, which means transformations are not executed immediately.

Instead, Spark waits until an action is called.

This improves performance because Spark gets time to build an optimized execution plan before running the job.

For example, if multiple filters and selections are applied, Spark can combine those operations and reduce unnecessary processing.

## 4. DAG and Fault Tolerance

Spark creates a DAG, also known as a Lineage Graph, to track all transformations applied to the data.

If any worker node fails, Spark uses this DAG to recompute only the lost partitions.

This provides fault tolerance because Spark does not need to restart the complete job from the beginning.

It can rebuild missing data from the original source and transformation steps.

## 5. CSV and Parquet File Formats

CSV is a row-based file format. It stores data row by row and is easy to read, but it is not very efficient for big data analytics.

Parquet is a columnar file format. It stores data column by column, which makes it better for analytical workloads.

When only a few columns are required, Parquet allows Spark to read only those columns instead of scanning the complete dataset.

This improves query performance and reduces memory usage.

## 6. Predicate Pushdown

Predicate Pushdown is an optimization technique where Spark pushes filter conditions closer to the data source.

In Parquet files, Spark can use metadata to skip unnecessary data blocks.

For example, if the filter condition is `region = 'North'`, Spark can skip blocks that do not contain matching records.

This reduces the amount of data loaded into memory and improves performance.

## 7. Transformations and Actions

Transformations are operations that create a new DataFrame from an existing DataFrame.

Examples of transformations include:

```python
filter()
select()
withColumn()
withColumnRenamed()
```

Actions are operations that trigger actual execution.

Examples of actions include:

```python
show()
count()
collect()
write()
```

The important learning is that transformations are lazy, while actions start the actual computation.

## 8. Filtering and Column Selection

Filtering and selecting only required columns improves performance.

In this assignment, records were filtered based on conditions such as:

- category is Electronics
- status is Completed and amount is greater than 1000
- region is North or priority is High
- user_id is not null

These filters help reduce unnecessary data processing.

## 9. Schema Handling

Schema handling is important when working with structured data.

The CSV file was read using `inferSchema=True`, so Spark automatically detected column data types.

The `price` column was also cast to Double to make sure it could be used properly for numerical operations.

## 10. Adding Calculated Columns

A new column called `final_price` was created by multiplying `base_price` by `1.18`.

This represents adding 18% tax to the base price.

This step shows how Spark DataFrames can be used to create derived columns during data transformation.

## 11. Null Value Handling

Rows where `user_id` was null were filtered out before saving the final output.

Handling null values is important because missing values can affect data quality and analysis results.

Filtering null values helps make the final dataset cleaner and more reliable.

## 12. Safe Dataset Exploration

Using `.show(5)` is safer than `.collect()` when working with large datasets.

`.show(5)` displays only the first 5 rows.

`.collect()` brings the entire dataset to the Driver machine.

For multi-terabyte datasets, `.collect()` can crash the Driver due to memory overload.

That is why `.show(5)` is the better option for quick data checking.

## 13. Output Handling

The notebook saves processed outputs inside the `outputs` folder.

The generated output files include:

```text
electronics_products.csv
revised_dataframe.csv
completed_orders.csv
final_price_data.csv
region_priority_data.csv
filtered_users.csv
source_data.parquet
filtered_users.parquet
execution_results_summary.txt
```

This makes the assignment easy to review because all output files are organized clearly.

## 14. Windows Execution Handling

During local Spark execution on Windows, native Spark write operations may fail due to Hadoop `winutils.exe` setup issues.

To avoid this, Spark was used for DataFrame processing, while Pandas and PyArrow helper functions were used for saving output files.

This allowed the complete notebook to run successfully and store outputs without Spark write errors.

## 15. Final Learning Summary

This assignment gave practical understanding of how Spark works and how DataFrames are used for processing structured data.

The most important learnings were:

1. Spark architecture is based on Driver, Cluster Manager, and Executors.
2. Lazy Evaluation improves performance by optimizing the execution plan.
3. DAG provides fault tolerance by recomputing lost partitions.
4. CSV is row-based, while Parquet is columnar and better for analytics.
5. Predicate Pushdown reduces unnecessary data loading.
6. Transformations define the processing steps.
7. Actions trigger actual execution.
8. Filtering early improves performance.
9. `.show(5)` is safer than `.collect()` for large datasets.
10. Output data was saved in a clean and organized way inside the `outputs` folder.

## Conclusion

The Week 6 assignment successfully covered Spark architecture and efficient data processing concepts.

It combined theory with practical PySpark implementation and produced organized output files for review.

The assignment also highlighted real-world performance concepts such as Lazy Evaluation, DAG, Predicate Pushdown, Parquet optimization, and safe handling of large datasets.
