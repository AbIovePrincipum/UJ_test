from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://todolist.james.am/#/")

wait = WebDriverWait(driver, 20)  # Adjust the timeout value as needed

try:
    task = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".new-todo")))
    task_names = []

    for i in range(1, 7):
        task_name = "zakupy"

        task.click()
        task.send_keys(task_name)
        task.send_keys(Keys.ENTER)

        task_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".todo-list li")))
        task_names = [task.text for task in task_list]

        if task_names.count(task_name) > 1:
            print(f"Task '{task_name}' already exists in the to-do list.")
        else:
            print(f"Task '{task_name}' added successfully to the to-do list.")
finally:
    driver.quit()
