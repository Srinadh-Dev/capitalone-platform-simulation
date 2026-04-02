transactions = [
    {"date": "2026-01-05", "amount": 200},
    {"date": "2026-01-10", "amount": 150},
    {"date": "2026-01-15", "amount": 300},
    {"date": "2026-01-20", "amount": 100},
    {"date": "2026-01-25", "amount": 250},
    {"date": "2026-01-28", "amount": 50},
    {"date": "2026-02-02", "amount": 180},
    {"date": "2026-02-10", "amount": 220},
    {"date": "2026-02-15", "amount": 130},
    {"date": "2026-02-20", "amount": 149.72},
]

def calculate_total(transactions):
    total = 0
    for txn in transactions:
        total += txn["amount"]
    return total

def filter_by_month(transactions, month):
    return [t for t in transactions if t["date"].startswith(month)]

def generate_report():
    jan = filter_by_month(transactions, "2026-01")
    feb = filter_by_month(transactions, "2026-02")

    jan_total = calculate_total(jan)
    feb_total = calculate_total(feb)
    q1_total = calculate_total(transactions)

    print(f"January Total:  ${jan_total} ({len(jan)} txns)")
    print(f"February Total: ${feb_total} ({len(feb)} txns)")
    print(f"Q1 Total:       ${q1_total} ({len(transactions)} txns)")

if __name__ == "__main__":
    generate_report()