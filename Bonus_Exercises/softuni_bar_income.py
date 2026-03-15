import re

line = input()
total_income = 0.0
pattern = r"%([A-Z][a-z]+)%<(\w+)>(?:\w+)?\|(\d+)\|(?:[a-zA-Z]+)?(\d+(?:\.\d+)?)\$"

while line != "end of shift":
    result = re.search(pattern, line)
    if result:
        name = result.group(1)
        item = result.group(2)
        quantity = result.group(3)
        price = result.group(4)
        total_price = float(price) * int(quantity)
        total_income += total_price

        print(f"{name}: {item} - {total_price:.2f}")

    line = input()

print(f"Total income: {total_income:.2f}")