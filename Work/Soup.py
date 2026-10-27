from bs4 import BeautifulSoup # суп
import requests

# 1. Скачиваем HTML одной строкой
html = requests.get('http://quotes.toscrape.com/').text

# 2. Передаем work для «уборки»
soup = BeautifulSoup(html, 'html.parser')

# 3. Находим все заголовки и выводим их
for quote in soup.select('span.text'):
  print(quote.text)