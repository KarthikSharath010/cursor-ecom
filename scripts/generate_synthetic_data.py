import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def daterange(start_date: datetime, end_date: datetime) -> datetime:
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


customers = [
    ("CUST001", "Ava", "Hernandez", "ava.hernandez@example.com", "415-555-0134", "San Francisco", "CA", "2022-01-15"),
    ("CUST002", "Liam", "Chambers", "liam.chambers@example.com", "206-555-0199", "Seattle", "WA", "2021-11-02"),
    ("CUST003", "Noah", "Patel", "noah.patel@example.com", "312-555-0150", "Chicago", "IL", "2022-05-21"),
    ("CUST004", "Emma", "Jackson", "emma.jackson@example.com", "917-555-0174", "New York", "NY", "2023-02-10"),
    ("CUST005", "Olivia", "Wang", "olivia.wang@example.com", "512-555-0143", "Austin", "TX", "2023-04-18"),
    ("CUST006", "Isabella", "Lopez", "isabella.lopez@example.com", "213-555-0102", "Los Angeles", "CA", "2021-09-30"),
    ("CUST007", "Sophia", "Adams", "sophia.adams@example.com", "303-555-0162", "Denver", "CO", "2022-12-05"),
    ("CUST008", "Mason", "Bennett", "mason.bennett@example.com", "404-555-0177", "Atlanta", "GA", "2023-01-27"),
    ("CUST009", "Lucas", "Griffin", "lucas.griffin@example.com", "480-555-0116", "Phoenix", "AZ", "2022-08-14"),
    ("CUST010", "Mia", "Foster", "mia.foster@example.com", "702-555-0192", "Las Vegas", "NV", "2021-10-08"),
    ("CUST011", "Ethan", "Kumar", "ethan.kumar@example.com", "617-555-0183", "Boston", "MA", "2022-03-19"),
    ("CUST012", "Harper", "Reed", "harper.reed@example.com", "919-555-0126", "Raleigh", "NC", "2023-06-12"),
    ("CUST013", "Elijah", "Ferguson", "elijah.ferguson@example.com", "801-555-0176", "Salt Lake City", "UT", "2022-07-25"),
    ("CUST014", "Charlotte", "Diaz", "charlotte.diaz@example.com", "305-555-0155", "Miami", "FL", "2022-10-03"),
    ("CUST015", "Amelia", "Nguyen", "amelia.nguyen@example.com", "214-555-0180", "Dallas", "TX", "2023-03-07"),
    ("CUST016", "James", "Larson", "james.larson@example.com", "612-555-0189", "Minneapolis", "MN", "2021-12-29"),
    ("CUST017", "Benjamin", "Stone", "benjamin.stone@example.com", "615-555-0178", "Nashville", "TN", "2022-06-01"),
    ("CUST018", "Evelyn", "Garcia", "evelyn.garcia@example.com", "702-555-0132", "Henderson", "NV", "2023-05-03"),
    ("CUST019", "Henry", "Cole", "henry.cole@example.com", "925-555-0171", "Oakland", "CA", "2022-09-09"),
    ("CUST020", "Avery", "Simmons", "avery.simmons@example.com", "971-555-0153", "Portland", "OR", "2021-08-22"),
]

product_catalog = [
    ("PRO001", "Wireless Earbuds", "Electronics", 79.99, 120, "AUDIO-EB001"),
    ("PRO002", "Smart Fitness Watch", "Wearables", 149.00, 85, "WEAR-SW002"),
    ("PRO003", "4K Action Camera", "Electronics", 249.99, 60, "CAM-AC003"),
    ("PRO004", "Portable Projector", "Home Entertainment", 329.50, 40, "HOME-PP004"),
    ("PRO005", "Espresso Machine", "Appliances", 199.99, 35, "KITCH-EM005"),
    ("PRO006", "Air Fryer Pro", "Appliances", 129.95, 50, "KITCH-AF006"),
    ("PRO007", "Smart LED Light Kit", "Home Automation", 89.50, 140, "HOME-LG007"),
    ("PRO008", "Bluetooth Speaker", "Electronics", 59.99, 200, "AUDIO-BS008"),
    ("PRO009", "Ergonomic Office Chair", "Furniture", 299.00, 25, "FURN-OC009"),
    ("PRO010", "Standing Desk Converter", "Furniture", 179.50, 30, "FURN-SD010"),
    ("PRO011", "Noise Cancelling Headphones", "Electronics", 199.50, 75, "AUDIO-NC011"),
    ("PRO012", "Smart Home Hub", "Home Automation", 129.00, 90, "HOME-HH012"),
    ("PRO013", "Robot Vacuum", "Appliances", 349.99, 20, "HOME-RV013"),
    ("PRO014", "Gaming Keyboard", "Electronics", 99.99, 110, "GAME-GK014"),
    ("PRO015", "Mechanical Monitor Arm", "Accessories", 149.99, 55, "ACC-MA015"),
    ("PRO016", "USB-C Docking Station", "Accessories", 199.00, 70, "ACC-DS016"),
    ("PRO017", "Smartphone Gimbal", "Electronics", 119.99, 65, "PHOTO-SG017"),
    ("PRO018", "LED Desk Lamp", "Home & Office", 39.99, 180, "HOME-DL018"),
    ("PRO019", "Premium Yoga Mat", "Fitness", 69.99, 95, "FIT-YM019"),
    ("PRO020", "Insulated Water Bottle", "Outdoors", 34.95, 150, "OUTD-WB020"),
]


