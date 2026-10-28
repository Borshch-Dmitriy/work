import re
import sys


def remove_comments():
    code = sys.stdin.read()

    # 1. Удаляем многострочные комментарии ("""...""" или '''...''') с флагом re.DOTALL,
    # чтобы точка захватывала переводы строк внутри кавычек.
    code = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\')', "", code, flags=re.DOTALL)

    # 2. Удаляем хвостовые комментарии (минимум 2 пробела перед # до конца строки)[cite: 5]
    code = re.sub(r" {2,}#.*", "", code)

    # 3. Удаляем однострочные комментарии (начинающиеся с # с начала строки)[cite: 5]
    code = re.sub(r"^[ \t]*#.*", "", code, flags=re.MULTILINE)

    # 4. Финальная очистка: убираем пробелы на концах строк и пустые строки[cite: 5]
    final_lines = []
    for line in code.splitlines():
        stripped_line = line.rstrip()
        if stripped_line:
            final_lines.append(stripped_line)

    print("\n".join(final_lines))


if __name__ == "__main__":
    remove_comments()