import re
html_input = input()

title_pattern = r"<title>(.*?)</title>"
content_pattern = r"<body>(.*?)</body>"
text_pattern = r"<[^>]+>|\\n"

title = ''.join(re.findall(title_pattern, html_input))
content = re.search(content_pattern, html_input).group(1)
text = re.sub(text_pattern, '', content)

print(f"Title: {title}\n"
      f"Content: {text}")

