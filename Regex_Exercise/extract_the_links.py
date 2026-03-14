import re


pattern = r"(w{3}\.[a-z\d\-]+(\.[a-z]+)+)"
text_with_links = input()

while text_with_links:
    found_links = re.search(pattern, text_with_links, re.IGNORECASE)

    if found_links:
        link = found_links.group(1)
        print(link)

    text_with_links = input()
