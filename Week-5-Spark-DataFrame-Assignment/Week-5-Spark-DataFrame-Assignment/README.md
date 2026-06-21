# Week 5 Spark DataFrame Assignment

## Objective

The objective of this assignment is to understand the basics of Apache Spark and perform common data processing operations using Spark DataFrames.

This assignment covers both theoretical concepts and practical PySpark implementation. The main focus is on data cleaning, filtering, transformation, grouping, aggregation, schema modification, and building a simple end-to-end data processing pipeline.

---

## Assignment Overview

In this assignment, a sample sales dataset is used to practice Spark DataFrame operations. The dataset contains transaction and user-related information such as user ID, transaction date, region, product category, sale amount, city, age, subscription type, status, timestamp, email, username, price, store ID, and quantity.

The assignment is divided into theory-based and code-based questions. Theory questions explain important Spark concepts like MapReduce limitations, in-memory computing, DataFrame immutability, shuffle, and schema inference. Code-based questions demonstrate how these concepts are applied practically using PySpark.

---

## Tools and Technologies Used

* Python
* Apache Spark
* PySpark
* Jupyter Notebook
* VS Code
* Java JDK

---

## Folder Structure

```text
Week-5-Spark-DataFrame-Assignment/
│
├── data/
│   └── sample_sales_data.csv
│
├── outputs/
│   └── query_results.md
│   └── results.csv
├── screenshots/
│
├── Week5_Spark_Assignment.ipynb
├── README.md
└── requirements.txt
```

---

## Files Included

### `Week5_Spark_Assignment.ipynb`

This is the main assignment notebook. It contains all 15 questions with their solutions.

The notebook includes:

* Markdown cells for theory answers
* Code cells for PySpark implementation
* Output tables for practical questions
* Final summary and insights

### `data/sample_sales_data.csv`

This is the sample dataset used for the assignment. It contains sales, user, product, and store-related fields.

### `outputs/query_results.md`

This file contains a short summary of the output and insights for the code-based questions.

### `screenshots/`

This folder contains screenshots of important notebook outputs, such as dataset loading, duplicate removal, aggregation results, timestamp conversion, and final pipeline output.

### `requirements.txt`

This file contains the Python packages required to run the notebook.

---

## Requirements

The following packages are required:

```txt
pyspark==4.1.2
notebook==7.5.7
ipykernel==7.3.0
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## How to Run the Assignment

### Step 1: Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 3: Open the Notebook

Open the file:

```text
Week5_Spark_Assignment.ipynb
```

### Step 4: Select Kernel

Select the virtual environment kernel in Jupyter Notebook or VS Code.

Example:

```text
venv (Python 3.12.0)
```

### Step 5: Run All Cells

Run the notebook cells from top to bottom.

---

## Operations Performed

### 1. Spark Session Creation

A Spark session was created to start working with PySpark DataFrames.

```python
spark = SparkSession.builder \
    .appName("Week 5 Spark DataFrame Assignment") \
    .getOrCreate()
```

This is the starting point for using Spark in the notebook.

---

### 2. Dataset Loading

The CSV dataset was loaded into a Spark DataFrame using:

```python
df = spark.read.csv(
    "data/sample_sales_data.csv",
    header=True,
    inferSchema=True
)
```

The dataset was displayed using `df.show()` and its schema was checked using `df.printSchema()`.

---

### 3. Duplicate Removal

Duplicate rows were removed using `dropDuplicates()`.

```python
df_no_duplicates = df.dropDuplicates(["user_id", "transaction_date"])
```

This helps clean repeated transaction records based on `user_id` and `transaction_date`.

---

### 4. Filtering Data

Filtering was performed to select specific records from the dataset.

For example, users between age 18 and 30 with a Premium subscription were selected using:

```python
filtered_df = df.filter(
    (col("age") >= 18) &
    (col("age") <= 30) &
    (col("subscription") == "Premium")
)
```

Filtering helps extract useful records based on given conditions.

---

### 5. Grouping and Aggregation

The dataset was grouped by different columns and aggregation functions were applied.

For example, average sale amount was calculated for each product category in the West region:

```python
west_avg_sales = df.filter(col("region") == "West") \
    .groupBy("product_category") \
    .agg(avg("sale_amount").alias("average_sale_amount"))
```

Aggregation functions used in this assignment include:

* `count()`
* `avg()`
* `sum()`
* `min()`
* `max()`
* `mean()`

---

### 6. Null Value Handling

Null values were handled using `.na.fill()`.

For example, missing values in the `status` column were filled with `Unknown`:

```python
df_status_filled = df.na.fill({"status": "Unknown"})
```

This makes the dataset cleaner and easier to analyze.

---

### 7. Schema Modification

The `raw_timestamp` column was converted to `TimestampType` and renamed to `event_time`.

```python
df_timestamp = df.withColumn(
    "raw_timestamp",
    col("raw_timestamp").cast(TimestampType())
).withColumnRenamed("raw_timestamp", "event_time")
```

This step shows how to modify column data types and rename columns in Spark.

---

### 8. Removing Invalid Records

Rows with missing email values or empty usernames were removed.

```python
df_cleaned_users = df.filter(
    col("email").isNotNull() &
    (col("username") != "")
)
```

This helps keep only valid user records in the dataset.

---

### 9. Multiple Aggregations Using `.agg()`

The `.agg()` function was used to calculate multiple statistics at once.

```python
price_stats = df.agg(
    min("price").alias("minimum_price"),
    max("price").alias("maximum_price"),
    mean("price").alias("average_price")
)
```

This gives a quick summary of the `price` column.

---

### 10. Final Processing Pipeline

A final data processing pipeline was created by combining multiple operations.

```python
final_pipeline = df.dropDuplicates() \
    .na.fill({"price": 0}) \
    .withColumn("revenue", col("price") * col("quantity")) \
    .groupBy("store_id") \
    .agg(sum("revenue").alias("total_revenue"))
```

The pipeline performs:

1. Duplicate removal
2. Null price replacement with 0
3. Revenue calculation using `price * quantity`
4. Grouping by `store_id`
5. Total revenue calculation for each store

This shows how Spark can be used to build a clean and simple data processing workflow.

---

## Theory Concepts Covered

### Limitations of MapReduce

Traditional MapReduce is slower because it writes intermediate results to disk after each step. It is also less suitable for iterative tasks like machine learning. Spark improves this by using in-memory processing.

### In-Memory Computing

Spark can keep intermediate data in memory, which makes repeated processing much faster compared to disk-based systems.

### DataFrame Immutability

Spark DataFrames are immutable. This means every transformation creates a new DataFrame instead of changing the original one.

### Shuffle and Wide Transformation

Shuffle happens when Spark moves data across partitions, usually during operations like `groupBy()`. It is called a wide transformation because data from multiple partitions is reorganized.

### Schema Inference Risk

Using `inferSchema=True` is convenient, but it can be risky when the dataset has messy or inconsistent date formats. Spark may infer the wrong data type in such cases.

---

## Final Summary

This assignment helped in understanding how Spark DataFrames are used for real-world data processing tasks.

The practical work included loading data, removing duplicates, handling null values, filtering records, grouping data, calculating aggregations, modifying schema, and creating a final revenue pipeline.

Overall, this assignment gives a basic but clear understanding of how PySpark can be used for data cleaning, transformation, and analysis.
