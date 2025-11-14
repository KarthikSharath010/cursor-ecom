# Cursor E-commerce Data Demo

Synthetic e-commerce dataset plus tooling to materialize it into SQLite for quick demos, analytics exercises, or onboarding tasks.

## What It Does
- Generates realistic CSVs for customers, products, orders, order items, and payments under `data/`.
- Defines a normalized schema with foreign keys and helpful indexes via `sql/schema.sql`.
- Loads the CSVs into `database/ecom.db` and exposes reusable SQL queries and a join report.

## Folder Structure
- `data/` – Generated CSV files.
- `database/` – SQLite database output (`ecom.db`).
- `scripts/`
  - `generate_synthetic_data.py` – Builds the CSV datasets.
  - `load_to_sqlite.py` – Creates the database and imports CSVs.
  - `run_query.py` – Executes the join query and prints a formatted table.
- `sql/`
  - `schema.sql` – Table definitions, foreign keys, and indexes.
  - `join_query.sql` – Multi-table join for customer/order insights.
  - `bonus_queries.sql` – Extra analytics (top customers, popular products, revenue per day).
  - `er_diagram.dot` – Graphviz ER diagram description.

## Load the Database
1. Ensure you have Python 3.x installed.
2. From the repo root:
   ```bash
   python scripts/generate_synthetic_data.py
   python scripts/load_to_sqlite.py
   ```
   The first command refreshes the CSVs; the second recreates `database/ecom.db` and loads all rows.

## Run the Join Query
- Preferred: `python scripts/run_query.py`
  - Reads `sql/join_query.sql`, runs it against `database/ecom.db`, and prints an aligned table with customer name, order info, totals, and payment method.
- Alternatively: `sqlite3 database/ecom.db < sql/join_query.sql`

## Extra Features
- **Indexes**: `sql/schema.sql` enables foreign keys and adds targeted indexes on email, customer_id, order_id, product_id to keep lookups fast.
- **Bonus Queries**: `sql/bonus_queries.sql` includes top spenders, most popular products, and last-30-day revenue reports.
- **ER Diagram**: Render `sql/er_diagram.dot` with Graphviz (`dot -Tpng sql/er_diagram.dot -o er_diagram.png`) to visualize table relationships.
