import re

sentence = input()

pattern = r'[A-Z][a-z]*'

result = re.findall(pattern, sentence)

print('\n'.join(result))