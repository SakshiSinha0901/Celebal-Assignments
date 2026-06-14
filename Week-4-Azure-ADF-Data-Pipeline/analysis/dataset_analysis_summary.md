# Dataset Analysis Summary

## Dataset Used

The dataset used for this assignment is the Superstore dataset from Kaggle.

Dataset Source:

https://www.kaggle.com/datasets/vivek468/superstore-dataset-final


The dataset is available in CSV format and contains sales-related records for a superstore business. It includes information about orders, customers, products, categories, regions, sales, quantity, discount, and profit.

## Purpose of Dataset Analysis

Before uploading the dataset to Azure Blob Storage and using it in Azure Data Factory, basic data analysis was performed using Python and Pandas.

The purpose of this analysis was to understand the structure, quality, and usability of the dataset before performing cloud-based pipeline operations.

## Dataset Overview

The dataset contains order-level sales data. Each row represents a sales transaction, and each column provides details related to that transaction.

The important columns in the dataset include:

* Row ID
* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* Country
* City
* State
* Postal Code
* Region
* Product ID
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

## Analysis Performed

The following analysis steps were performed on the dataset:

### 1. Loaded the Dataset

The CSV file was loaded into a Pandas DataFrame using `read_csv()`.

This helped in reading the dataset and preparing it for basic analysis.

### 2. Checked Dataset Shape

The total number of rows and columns were checked using the `shape` function.

This helped in understanding the size of the dataset.

### 3. Viewed First Few Records

The first few records were displayed using the `head()` function.

This helped in getting a quick preview of the data and understanding how the records are structured.

### 4. Checked Column Names

All column names were reviewed to understand what type of information is available in the dataset.

The dataset contains columns related to order details, customer details, product details, location, sales, quantity, discount, and profit.

### 5. Checked Data Types

The data types of all columns were checked using `dtypes`.

This helped in identifying which columns contain text values, numerical values, and date-related values.

### 6. Checked Missing Values

Missing values were checked using `isnull().sum()`.

This helped in identifying whether any column had null or empty values.

### 7. Checked Duplicate Records

Duplicate rows were checked using `duplicated().sum()`.

This helped in verifying whether the dataset had repeated records.

### 8. Generated Numerical Summary

A numerical summary was generated using `describe()`.

This provided basic statistical details for numerical columns such as:

* Sales
* Quantity
* Discount
* Profit

The summary included count, mean, minimum, maximum, and percentile values.

### 9. Reviewed Category-wise Data

The product categories were reviewed to understand the distribution of records across different categories.

The major categories in the dataset are:

* Furniture
* Office Supplies
* Technology

### 10. Reviewed Region-wise Data

Region-wise data was checked to understand how the records are distributed across different regions.

The dataset includes regions such as:

* East
* West
* Central
* South

## Key Observations

* The dataset contains structured sales transaction data.
* The dataset has useful business columns such as Sales, Quantity, Discount, and Profit.
* The dataset also contains categorical columns such as Category, Sub-Category, Segment, Region, and Ship Mode.
* The data is suitable for building a basic Azure Data Factory pipeline.
* The dataset can be used as a source file in Azure Blob Storage.
* No major transformation was required before uploading the file because the main objective of this assignment was to create a data pipeline and copy the file from source to destination.
* The source CSV file was successfully used for metadata validation and copy activity in Azure Data Factory.

## Use of Dataset in Azure Pipeline

After the dataset analysis was completed, the CSV file was uploaded to the `source` container in Azure Blob Storage.

The file was then used as the source dataset in Azure Data Factory.

The pipeline performed the following steps:

```txt
CSV File
    ↓
Source Blob Container
    ↓
Get Metadata Activity
    ↓
Copy Data Activity
    ↓
Destination Blob Container
```

The Get Metadata activity was used to validate the source file details, and the Copy Data activity was used to copy the file to the destination container.

## Conclusion

The Superstore dataset was successfully analyzed before performing Azure operations.

The analysis helped in understanding the structure and quality of the dataset. After validation, the dataset was uploaded to Azure Blob Storage and used as the input file for the Azure Data Factory pipeline.

The dataset was suitable for this assignment because it is structured, easy to understand, and contains meaningful business data for pipeline implementation.
