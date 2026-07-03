# Brief Summary - Week 7 Pandas Assignment

## Dataset Overview

This assignment uses a Superstore sales dataset containing customer orders, products, sales, quantity, discount, and profit details. The dataset has **9,994 rows** and **21 columns**.

## Work Completed

1. Loaded the raw CSV dataset into a Pandas DataFrame.
2. Explored the dataset using `head()`, `tail()`, `shape`, `columns`, and `dtypes`.
3. Checked missing values column-wise. The raw dataset had **0 missing values**.
4. Handled missing values using practical rules:
   - Text columns are filled with `Unknown`.
   - Numeric columns are filled using median values.
   - Date columns are parsed into proper datetime format.
5. Performed basic operations like filtering Technology orders with positive profit and selecting important columns.
6. Removed duplicate rows. The raw dataset had **0 duplicate rows**.
7. Created a derived `price` column using `Sales / Quantity`.
8. Created a derived `total_amount` column using `price * Quantity`.
9. Saved the cleaned dataset as `data/processed/cleaned_superstore_sales.csv`.

## Final Output

- Cleaned CSV file: `data/processed/cleaned_superstore_sales.csv`
- Notebook file: `notebooks/week7_pandas_data_cleaning.ipynb`
- Extra output files are stored inside the `outputs/` folder.

## Key Dataset Insights

- Total sales after cleaning: **$2,297,200.86**
- Total profit after cleaning: **$286,397.02**
- Total quantity sold: **37,873**
- Number of unique orders: **5,009**
- Best-selling category by sales: **Technology**
- Most profitable category: **Technology**

## Conclusion

The dataset was successfully loaded, explored, cleaned, transformed, and exported using Pandas. The final cleaned file is ready for further analysis or reporting.
