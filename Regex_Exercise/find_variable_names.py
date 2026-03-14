import re

text = input()

pattern = r''

found_names = re.findall(pattern, text)

print(','.join(found_names))