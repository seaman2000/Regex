import re
text = input()
searched_word = input()

pattern = fr'{searched_word}'

result = re.findall(pattern, text, re.IGNORECASE)

print(len(result))