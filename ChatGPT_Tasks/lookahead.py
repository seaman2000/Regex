import re

text = input()

pattern = r"\d+(?=%)"

percents = re.findall(pattern, text)

print('\n'.join(percents))