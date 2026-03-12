import re

text = input()

pattern = r"(?<=#)[a-z]+"

result = re.findall(pattern, text)

print('\n'.join(result))