import re

tags = input()

pattern = r''

valid_tags = re.findall(pattern, tags)

print('\n'.join(valid_tags))