# Data Quality Rules

This file explains the main data quality rules used in the TrustGuard pipeline.

## 1. Completeness Checks

Completeness checks are used to find missing values in important columns.

Important columns checked:

- `transaction_id`
- `customer_id`
- `product_category`
- `payment_method`
- `quantity`
- `unit_price`
- `total_amount`
- `transaction_date`

If `transaction_id` or `customer_id` is missing, the record is treated as invalid because these fields are required to identify the transaction and customer.

## 2. Duplicate Checks

The pipeline checks duplicate transaction IDs.

If the same `transaction_id` appears more than once, only the earliest record is kept. Duplicate records are removed from the clean dataset so that revenue is not counted multiple times.

## 3. Date Standardization

The raw data contains dates in different formats.

Examples:

```text
2024-03-15
15-03-2024
04/28/24
```

The pipeline converts these dates into a standard format wherever possible.

Final format:

```text
YYYY-MM-DD
```

## 4. Payment Method Standardization

Payment methods are written in different ways in the raw data.

Examples:

```text
UPI
upi
U.P.I.
Cash
CASH
card
```

The pipeline converts them into standard values:

```text
UPI
CASH
CARD
COD
NET_BANKING
UNKNOWN
```

## 5. City Name Correction

Some city names contain spelling mistakes.

Examples:

```text
Mumabi → Mumbai
Dhelhi → Delhi
Bangalor → Bangalore
Chennia → Chennai
Hydrabad → Hyderabad
```

This helps make city-wise reporting more accurate.

## 6. Type Casting

The raw CSV stores many values as text. The pipeline converts them into correct data types.

Examples:

```text
quantity → integer
unit_price → double
total_amount → double
transaction_date → date
```

## 7. Amount Validation

The pipeline checks whether:

```text
total_amount = quantity × unit_price
```

If the difference is too high, the record is marked as invalid.

## 8. Range Checks

The pipeline checks that numeric values are valid.

Rules:

- `quantity` should be greater than 0.
- `unit_price` should be greater than 0.
- `total_amount` should be greater than 0.

Records with invalid values are moved to rejected records.

## 9. Rejected Records

Rejected records are records that fail important checks.

Common rejection reasons:

- Missing transaction_id
- Missing customer_id
- Invalid quantity
- Non-positive quantity
- Invalid unit price
- Invalid transaction date
- Total amount mismatch

These records are stored separately instead of being deleted silently.

## 10. Data Quality Report

The DQ report shows how many records passed and failed each check.

It includes:

- Check name
- Total records
- Passed records
- Failed records
- Data quality score
- Run timestamp
