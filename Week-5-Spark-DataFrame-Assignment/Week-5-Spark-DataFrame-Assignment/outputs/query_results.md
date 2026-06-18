# Query Results Summary

## Dataset Used

The assignment uses a sample sales dataset to perform Spark DataFrame operations. The dataset contains details such as user ID, transaction date, region, product category, sale amount, city, age, subscription type, status, timestamp, email, username, price, store ID, and quantity.

The main purpose of using this dataset is to demonstrate data cleaning, filtering, transformation, grouping, aggregation, schema modification, and final data processing using PySpark.

---

## Q3: Duplicate Removal

Duplicate rows were removed using the `dropDuplicates()` function.

The duplicate check was performed based on the following columns:

* `user_id`
* `transaction_date`

Code used:

```python
df_no_duplicates = df.dropDuplicates(["user_id", "transaction_date"])
```

### Result

The duplicate transaction record having the same `user_id` and `transaction_date` was removed from the DataFrame.

### Insight

Removing duplicate records helps improve data quality and avoids incorrect results during analysis or aggregation.

---

## Q4: West Region Average Sales

The dataset was filtered for records where the region is `West`.

After filtering, the data was grouped by `product_category`, and the average `sale_amount` was calculated.

Code used:

```python
west_avg_sales = df.filter(col("region") == "West") \
    .groupBy("product_category") \
    .agg(avg("sale_amount").alias("average_sale_amount"))
```

### Result

The output shows the average sale amount for each product category in the West region.

### Insight

This helps understand which product categories perform better in a specific region.

---

## Q5: Null Status Handling

Null values in the `status` column were filled with the value `Unknown`.

Code used:

```python
df_status_filled = df.na.fill({"status": "Unknown"})
```

### Result

Blank or missing values in the `status` column were replaced with `Unknown`.

### Insight

Handling null values makes the dataset cleaner and prevents missing values from creating confusion during analysis.

---

## Q6: City Count Greater Than 100

Records were grouped by `city`, and the total number of records for each city was calculated.

Only cities where the count is greater than 100 were selected.

Code used:

```python
city_count = df.groupBy("city") \
    .agg(count("*").alias("total_records")) \
    .filter(col("total_records") > 100)
```

### Result

Since the sample dataset is small, the output may be empty.

### Insight

The query logic is correct. In a larger dataset, this query would return cities that have more than 100 records.

---

## Q8: Premium Users Between Age 18 and 30

The dataset was filtered for users where:

* Age is between 18 and 30
* Subscription type is `Premium`

Code used:

```python
filtered_df = df.filter(
    (col("age") >= 18) &
    (col("age") <= 30) &
    (col("subscription") == "Premium")
)
```

### Result

The output shows users who are between 18 and 30 years old and have a Premium subscription.

### Insight

Filtering helps extract specific records from a dataset based on business conditions.

---

## Q10: Timestamp Conversion and Column Rename

The `raw_timestamp` column was converted to `TimestampType`.

After casting, the column was renamed to `event_time`.

Code used:

```python
df_timestamp = df.withColumn(
    "raw_timestamp",
    col("raw_timestamp").cast(TimestampType())
).withColumnRenamed("raw_timestamp", "event_time")
```

### Result

The schema was updated, and the timestamp column was converted into the correct timestamp format.

### Insight

Correct data types are important for time-based filtering, sorting, and analysis.

---

## Q12: Removing Invalid User Records

Rows were removed where:

* `email` is null
* `username` is an empty string

Code used:

```python
df_cleaned_users = df.filter(
    col("email").isNotNull() &
    (col("username") != "")
)
```

### Result

Records with missing email values or empty usernames were removed.

### Insight

This improves the quality of user-related data and ensures that only valid user records are kept.

---

## Q13: Price Statistics

The `.agg()` function was used to calculate multiple statistics on the `price` column.

The following values were calculated:

* Minimum price
* Maximum price
* Average price

Code used:

```python
price_stats = df.agg(
    min("price").alias("minimum_price"),
    max("price").alias("maximum_price"),
    mean("price").alias("average_price")
)
```

### Result

The output displays the minimum, maximum, and average price from the dataset.

### Insight

Aggregation functions help summarize numerical data and understand the overall range and average of values.

---

## Q15: Final Processing Pipeline

The final pipeline combines cleaning, transformation, and aggregation steps.

The pipeline performs the following operations:

1. Removes duplicate rows.
2. Fills null values in the `price` column with 0.
3. Creates a new `revenue` column using `price * quantity`.
4. Groups the data by `store_id`.
5. Calculates total revenue for each store.

Code used:

```python
final_pipeline = df.dropDuplicates() \
    .na.fill({"price": 0}) \
    .withColumn("revenue", col("price") * col("quantity")) \
    .groupBy("store_id") \
    .agg(sum("revenue").alias("total_revenue"))
```

### Result

The output shows the total revenue generated by each store.

### Insight

This final pipeline demonstrates how multiple Spark DataFrame operations can be combined to create a complete data processing workflow.

---

## Final Summary

This assignment demonstrates the practical use of Spark DataFrames for data processing.

The main operations performed include:

1. Removing duplicate records.
2. Handling null values.
3. Filtering data using multiple conditions.
4. Grouping records using `groupBy()`.
5. Performing aggregations using `count()`, `avg()`, `min()`, `max()`, `mean()`, and `sum()`.
6. Modifying schema by casting and renaming columns.
7. Building a complete processing pipeline.

Overall, this assignment shows how PySpark can be used to clean, transform, and analyze structured data efficiently.
