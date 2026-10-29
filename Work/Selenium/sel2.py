#Находим элемент и читаем текст
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Запускаем браузер
driver = webdriver.Chrome()

try:
    # 2. Открываем сайт
    driver.get('http://quotes.toscrape.com/')

    # Небольшая пауза, чтобы страница успела отрисоваться
    time.sleep(1)

    # 3. Ищем элемент на странице (используем CSS-селектор для тега h1 и ссылки внутри него)
    title_element = driver.find_element(By.CSS_SELECTOR, 'h1 a')

    # 4. Достаем текст с помощью свойства .text
    print("Текст заголовка:", title_element.text)

finally:
    # 5. Закрываем браузер
    driver.quit()