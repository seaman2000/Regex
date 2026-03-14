import re

bought_furniture = []
total_cost = 0.0

pattern = r">>\b([A-Za-z]+)<<(\d+(?:[\.]\d+)?)!(\d+)\b"

while True:

    purchase_information = input()

    if purchase_information == "Purchase":
        break
    result = re.search(pattern, purchase_information)

    if result:
        furniture, price, quantity = result.groups()
        total_cost += float(price) * int(quantity)
        bought_furniture.append(furniture)

print(f"Bought furniture:\n"
      f"{'\n'.join(bought_furniture)}")

print(f"Total money spend:\n"
      f"{total_cost:.2f}")
