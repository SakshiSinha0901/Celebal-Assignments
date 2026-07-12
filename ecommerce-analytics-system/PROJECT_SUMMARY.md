# Assignment Summary

The E-Commerce Order Analytics System is a local data analytics project that combines Python and SQL in one complete workflow. Four connected datasets are generated for customers, products, orders, and order items. The raw files contain a small number of deliberate errors to represent the type of issues commonly found in real business data.

Pandas is used to remove duplicates, handle missing values, correct data types, reject invalid values, and verify relationships between files. The cleaned data is then loaded into SQLite tables that use primary keys, foreign keys, required fields, and check constraints.

The SQL section focuses on business reporting. It calculates customer and category revenue, monthly sales, top products, average order value, customer lifetime value, running totals, moving averages, growth rates, cohort retention, churn status, and customer segments. A Python CLI makes these reports easy to run without opening the database manually.

The project can be executed completely from VS Code. No cloud platform is required because SQLite runs locally through Python.
