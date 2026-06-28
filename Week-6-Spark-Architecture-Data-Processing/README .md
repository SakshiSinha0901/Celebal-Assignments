# Week 6 Spark Assignment

## Spark Architecture and Efficient Data Processing

## Objective

The objective of this assignment is to understand Spark architecture and perform efficient data processing using Spark DataFrames.

This assignment covers Spark architecture, execution modes, Lazy Evaluation, DAG/Lineage Graph, CSV and Parquet file handling, filtering, schema handling, transformations, actions, Predicate Pushdown, and safe practices for working with large datasets.

## Assignment Questions Covered

This notebook answers the following Week 6 questions:

1. Role of Driver, Cluster Manager, and Executor in Spark
2. Lazy Evaluation and its performance benefits
3. Reading CSV files with header and inferSchema
4. Difference between CSV and Parquet
5. Selecting specific columns with filter conditions
6. Renaming columns and casting data types
7. DAG/Lineage Graph and fault tolerance
8. Filtering DataFrames using AND condition
9. Predicate Pushdown in Parquet
10. Adding a calculated column
11. Difference between Transformations and Actions
12. Reading Parquet, filtering null values, and saving output
13. Difference between Client Mode and Cluster Mode
14. Filtering DataFrames using OR condition
15. Why `.show(5)` is safer than `.collect()`

## Project Folder Structure

```text
Week-6-Spark-Architecture-Data-Processing/
│
├── data/
│   └── source.csv
│
├── outputs/
│   ├── csv_outputs/
│   │   ├── electronics_products/
│   │   ├── revised_dataframe/
│   │   ├── completed_orders/
│   │   ├── final_price_data/
│   │   └── region_priority_data/
│   │
│   ├── parquet_outputs/
│   │   └── parquet_input/
│   │
│   └── final_outputs/
│       ├── filtered_users_csv/
│       └── filtered_users_parquet/
│
├── Week6_Spark_Assignment_Final.ipynb
├── README.md
└── insights.md
```

## Tools and Technologies Used

- Python 3.12
- PySpark
- Spark DataFrames
- Pandas
- PyArrow
- Jupyter Notebook
- VS Code
- CSV
- Parquet

## Dataset Used

The assignment uses a sample CSV file stored at:

```text
data/source.csv
```

The dataset contains product and order-related columns such as:

- product_id
- product_name
- category
- price
- old_name
- status
- amount
- region
- priority
- base_price
- user_id

## Important Implementation Note

During local execution on Windows, Spark’s native `.write.csv()` and `.write.parquet()` operations can fail if Hadoop `winutils.exe` is not configured properly.

To avoid this Windows-specific issue, the notebook uses Spark for all DataFrame transformations and uses Pandas/PyArrow helper functions for saving final outputs into the `outputs` folder.

This keeps the assignment execution stable while still demonstrating the required Spark concepts and DataFrame operations.

## Steps Performed

### 1. Environment Setup

The notebook first checks and installs the required packages:

```python
pyspark
pandas
pyarrow
```

It also sets the working directory to the project folder and creates the required output folders.

### 2. Spark Session Creation

A local SparkSession is created using:

```python
SparkSession.builder.appName(...).master("local[*]").getOrCreate()
```

This allows Spark to run locally using available CPU cores.

### 3. CSV File Reading

The CSV file is read using:

```python
spark.read.option("header", True).option("inferSchema", True).csv("data/source.csv")
```

This ensures that the first row is treated as the header and Spark automatically detects column data types.

### 4. DataFrame Operations

The notebook performs multiple DataFrame operations, including:

- Selecting required columns
- Filtering rows
- Renaming columns
- Casting column data types
- Adding a calculated column
- Filtering null values
- Reading and saving Parquet data
- Saving processed outputs

### 5. Output Generation

The processed outputs are saved inside the `outputs` folder.

Generated outputs include:

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

## Key Spark Concepts Covered

### Driver

The Driver controls the Spark application. It creates the SparkSession, builds the execution plan, and coordinates tasks.

### Cluster Manager

The Cluster Manager provides resources like CPU and memory to the Spark application.

### Executor

Executors are worker processes that execute tasks and process data.

### Lazy Evaluation

Spark does not execute transformations immediately. It waits until an action is called, allowing Spark to optimize the full execution plan.

### DAG / Lineage Graph

Spark tracks transformations using a DAG. If a worker node fails, Spark can recompute only the lost partitions using the lineage information.

### Transformations

Transformations create a new DataFrame but do not execute immediately.

Examples:

```python
filter()
select()
withColumn()
withColumnRenamed()
```

### Actions

Actions trigger actual execution.

Examples:

```python
show()
count()
collect()
write()
```

### Predicate Pushdown

Predicate Pushdown helps Spark reduce the amount of data read from storage by applying filters closer to the data source, especially in Parquet files.

### CSV vs Parquet

CSV is row-based and simple to read, but it is less efficient for analytics.

Parquet is columnar and performs better for analytical workloads because Spark can read only the required columns.

## How to Run the Notebook

Open the project folder in VS Code.

Select the kernel:

```text
venv (Python 3.12.0)
```

Then open:

```text
Week6_Spark_Assignment_Final.ipynb
```

Run all cells from top to bottom.

## Expected Output

After successful execution, output files will be available inside:

```text
outputs/
```

The final output structure should include:

```text
outputs/
├── csv_outputs/
│   ├── electronics_products/
│   ├── revised_dataframe/
│   ├── completed_orders/
│   ├── final_price_data/
│   └── region_priority_data/
│
├── parquet_outputs/
│   └── parquet_input/
│
└── final_outputs/
    ├── filtered_users_csv/
    └── filtered_users_parquet/
```

## Conclusion

This assignment helped in understanding how Spark works internally and how Spark DataFrames can be used for efficient data processing.

It covered both architecture-level concepts and practical implementation, including reading files, applying transformations, filtering data, handling schemas, working with optimized file formats, and saving processed outputs.