def write_csv(filename, headers, rows):
    with (DATA_DIR / filename).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


customer_rows = customers
write_csv(
    "customers.csv",
    ["customer_id", "first_name", "last_name", "email", "phone", "city", "state", "signup_date"],
    customer_rows,
)


product_rows = product_catalog
write_csv(
    "products.csv",
    ["product_id", "name", "category", "price", "stock_qty", "sku"],
    product_rows,
)


order_ids = [f"ORD{1000 + i}" for i in range(1, 31)]
statuses = ["processing", "fulfilled", "shipped", "delivered"]
addresses = [
    ("125 Market St", "San Francisco", "CA", "94105"),
    ("742 Evergreen Terrace", "Chicago", "IL", "60610"),
    ("89 5th Ave", "New York", "NY", "10011"),
    ("410 Peachtree Rd", "Atlanta", "GA", "30303"),
    ("222 Congress Ave", "Austin", "TX", "78701"),
    ("56 Sunset Blvd", "Los Angeles", "CA", "90028"),
    ("233 Fremont St", "Las Vegas", "NV", "89101"),
    ("840 Pine St", "Seattle", "WA", "98101"),
]

order_rows = []
order_item_rows = []
payment_rows = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 11, 1)

order_item_counter = 1
payment_counter = 1

payment_methods = ["credit_card", "paypal", "apple_pay", "google_pay"]

for oid in order_ids:
    customer = random.choice(customers)
    address = random.choice(addresses)
    order_date = daterange(start_date, end_date)
    status = random.choice(statuses)

    num_items = random.randint(1, 4)
    line_items = []
    for _ in range(num_items):
        product = random.choice(product_catalog)
        quantity = random.randint(1, 3)
        unit_price = product[3]
        line_total = round(quantity * unit_price, 2)
        line_items.append((product[0], quantity, unit_price, line_total))

    order_total = round(sum(item[3] for item in line_items), 2)
    order_rows.append(
        (
            oid,
            customer[0],
            order_date.strftime("%Y-%m-%d"),
            status,
            address[0],
            address[1],
            address[2],
            address[3],
            f"{order_total:.2f}",
        )
    )

    for product_id, quantity, unit_price, line_total in line_items:
        order_item_rows.append(
            (
                f"OITEM{order_item_counter:04d}",
                oid,
                product_id,
                quantity,
                f"{unit_price:.2f}",
                f"{line_total:.2f}",
            )
        )
        order_item_counter += 1

    payment_date = order_date + timedelta(days=random.randint(0, 5))
    payment_rows.append(
        (
            f"PAY{payment_counter:04d}",
            oid,
            payment_date.strftime("%Y-%m-%d"),
            f"{order_total:.2f}",
            random.choice(payment_methods),
            "completed" if status in {"shipped", "delivered", "fulfilled"} else "pending",
            f"TXN{random.randint(100000, 999999)}",
        )
    )
    payment_counter += 1


write_csv(
    "orders.csv",
    ["order_id", "customer_id", "order_date", "status", "shipping_address", "shipping_city", "shipping_state", "shipping_zip", "total_amount"],
    order_rows,
)

write_csv(
    "order_items.csv",
    ["order_item_id", "order_id", "product_id", "quantity", "unit_price", "line_total"],
    order_item_rows,
)

write_csv(
    "payments.csv",
    ["payment_id", "order_id", "payment_date", "amount", "payment_method", "status", "transaction_id"],
    payment_rows,
)


