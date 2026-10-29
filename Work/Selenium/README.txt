# ==========================================
# ШПАРГАЛКА ПО SELENIUM (PYTHON)
# ==========================================

# 1. ИМПОРТ И ИНИЦИАЛИЗАЦИЯ
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()  # или webdriver.Firefox(), webdriver.Edge()
# driver.get("https://example.com")

# 2. ПОИСК ЭЛЕМЕНТОВ (Класс By)
# driver.find_element(By.ID, "id")                  - поиск по ID атрибуту
# driver.find_element(By.NAME, "name")              - поиск по атрибуту name
# driver.find_element(By.CLASS_NAME, "class")       - поиск по имени класса CSS
# driver.find_element(By.TAG_NAME, "tag")           - поиск по тегу (например, "div", "a")
# driver.find_element(By.CSS_SELECTOR, "css")       - поиск по CSS-селектору
# driver.find_element(By.XPATH, "xpath")            - поиск по XPath выражению
# driver.find_element(By.LINK_TEXT, "text")         - поиск ссылки по точному тексту
# driver.find_element(By.PARTIAL_LINK_TEXT, "text") - поиск ссылки по частичному тексту
# * Замена find_element на find_elements возвращает список (list) всех найденных элементов.

# 3. ВЗАИМОДЕЙСТВИЕ С ЭЛЕМЕНТАМИ
# element.click()            - клик по элементу
# element.send_keys("text")  - ввод текста (или отправка клавиш, например Keys.ENTER)
# element.clear()            - очистка текстового поля
# element.submit()           - отправка формы (для элементов внутри форм)
# element.text               - получение видимого текста элемента
# element.get_attribute("a") - получение значения атрибута (например, "href", "value")
# element.is_displayed()     - проверка, виден ли элемент на странице (True/False)
# element.is_enabled()       - проверка, активен/доступен ли элемент
# element.is_selected()      - проверка, выбран ли чекбокс или радиокнопка

# 4. ОЖИДАНИЯ (WAITS)
# Неявное ожидание (глобально для всего драйвера):
# driver.implicitly_wait(10)  # ожидать до 10 секунд перед ошибкой

# Явное ожидание (рекомендуемый подход):
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, "id")))
# Популярные условия (Expected Conditions - EC):
# - EC.presence_of_element_located(locator)      - элемент появился в DOM
# - EC.visibility_of_element_located(locator)    - элемент стал видимым
# - EC.element_to_clickable(locator)             - элемент виден и доступен для клика
# - EC.text_to_be_present_in_element(loc, text)  - текст появился внутри элемента
# - EC.alert_is_present()                        - появилось всплывающее окно (alert)

# 5. РАБОТА С ОКНАМИ, ВКЛАДКАМИ И ФРЕЙМАМИ
# driver.switch_to.frame("frame_name")         - переключение во фрейм / iframe
# driver.switch_to.default_content()           - возврат из фрейма в основной документ
# driver.switch_to.alert                       - переключение на системное окно (alert/confirm/prompt)
# alert = driver.switch_to.alert; alert.accept()  - подтвердить alert / alert.dismiss() - отклонить
# driver.switch_to.window(driver.window_handles[1]) - переключение на другую вкладку по индексу
# driver.current_window_handle                 - получить дескриптор текущего окна
# driver.window_handles                        - список всех открытых дескрипторов окон/вкладок

# 6. РАСШИРЕННЫЕ ДЕЙСТВИЯ (ActionChains)
# from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()   # наведение курсора мыши на элемент
# actions.context_click(element).perform()     # клик правой кнопкой мыши
# actions.double_click(element).perform()      # двойной клик по элементу
# actions.drag_and_drop(src, target).perform() # перетаскивание элемента (drag-and-drop)

# 7. ПОЛЕЗНЫЕ МЕТОДЫ ДРАЙВЕРА И УПРАВЛЕНИЕ БРАУЗЕРОМ
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") - выполнить JS код
# driver.save_screenshot("screen.png")         - сделать скриншот всей страницы
# element.screenshot("element.png")            - сделать скриншот конкретного элемента
# driver.back() / driver.forward()             - на шаг назад / вперед по истории браузера
# driver.refresh()                             - обновить текущую страницу
# driver.current_url                           - получить URL текущей страницы
# driver.title                                 - получить заголовок (title) страницы
# driver.close()                               - закрыть текущую вкладку
# driver.quit()                                - закрыть браузер и полностью завершить сессию
# ==========================================