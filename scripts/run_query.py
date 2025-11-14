import sqlite3
from pathlib import Path

DB_PATH = Path("database/ecom.db")
QUERY_PATH = Path("sql/join_query.sql")


def read_query() -> str:
    with QUERY_PATH.open("r", encoding="utf-8") as query_file:
        return query_file.read()


def format_table(headers, rows):
    str_rows = [[str(value) for value in row] for row in rows]
    widths = [len(header) for header in headers]
    for row in str_rows:
        for idx, value in enumerate(row):
            widths[idx] = max(widths[idx], len(value))

    def format_row(values):
        return " | ".join(value.ljust(widths[idx]) for idx, value in enumerate(values))

    separator = "-+-".join("-" * width for width in widths)
    lines = [
        format_row(headers),
        separator,
    ]
    lines.extend(format_row(row) for row in str_rows)
    return "\n".join(lines)


def main():
    query = read_query()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(query)
        headers = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
    table = format_table(headers, rows)
    print(table)


if __name__ == "__main__":
    main()

