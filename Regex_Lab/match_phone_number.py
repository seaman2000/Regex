import re

phone_numbers = input()

pattern = r'\+359 \d{1} \d{3} \d{4}|\+359-\d{1}-\d{3}-\d{4}'

result = re.findall(pattern, phone_numbers)

print(', '.join(result))
