# Week 7 - Pandas Data Exploration and Cleaning Assignment

## Objective

The objective of this assignment is to learn Python basics and perform basic data exploration and data cleaning using Pandas.

## Dataset

The dataset used in this assignment is a Superstore sales dataset. It contains order-level sales information such as order details, customer details, product details, sales, quantity, discount, and profit.

## Folder Structure

```
Week-7-Pandas-Data-Cleaning-Assignment/
│
├── data/
│   ├── raw/
│   │   └── superstore_sales.csv
│   └── processed/
│       └── cleaned_superstore_sales.csv
│
├── notebooks/
│   └── week7_pandas_data_cleaning.ipynb
│
├── outputs/
│   ├── category_summary.csv
│   ├── selected_columns_preview.csv
│   └── technology_profitable_orders.csv
│
├── README.md
├── requirements.txt
└── summary.md
```

## Steps Performed

1. Loaded the CSV dataset into a Pandas DataFrame.
2. Explored the dataset using `head()`, `tail()`, `shape`, `columns`, and `dtypes`.
3. Checked missing values and handled them using suitable cleaning rules.
4. Filtered rows and selected useful columns for analysis.
5. Removed duplicate rows from the dataset.
6. Created a derived `price` column using `Sales / Quantity`.
7. Created a derived `total_amount` column using `price * Quantity`.
8. Saved the cleaned dataset as a new CSV file.

## How to Run

Open the project folder in VS Code and run the notebook:

```bash
cd Week-7-Pandas-Data-Cleaning-Assignment
pip install -r requirements.txt
```

Then open this notebook:

```
notebooks/week7_pandas_data_cleaning.ipynb
```

Run all cells from top to bottom. The cleaned CSV will be saved automatically inside:

```
data/processed/cleaned_superstore_sales.csv
```

## Output Files

- `cleaned_superstore_sales.csv`: Final cleaned dataset.
- `category_summary.csv`: Sales and profit summary by product category.
- `technology_profitable_orders.csv`: Filtered Technology orders with positive profit.
- `selected_columns_preview.csv`: Preview of important selected columns.

## Tools Used

- Python
- Pandas
- Jupyter Notebook
- VS Code
