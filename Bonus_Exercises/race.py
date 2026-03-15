import re

pattern_for_name = r"[A-Za-z]"
pattern_for_numbers = r"\d"

participants = input().split(', ')
line = input()
results = {}

while line != "end of race":
    found_name = re.findall(pattern_for_name, line)
    found_name = ''.join(found_name)

    if found_name in participants:
        distance = re.findall(pattern_for_numbers, line)
        if distance:
            distance = sum([int(meters) for meters in distance])
            results[found_name] = results.get(found_name, 0) + distance

    line = input()

sorted_names = sorted(results, key=lambda name: results[name], reverse=True)

print(f"1st place: {sorted_names[0]}")
print(f"2nd place: {sorted_names[1]}")
print(f"3rd place: {sorted_names[2]}")


