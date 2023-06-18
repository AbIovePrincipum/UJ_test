# Selenium Web Driver To-Do List Test

This repository contains a Python script that utilizes Selenium WebDriver to test the functionality of a to-do list web application. The script performs the following tasks:

- Adds tasks to the to-do list.
- Verifies if tasks are added successfully.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (for Chrome browser)

## Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies using pip:

   ```bash
   pip install selenium
   ```
   
3. Download the Chrome WebDriver executable that matches your Chrome browser version and place it in the same directory as the script. You can download it from the official ChromeDriver page: [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)

## Usage

1. Open the script file `selenium_test.py` in a text editor.
2. Modify the `zenek.get()` method's argument to specify the URL of the to-do list web application you want to test.
3. Save the file.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script using the following command:

   ```bash
   python selenium_test.py
   ```

6. The script will execute the test, adding tasks to the to-do list and verifying their successful addition. The test results will be displayed in the console.

## Customization

- Timeout: The script uses a default timeout of 20 seconds for waiting for elements to appear or become visible on the web page. You can modify this timeout value by changing the argument of the `WebDriverWait` constructor.
- Task Names: The script currently adds two tasks, `Task 1` and `Task 2`. You can modify the task names by updating the `task_name` variable in the script.
- CSS Selectors: The script uses CSS selectors to locate elements on the web page. If the CSS selectors provided in the script do not match the structure of the web page you are testing, you may need to modify them to correctly locate the required elements.
