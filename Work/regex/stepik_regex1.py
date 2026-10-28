import keyword
import re
text_new = input()
def change_text(text):
    pattern = r'\b(' + '|'.join(keyword.kwlist) + r')\b'
    return re.sub(pattern, '<kw>', text,flags=re.I)


print(change_text(text_new))

