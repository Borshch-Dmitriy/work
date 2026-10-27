import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://quotes.toscrape.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    all_quotes = []
    for quote in quotes:
        result = {}
        author = quote.find('small', class_='author').text
        text = quote.select_one('span.text').text
        tags = quote.select('a.tag')
        tags_list = []
        result['quote'] = text
        result['author'] = author

        for tag in tags:
            tags_list.append(tag.text)
        result['tags'] = tags_list
        all_quotes.append(result)
        with open('../sqlite3/test.json', 'w', encoding='utf-8') as outfile:

            json.dump(all_quotes, outfile, indent=4, ensure_ascii=False)
        print(f'result: {result}')
else:
  print('НЕТ ДОСТУПА К СТРАНИЦЕ')