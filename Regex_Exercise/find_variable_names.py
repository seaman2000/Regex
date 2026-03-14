import re

text = input()

pattern = r'\b_([A-Za-z\d]+)\b'

found_names = re.findall(pattern, text)

print(','.join(found_names))