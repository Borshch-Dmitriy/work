from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Запускаем браузер
driver = webdriver.Chrome()

try:
    # 2. Открываем сайт
    driver.get('http://quotes.toscrape.com/')

    # Создаем объект ожидания (максимум 10 секунд)
    wait = WebDriverWait(driver, 10)

    # Проходим по циклу 2 страницы (1-я и 2-я)
    for page_num in range(1, 3):
        print(f"\n=== Сбор данных со страницы {page_num} ===")

        # 3. Ждем появления цитат на странице
        quotes = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.text'))
        )

        # 4. Выводим каждую цитату
        for i, quote in enumerate(quotes, 1):
            print(f"{i}. {quote.text}")

        # 5. Если это первая страница, находим кнопку "Next" и кликаем по ней
        if page_num == 1:
            print("\nПереходим на следующую страницу...")
            next_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a'))
            )
            next_button.click()

            # Короткая пауза для стабильности смены страницы
            time.sleep(1)

finally:
    # 6. Закрываем браузер
    print("\nРабота завершена, закрываем браузер.")
    driver.quit()