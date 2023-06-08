from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_task_addition():
    zenek = webdriver.Chrome()
    zenek.get("https://todolist.james.am/#/")

    wait = WebDriverWait(zenek, 20)  # Adjust the timeout value as needed

    try:
        zadanie = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".new-todo")))
        
        # Add the first task
        task_name = "Task 1"
        zadanie.click()
        zadanie.send_keys(task_name)
        zadanie.send_keys(Keys.ENTER)

        # Verify if the task is added successfully
        task_added = wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[text()='{task_name}']")))
        assert task_added.is_displayed(), f"Failed to add task: {task_name}"
        print(f"Task '{task_name}' added successfully.")

        # Add the second task
        task_name = "Task 2"
        zadanie.click()
        zadanie.send_keys(task_name)
        zadanie.send_keys(Keys.ENTER)

        # Verify if the second task is added successfully
        task_added = wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[text()='{task_name}']")))
        assert task_added.is_displayed(), f"Failed to add task: {task_name}"
        print(f"Task '{task_name}' added successfully.")

    finally:
        zenek.quit()

# Run the test
test_task_addition()
