# SQL Subqueries, CTEs and Window Functions Assignment

## Objective

The objective of this assignment is to analyze Superstore sales data using SQL concepts such as Subqueries, Common Table Expressions and Window Functions.

## Dataset

The dataset used is the Superstore sales dataset. It contains order, customer, product, sales, quantity, discount and profit details.

## Tables Created
1. superstore_raw

This is the main raw table created directly from the Superstore CSV file.
It contains the complete dataset without splitting it into separate tables.

2. customers

This table contains unique customer details such as customer ID, customer name, segment, city, state, country, postal code, and region.

3. orders

This table contains order-related details such as order ID, order date, ship date, ship mode, customer ID, product ID, sales, quantity, discount, and profit.

4. products

This table contains product-related details such as product ID, category, sub-category, and product name.

## SQL Concepts Used

The following SQL concepts are used in this assignment:

1. Subqueries
Used to compare sales values with average sales and to find the highest order value for each customer.

2. Common Table Expressions
Used to calculate total sales per customer and make complex queries easier to read.

3. Window Functions
Used to rank customers and assign row numbers to orders within each customer.

4. JOIN
Used in the final query to combine customer information with sales ranking.

5. Aggregate Functions
Used for calculations like total sales, average sales, maximum sales, and order count.

## Queries Performed

The assignment includes SQL queries for the following tasks:

1. Find all orders where sales are greater than the average sales.

2. Find the highest sales order for each customer.

3. Calculate total sales for each customer.

4. Find customers whose total sales are above average.

5. Rank all customers based on total sales.

6. Assign row numbers to each order within a customer.

7. Display the top 3 customers based on total sales.

8. Create a final combined query using JOIN, CTE, and Window Function.

## Mini Project: Customer Sales Insights

The mini project answers the following business questions:

1. Who are the top 5 customers?
2. Who are the bottom 5 customers?
3. Which customers made only one order?
4. Which customers have above-average sales?
5. What is the highest order value per customer?


## Output

The project generates a SQLite database file:

superstore_sales.db

1. It also generates query output files inside the results folder.

2. These CSV files make it easier to review the results directly on GitHub.

# Note About the Database File

The "superstore_sales.db" file is a SQLite database file. GitHub may not preview this file directly because database files are not meant to be viewed like normal text or CSV files.

To review the work, please check:

1. superstore_analysis.sql for all SQL queries.
2. results/ folder for exported query outputs.
3. insights.md for a short explanation of the findings.

To open the database locally, download the project and open "superstore_sales.db" using DB Browser for SQLite or any SQLite viewer extension in VS Code.

## Conclusion

This assignment helped me understand how SQL can be used for business analysis.

Using Subqueries, CTEs, Window Functions, and JOINs made it easier to analyze customer sales, rank customers, identify high-value customers, and find useful sales patterns from the Superstore dataset.