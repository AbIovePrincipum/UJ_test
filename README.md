# Selenium Web Driver To-Do List Test

This Python script demonstrates the use of Selenium WebDriver to interact with a to-do list web application. It adds tasks to the to-do list and performs a check to determine if a task can be added multiple times.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (for Chrome browser)

## Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies using pip:
   pip install selenium
3. Download the Chrome WebDriver executable that matches your Chrome browser version and place it in the same directory as the script. You can download it from the official ChromeDriver page: [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)

## Usage

1. Open the script file `TestCase12.py` in a text editor.
2. Modify the `driver.get()` method's argument to specify the URL of the to-do list web application you want to test.
3. Customise the file if needed
4. Save the file.
5. Open a terminal or command prompt and navigate to the directory containing the script.
6. Run the script using the following command:

   python selenium_test.py

7. The script will execute the test, adding tasks to the to-do list and checking if they can be added multiple times. The corresponding messages will be printed in the terminal.

## Customization

- Timeout: The script uses a default timeout of 20 seconds for waiting for elements to appear or become visible on the web page. You can modify this timeout value by changing the argument of the `WebDriverWait` constructor.

- Task Name: The script currently adds tasks with the name "zakupy". If you want to test with a different task name, modify the `task_name` variable in the script accordingly.

- CSS Selectors: The script uses CSS selectors to locate elements on the web page. If the CSS selectors provided in the script do not match the structure of the web page you are testing, you may need to modify them to correctly locate the required elements.
