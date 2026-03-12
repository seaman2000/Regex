import re

sentence = input()

pattern = r"\d+"

result = re.findall(pattern, sentence)

for num in result:
    print(num)