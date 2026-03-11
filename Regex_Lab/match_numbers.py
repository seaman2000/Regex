import re

numbers = input()

pattern = r"(?:^|(?<=\s))-?(?:0|[1-9][0-9]*)(?:\.\d+)?(?=$|\s)"

result = re.findall(pattern, numbers)

print(' '.join(result))
