import re

text = input()

pattern = r'(?<=\$)\d+(?=\$)'

result = re.findall(pattern, text)

print('\n'.join(result))