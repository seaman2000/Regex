import re

sentence = input()

pattern = r'[a-z][a-z\d._]*@[a-z]+\.[a-z]{2,}'

result = re.findall(pattern, sentence)

print('\n'.join(result))
