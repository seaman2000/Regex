import re

text = input()

pattern = r'\b\d+(?:\.\d{2}+)?\b'

result = re.findall(pattern, text)

print("\n".join(result))