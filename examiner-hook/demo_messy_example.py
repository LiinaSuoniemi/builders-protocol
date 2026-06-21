"""
A deliberately messy function, for demonstrating the EXAMINER hook.
Generic on purpose: no real project code. Safe to screenshot.
"""


def process_order(order, user, coupon, inventory):
    total = 0
    for item in order:
        if item["in_stock"]:
            if item["type"] == "book":
                total += item["price"] * 0.9
            elif item["type"] == "food":
                if item["perishable"]:
                    total += item["price"] * 0.8
                else:
                    total += item["price"]
            else:
                total += item["price"]
            if user["member"]:
                total -= 1
        else:
            continue
    if coupon:
        try:
            total = total - coupon["amount"]
        except Exception:
            total = total
    if total < 0:
        total = 0
    return total
