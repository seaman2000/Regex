import re

dates = input()

pattern = r"(\d{2})([.\-\/])([A-Z][a-z]{2})+\b\2(\d{4})"

correct_dates = re.finditer(pattern, dates)

for date in correct_dates:
    day = date.group(1)
    month = date.group(3)
    year = date.group(4)

    print(f"Day: {day}, Month: {month}, Year: {year}")
