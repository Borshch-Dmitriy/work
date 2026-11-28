class HtmlTag:
    _level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self._indent = 0

    def __enter__(self):
        self._indent = HtmlTag._level
        if not self.inline:
            print(f"{' ' * self._indent}<{self.tag}>")
            HtmlTag._level += 2
        return self

    def __exit__(self, ex_type, ex_value, ex_tr):
        if not self.inline:
            HtmlTag._level -= 2
            print(f"{' ' * self._indent}</{self.tag}>")
        return False

    def print(self, text):
        if self.inline:
            print(f"{' ' * self._indent}<{self.tag}>{text}</{self.tag}>")
        else:
            print(f"{' ' * HtmlTag._level}{text}")


with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
