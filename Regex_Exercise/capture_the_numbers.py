import re

text = input()
list_of_numbers = []
pattern = r'\d+'

while text:
    result = re.findall(pattern, text)
    if result:
        list_of_numbers += result
    text = input()

print(' '.join(list_of_numbers))