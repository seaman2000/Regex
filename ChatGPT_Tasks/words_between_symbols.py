import re

text = input()

pattern = r"(?<=@)[A-za-z]+(?=\!)"

result = re.findall(pattern, text)

print('\n'.join(result))