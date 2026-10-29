# Явное ожидание
from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем инструменты для ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('http://quotes.toscrape.com/')

    # 1. Создаем объект ожидания: максимум 10 секунд
    wait = WebDriverWait(driver, 10)

    # 2. Ждем, пока элемент станет доступен на странице
    # EC.presence_of_element_located означает "ждать присутствия элемента в HTML"
    title_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h1 a'))
    )

    print("Текст заголовка (поймано через WebDriverWait):", title_element.text)

finally:
    driver.quit()