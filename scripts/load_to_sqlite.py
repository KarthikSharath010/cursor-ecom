import csv
import sqlite3

DB_PATH = "database/ecom.db"
SCHEMA_PATH = "sql/schema.sql"
DATA_DIR = "data"

TABLE_CONFIG = [
    (
        "customers",
        "customers.csv",
        ["customer_id", "first_name", "last_name", "email", "phone", "city", "state", "signup_date"],
    ),
    (
        "products",
        "products.csv",
        ["product_id", "name", "category", "price", "stock_qty", "sku"],
    ),
    (
        "orders",
        "orders.csv",
        [
            "order_id",
            "customer_id",
            "order_date",
            "status",
            "shipping_address",
            "shipping_city",
            "shipping_state",
            "shipping_zip",
            "total_amount",
        ],
    ),
    (
        "order_items",
        "order_items.csv",
        ["order_item_id", "order_id", "product_id", "quantity", "unit_price", "line_total"],
    ),
    (
        "payments",
        "payments.csv",
        ["payment_id", "order_id", "payment_date", "amount", "payment_method", "status", "transaction_id"],
    ),
]


def drop_existing_tables(conn):
    conn.execute("PRAGMA foreign_keys = OFF;")
    for table in ["payments", "order_items", "orders", "products", "customers"]:
        conn.execute(f"DROP TABLE IF EXISTS {table}")
    conn.commit()


def apply_schema(conn):
    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        conn.executescript(schema_file.read())


def load_table(conn, table_name, filename, columns):
    file_path = f"{DATA_DIR}/{filename}"
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        placeholders = ",".join("?" for _ in columns)
        insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        rows = [tuple(row[col] for col in columns) for row in reader]
        if rows:
            conn.executemany(insert_sql, rows)


def main():
    with sqlite3.connect(DB_PATH) as conn:
        drop_existing_tables(conn)
        apply_schema(conn)
        conn.execute("PRAGMA foreign_keys = ON;")
        for table_name, filename, columns in TABLE_CONFIG:
            load_table(conn, table_name, filename, columns)
        conn.commit()


if __name__ == "__main__":
    main()

