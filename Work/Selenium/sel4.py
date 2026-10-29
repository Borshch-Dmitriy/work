# Заполняем форму входа
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Запускаем браузер
driver = webdriver.Chrome()

try:
    # 2. Открываем страницу входа
    driver.get('http://quotes.toscrape.com/login')
    time.sleep(1)

    # 3. Находим поле логина и вводим в него текст
    # Селектор 'input#username' означает: тег input с id="username"
    username_input = driver.find_element(By.CSS_SELECTOR, 'input#username')
    username_input.send_keys('мой_логин_123')

    # 4. Находим поле пароля и тоже вводим текст
    password_input = driver.find_element(By.CSS_SELECTOR, 'input#password')
    password_input.send_keys('секретный_пароль')

    # 5. Находим кнопку отправки формы (кнопку Login) и кликаем по ней
    # Селектор 'input[type="submit"]' ищет тег input, у которого атрибут type равен submit
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()

    # Ждем пару секунд, чтобы увидеть результат
    time.sleep(2)
    print("Форма отправлена! Текущий адрес:", driver.current_url)

finally:
    # 6. Закрываем браузер
    driver.quit()