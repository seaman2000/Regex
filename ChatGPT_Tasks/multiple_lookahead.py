import re

words = input()
pattern = r"\b(?=\w*[A-Za-z])(?=\w*\d)\w+\b"

result = re.findall(pattern, words)

print('\n'.join(result))