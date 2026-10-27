# ==========================================
# ШПАРГАЛКА ПО BEAUTIFULSOUP (BS4)
# ==========================================

# 1. ПОДКЛЮЧЕНИЕ И СОЗДАНИЕ ОБЪЕКТА SOUP

# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://example.com")
# response.encoding = "utf-8"
# soup = BeautifulSoup(response.text, "html.parser")  - стандартный парсер
# soup = BeautifulSoup(response.text, "lxml")        - быстрейший парсер (pip install lxml)

# 2. ОСНОВНЫЕ МЕТОДЫ ПОИСКА

# soup.find('tag')             - находит ПЕРВЫЙ тег (возвращает объект Tag или None)
# soup.find_all('tag')         - находит ВСЕ теги (возвращает список элементов / list)
# soup.find_all('tag', limit=N)- находит первые N элементов

# 3. ПОИСК ПО КЛАССАМ, ID И АТРИБУТАМ

# soup.find('div', class_='name')    - поиск по CSS-классу (обязательно с _)
# soup.find('div', id='main')        - поиск по ID элемента
# soup.find('div', {'data-id': '1'}) - поиск по произвольным атрибутам (через словарь)
# soup.find_all(['h1', 'h2', 'h3'])  - поиск по нескольким тегам одновременно

# 4. ПОИСК ЧЕРЕЗ CSS-СЕЛЕКТОРЫ

# soup.select_one('selector')  - находит один (первый) элемент по CSS-селектору
# soup.select('selector')      - находит список всех элементов по CSS-селектору

# ПРИМЕРЫ СЕЛЕКТОРОВ:

# soup.select('.class_name')   - по классу (начинается с точки)
# soup.select('#id_name')      - по ID (начинается с решетки)
# soup.select('div.card p')    - вложенность (p внутри div.card)
# soup.select('a[href]')       - теги a с атрибутом href
# soup.select('a[href^="http"]') - href начинается с "http"
# soup.select('img[src$=".png"]') - src заканчивается на ".png"

# 5. ИЗВЛЕЧЕНИЕ ДАННЫХ ИЗ ТЕГА

# tag = soup.find('a')
# tag.text                     - весь текст внутри тега (и всех его вложенных тегов)
# tag.get_text(strip=True)     - текст без лишних пробелов и переносов строк
# tag.string                   - текст тега (работает, только если внутри нет дочерних тегов)
# tag['href']                  - значение атрибута (вызовет KeyError, если атрибута нет)
# tag.get('href')              - безопасное извлечение атрибута (вернет None, если его нет)
# tag.attrs                    - словарь всех атрибутов тега {'class': [...], 'href': '...'}

# 6. НАВИГАЦИЯ ПО ДЕРЕВУ ЭЛЕМЕНТОВ

# tag.parent                   - прямой родительский тег
# tag.parents                  - все предки тега выше по дереву
# tag.children                 - итератор по дочерним элементам (детям)
# tag.contents                 - список всех дочерних элементов
# tag.find_next_sibling()      - следующий соседний тег на том же уровне
# tag.find_previous_sibling()  - предыдущий соседний тег на том же уровне

# 7. ПОИСК ПО ТЕКСТУ ВНУТРИ ТЕГА (С RE / REGEX)

# import re
# soup.find('button', string='Купить')                - точное совпадение текста
# soup.find(string=re.compile(r'руб'))                - содержит слово "руб"
# soup.find_all('a', string=re.compile(r'Подробнее'))   - все ссылки с таким текстом

# 8. МОДИФИКАЦИЯ И УДАЛЕНИЕ ЭЛЕМЕНТОВ

# tag.string = "Новый текст"   - изменить текст внутри тега
# tag['class'] = "new_class"   - изменить/добавить атрибут
# tag.decompose()              - полностью удалить тег и его содержимое из HTML

# ПРИМЕР ОЧИСТКИ ОТ РЕКЛАМЫ И СКРИПТОВ:

# for s in soup(['script', 'style', 'footer']):
#     s.decompose()

# ==========================================