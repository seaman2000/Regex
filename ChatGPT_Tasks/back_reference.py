import re

text = input()

pattern = r'\b([A-Za-z]+) \1\b'

result_iteration = re.finditer(pattern, text)
result = re.findall(pattern, text)
group_num = 1

for match in re.finditer(pattern, text):
    for group_value in match.groups():
        print(f"Group {group_num}: {group_value}")
        group_num += 1

print(f"Words repeating are: {', '.join(result)}")