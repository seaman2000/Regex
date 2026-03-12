import re

text = input()

pattern = r''

result = re.findall(pattern, text)

print("\n".join(result))