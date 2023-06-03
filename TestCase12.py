from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

zenek = webdriver.Chrome()
zenek.get("https://todolist.james.am/#/")

wait = WebDriverWait(zenek, 20)  # Adjust the timeout value as needed

try:
    zadanie = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".new-todo")))
    for i in range(1, 7):
        zadanie.click()
        zadanie.send_keys("zakupy")
        zadanie.send_keys(Keys.ENTER)
finally:
    zenek.quit()
