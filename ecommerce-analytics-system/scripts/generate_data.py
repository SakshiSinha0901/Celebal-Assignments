"""Generate realistic raw e-commerce CSV datasets with intentional data issues."""
from __future__ import annotations

import argparse
import random
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
from faker import Faker

SEED = 42
fake = Faker("en_IN")
Faker.seed(SEED)
random.seed(SEED)

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

CATEGORIES = {
    "Electronics": ["Wireless Earbuds", "Smart Watch", "Power Bank", "Bluetooth Speaker", "Keyboard"],
    "Home & Kitchen": ["Mixer Grinder", "Water Bottle", "Storage Box", "Table Lamp", "Cookware Set"],
    "Fashion": ["T-Shirt", "Jeans", "Sneakers", "Backpack", "Jacket"],
    "Books": ["Programming Book", "Novel", "Business Book", "Biography", "Exam Guide"],
    "Beauty": ["Face Wash", "Moisturizer", "Shampoo", "Perfume", "Sunscreen"],
}
SEGMENTS = ["Consumer", "Corporate", "Student"]
PAYMENT_METHODS = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery", "Net Banking"]
ORDER_STATUS = ["Delivered", "Shipped", "Processing", "Cancelled", "Returned"]


def customer_rows(n: int) -> list[dict]:
    start = date(2023, 1, 1)
    rows = []
    for i in range(1, n + 1):
        signup = start + timedelta(days=random.randint(0, 1050))
        rows.append({
            "customer_id": f"C{i:04d}",
            "customer_name": fake.name(),
            "email": fake.unique.email(),
            "city": fake.city(),
            "state": fake.state(),
            "customer_segment": random.choices(SEGMENTS, weights=[55, 25, 20], k=1)[0],
            "signup_date": signup.isoformat(),
        })
    return rows


def product_rows(n: int) -> list[dict]:
    rows = []
    for i in range(1, n + 1):
        category = random.choice(list(CATEGORIES))
        base = random.choice(CATEGORIES[category])
        rows.append({
            "product_id": f"P{i:04d}",
            "product_name": f"{fake.company().split()[0]} {base}",
            "category": category,
            "unit_price": round(random.uniform(120, 30000), 2),
            "stock_quantity": random.randint(0, 500),
        })
    return rows


def order_rows(n: int, customers: list[dict]) -> list[dict]:
    today = date.today()
    start = date(2024, 1, 1)
    rows = []
    customer_ids = [x["customer_id"] for x in customers]
    for i in range(1, n + 1):
        order_date = start + timedelta(days=random.randint(0, max(1, (today - start).days)))
        status = random.choices(ORDER_STATUS, weights=[62, 12, 8, 12, 6], k=1)[0]
        rows.append({
            "order_id": f"O{i:05d}",
            "customer_id": random.choice(customer_ids),
            "order_date": order_date.isoformat(),
            "order_status": status,
            "payment_method": random.choice(PAYMENT_METHODS),
        })
    return rows


def order_item_rows(orders: list[dict], products: list[dict]) -> list[dict]:
    rows = []
    product_map = {x["product_id"]: x for x in products}
    item_no = 1
    for order in orders:
        for product_id in random.sample(list(product_map), k=random.randint(1, 5)):
            product = product_map[product_id]
            quantity = random.randint(1, 5)
            discount = random.choice([0, 0, 0, 0.05, 0.10, 0.15, 0.20])
            rows.append({
                "order_item_id": f"OI{item_no:06d}",
                "order_id": order["order_id"],
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": product["unit_price"],
                "discount": discount,
            })
            item_no += 1
    return rows


def introduce_issues(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame):
    """Create known nulls, duplicates, invalid values and broken references."""
    customers.loc[[4, 18, 31], "email"] = None
    customers.loc[[10, 22], "city"] = ""
    customers = pd.concat([customers, customers.iloc[[7, 15]]], ignore_index=True)

    products.loc[[2, 17], "category"] = None
    products.loc[9, "unit_price"] = -499.0
    products.loc[12, "stock_quantity"] = -5
    products = pd.concat([products, products.iloc[[5]]], ignore_index=True)

    orders.loc[[6, 24], "customer_id"] = ["C9999", "UNKNOWN"]
    orders.loc[14, "order_date"] = "2035-12-25"
    orders.loc[20, "order_date"] = "not-a-date"
    orders.loc[30, "payment_method"] = None
    orders = pd.concat([orders, orders.iloc[[11, 38]]], ignore_index=True)

    items.loc[[8, 43], "order_id"] = ["O99999", "BAD_ORDER"]
    items.loc[18, "product_id"] = "P9999"
    items.loc[25, "quantity"] = 0
    items.loc[28, "quantity"] = -2
    items.loc[35, "discount"] = 1.5
    items["unit_price"] = items["unit_price"].astype("object")
    items.loc[40, "unit_price"] = "invalid"
    items = pd.concat([items, items.iloc[[12, 50]]], ignore_index=True)
    return customers, products, orders, items


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate raw e-commerce datasets.")
    parser.add_argument("--customers", type=int, default=400)
    parser.add_argument("--products", type=int, default=120)
    parser.add_argument("--orders", type=int, default=1000)
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    customers = pd.DataFrame(customer_rows(args.customers))
    products = pd.DataFrame(product_rows(args.products))
    orders = pd.DataFrame(order_rows(args.orders, customers.to_dict("records")))
    items = pd.DataFrame(order_item_rows(orders.to_dict("records"), products.to_dict("records")))
    customers, products, orders, items = introduce_issues(customers, products, orders, items)

    datasets = {
        "customers.csv": customers,
        "products.csv": products,
        "orders.csv": orders,
        "order_items.csv": items,
    }
    for filename, frame in datasets.items():
        frame.to_csv(RAW_DIR / filename, index=False)
        print(f"Created {filename:<20} rows={len(frame):>5}")

    print("\nRaw datasets generated with intentional quality issues.")


if __name__ == "__main__":
    main()
