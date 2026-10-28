import re

in_text = input()


def result(text):
  pattern = r'(\d+)\(([a-zA-Z]*)\)'

  def replacer(match):
    num = int(match.group(1))
    s = match.group(2)
    return s * num

  while '(' in text:
    text = re.sub(pattern, replacer, text)
  return text


print(result(in_text))