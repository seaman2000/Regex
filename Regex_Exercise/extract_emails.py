import re

emails = input()

pattern = r"\s(([a-z\d]+)([\.\-\_][a-z\d]+)?@[a-z]+([.\-][a-z]+){1,})"

lists_of_emails = re.findall(pattern, emails)

for email in lists_of_emails:
    print(email[0])