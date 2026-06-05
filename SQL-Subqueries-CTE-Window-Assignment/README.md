# SQL Subqueries, CTEs and Window Functions Assignment

## Objective

The objective of this assignment is to analyze Superstore sales data using SQL concepts such as Subqueries, Common Table Expressions and Window Functions.

## Dataset

The dataset used is the Superstore sales dataset. It contains order, customer, product, sales, quantity, discount and profit details.

## Tables Created

### 1. superstore_raw

This table contains the complete raw dataset imported from the CSV file.

### 2. customers

This table contains distinct customer details such as customer ID, customer name, segment, country, city, state, postal code and region.

### 3. orders

This table contains order-level details such as order ID, order date, ship date, ship mode, customer ID, product ID, sales, quantity, discount and profit.

### 4. products

This table contains product details such as product ID, category, sub-category and product name.

## SQL Concepts Used

1. Subqueries
2. Common Table Expressions
3. Window Functions
4. ROW_NUMBER
5. RANK
6. JOIN
7. GROUP BY
8. HAVING
9. Aggregate functions

## Queries Performed

1. Orders where sales are greater than average sales.
2. Highest sales order for each customer.
3. Total sales for each customer.
4. Customers whose total sales are above average.
5. Rank customers based on total sales.
6. Assign row numbers to orders within each customer.
7. Display top 3 customers based on total sales.
8. Final combined query using JOIN, CTE and Window Function.

## Mini Project: Customer Sales Insights

The mini project answers the following business questions:

1. Who are the top 5 customers?
2. Who are the bottom 5 customers?
3. Which customers made only one order?
4. Which customers have above-average sales?
5. What is the highest order value per customer?

## How to Run

Create virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate