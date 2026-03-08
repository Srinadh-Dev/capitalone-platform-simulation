transactions = [
    {"amount": 100.50, "month": "January"},
    {"amount": 200.75, "month": "January"},
    {"amount": 300.00, "month": "January"},
    {"amount": 400.00, "month": "January"},
    {"amount": 728.47, "month": "January"}
]

def calculate_month_total(month):
    total = 0
    count = 0

    for txn in transactions:
        if txn["month"] == month:
            total =+ txn["amount"]
            count += 1

    return total, count


def generate_report():

    jan_total, jan_count = calculate_month_total("January")
    feb_total, feb_count = calculate_month_total("February")

    q1_total = jan_total + feb_total
    q1_count = jan_count + feb_count

    print(f"January Total:  ${jan_total:.2f} ({jan_count} txns)")
    print(f"February Total: ${feb_total:.2f} ({feb_count} txns)")
    print(f"Q1 Total:       ${q1_total:.2f} ({q1_count} txns)")


generate_report()