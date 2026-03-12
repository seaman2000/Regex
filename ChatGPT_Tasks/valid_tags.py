import re

tags = input()

pattern = r'(?<=<)[a-z]{3,}(?=>)'

valid_tags = re.findall(pattern, tags)

print('\n'.join(valid_tags))