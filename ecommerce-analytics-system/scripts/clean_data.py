"""Clean raw e-commerce CSV files and enforce cross-table consistency."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
CLEAN_DIR = ROOT / "data" / "cleaned"
OUTPUT_DIR = ROOT / "output" / "sample_reports"


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (
        pd.read_csv(RAW_DIR / "customers.csv"),
        pd.read_csv(RAW_DIR / "products.csv"),
        pd.read_csv(RAW_DIR / "orders.csv"),
        pd.read_csv(RAW_DIR / "order_items.csv"),
    )


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().drop_duplicates(subset="customer_id", keep="first")
    text_cols = ["customer_name", "email", "city", "state", "customer_segment"]
    for col in text_cols:
        df[col] = df[col].astype("string").str.strip()
    df["email"] = df["email"].fillna("unknown@example.com")
    df["city"] = df["city"].replace("", pd.NA).fillna("Unknown")
    df["state"] = df["state"].fillna("Unknown")
    df["customer_segment"] = df["customer_segment"].fillna("Consumer")
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    df = df.dropna(subset=["customer_id", "customer_name", "signup_date"])
    df["signup_date"] = df["signup_date"].dt.strftime("%Y-%m-%d")
    return df.sort_values("customer_id").reset_index(drop=True)


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().drop_duplicates(subset="product_id", keep="first")
    df["product_name"] = df["product_name"].astype("string").str.strip()
    df["category"] = df["category"].astype("string").str.strip().fillna("Uncategorized")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["stock_quantity"] = pd.to_numeric(df["stock_quantity"], errors="coerce")
    df = df.dropna(subset=["product_id", "product_name", "unit_price", "stock_quantity"])
    df = df[(df["unit_price"] > 0) & (df["stock_quantity"] >= 0)]
    df["stock_quantity"] = df["stock_quantity"].astype(int)
    df["unit_price"] = df["unit_price"].round(2)
    return df.sort_values("product_id").reset_index(drop=True)


def clean_orders(df: pd.DataFrame, valid_customer_ids: set[str]) -> pd.DataFrame:
    df = df.copy().drop_duplicates(subset="order_id", keep="first")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["payment_method"] = df["payment_method"].astype("string").str.strip().fillna("Unknown")
    df["order_status"] = df["order_status"].astype("string").str.strip().fillna("Processing")
    today = pd.Timestamp.today().normalize()
    df = df.dropna(subset=["order_id", "customer_id", "order_date"])
    df = df[df["customer_id"].isin(valid_customer_ids)]
    df = df[df["order_date"] <= today]
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
    return df.sort_values("order_id").reset_index(drop=True)


def clean_order_items(df: pd.DataFrame, valid_order_ids: set[str], valid_product_ids: set[str]) -> pd.DataFrame:
    df = df.copy().drop_duplicates(subset="order_item_id", keep="first")
    for col in ["quantity", "unit_price", "discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["order_item_id", "order_id", "product_id", "quantity", "unit_price", "discount"])
    df = df[df["order_id"].isin(valid_order_ids)]
    df = df[df["product_id"].isin(valid_product_ids)]
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]
    df = df[df["discount"].between(0, 0.80)]
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].round(2)
    df["discount"] = df["discount"].round(2)
    return df.sort_values("order_item_id").reset_index(drop=True)


def main() -> None:
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_customers, raw_products, raw_orders, raw_items = load_data()

    customers = clean_customers(raw_customers)
    products = clean_products(raw_products)
    orders = clean_orders(raw_orders, set(customers["customer_id"]))
    items = clean_order_items(raw_items, set(orders["order_id"]), set(products["product_id"]))

    outputs = {
        "customers_clean.csv": customers,
        "products_clean.csv": products,
        "orders_clean.csv": orders,
        "order_items_clean.csv": items,
    }
    for filename, frame in outputs.items():
        frame.to_csv(CLEAN_DIR / filename, index=False)

    summary = pd.DataFrame([
        ["customers", len(raw_customers), len(customers), len(raw_customers) - len(customers)],
        ["products", len(raw_products), len(products), len(raw_products) - len(products)],
        ["orders", len(raw_orders), len(orders), len(raw_orders) - len(orders)],
        ["order_items", len(raw_items), len(items), len(raw_items) - len(items)],
    ], columns=["dataset", "raw_rows", "clean_rows", "removed_rows"])
    summary.to_csv(OUTPUT_DIR / "data_cleaning_summary.csv", index=False)
    print(summary.to_string(index=False))
    print("\nClean datasets exported successfully.")


if __name__ == "__main__":
    main()
