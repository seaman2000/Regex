import re

usernames = input()

pattern = r'(?<=@)\w+'

valid_usernames = re.findall(pattern, usernames)

print('\n'.join(valid_usernames))