import re

text = input()

pattern = r'\b(?=[ab]*a[ab]*\b)[ab]{3}\b'

strings_including_a = re.findall(pattern, text)

print(', '.join(strings_including_a))