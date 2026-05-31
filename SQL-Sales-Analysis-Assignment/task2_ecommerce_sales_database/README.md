# Task 2: E-Commerce Sales Database

## Objective

The objective of this task is to write SQL queries on an e-commerce relational database to extract meaningful business insights.

## Business Context

ShopEase is a mid-sized e-commerce company that sells electronics, clothing, and home products across India. The management team wants to analyze sales patterns, customer behavior, and product performance.

## Database Tables

The database contains four tables:

1. customers
2. products
3. orders
4. order_items

## Relationships

- One customer can place many orders.
- One order can contain many order items.
- One product can appear in many order items.

## Files Included

| File | Description |
|---|---|
| `ecommerce_setup.sql` | Creates tables, indexes, constraints, and inserts sample data |
| `ecommerce_queries.sql` | Contains SQL solutions for Q1 to Q27 |
| `ecommerce_assignment.py` | Runs the setup file, executes queries, and saves outputs |
| `ecommerce.db` | SQLite database generated after running Python script |
| `outputs/query_results.md` | Query outputs in readable format |
| `outputs/*.csv` | Individual query result files |
| `outputs/q6_constraint_test.txt` | Error output for CHECK constraint test |

## Concepts Covered

1. SELECT queries
2. Primary Keys
3. Foreign Keys
4. Constraints
5. WHERE filtering
6. Indexes
7. GROUP BY aggregation
8. HAVING clause
9. INNER JOIN
10. LEFT JOIN
11. CASE statements
12. ACID properties
13. Transactions

## How to Run

Run this command from the task folder:

```bash
python ecommerce_assignment.py