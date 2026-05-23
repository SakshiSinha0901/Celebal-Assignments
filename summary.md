# Basic Data Exploration and Cleaning using Pandas

## Objective

The objective of this assignment was to learn basic Python and Pandas operations by performing data exploration and cleaning on a shopping dataset.

## Dataset Used

Shopping Dataset from Kaggle.

## Steps Performed

1. Loaded the CSV dataset into a Pandas DataFrame.
2. Explored the dataset using head, tail, shape, columns, data types, and info.
3. Checked missing values using isnull().sum().
4. Handled missing values by filling text columns with "Unknown" and numeric columns with median values.
5. Selected important columns for basic analysis.
6. Filtered rows where purchase amount was greater than 50 USD.
7. Removed duplicate rows from the dataset.
8. Created a derived column named total_amount.
9. Saved the cleaned dataset as a new CSV file.

## Output Files

- Notebook: notebooks/basic_data_exploration_cleaning.ipynb
- Cleaned CSV: data/processed/cleaned_shopping_data.csv
- Summary: summary.md

## Conclusion

This assignment helped in understanding the basic workflow of data exploration and cleaning using Pandas. The cleaned dataset is now ready for further analysis.