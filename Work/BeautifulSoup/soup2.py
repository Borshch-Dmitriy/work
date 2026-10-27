from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('http://quotes.toscrape.com/login')

    # Явное ожидание: ждем, пока поле ввода username станет доступным (максимум 10 секунд)
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input#username'))
    )

    # Вводим текст в  
    username_input.send_keys('my_super_login')

    # Находим поле пароля и тоже вводим текст
    password_input = driver.find_element(By.CSS_SELECTOR, 'input#password')
    password_input.send_keys('secret_password')

    # Находим кнопку входа и кликаем по ней
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()

    # Ждем пару секунд после клика, чтобы увидеть результат
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/logout"]')))
    print("Успешно залогинились через Selenium!")

finally:
    driver.quit()