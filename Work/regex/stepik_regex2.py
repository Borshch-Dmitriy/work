import re
new_text = input()

def change_text(text):
    pattern = r'\b(?P<first>\w)(?P<second>\w)(\w*)'
    res = re.sub(pattern, r'\g<second>\g<first>\3', text, flags=re.IGNORECASE)
    return res
print(change_text(new_text))