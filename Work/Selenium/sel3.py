#Кликаем по кнопке «Следующая страница»
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Запускаем браузер
driver = webdriver.Chrome()

try:
    # 2. Открываем главную страницу
    driver.get('http://quotes.toscrape.com/')
    time.sleep(1)

    print("Начальный URL:", driver.current_url)

    # 3. Находим кнопку "Next" (следующая страница) с помощью CSS-селектора
    next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')

    # 4. Программно кликаем по ней
    next_button.click()

    # Ждем пару секунд, чтобы страница загрузилась
    time.sleep(2)

    # 5. Проверяем, куда мы попали
    print("URL после клика:", driver.current_url)

finally:
    # 6. Закрываем браузер
    driver.quit()