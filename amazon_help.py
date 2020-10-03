from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "/Users/wintana/JobEasy-QAAutomation/python-selenium-automation/chromedriver-2")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.amazon.com/gp/help/customer/display.html')

input_field = driver.find_element(By.ID, 'helpsearch')
input_field.clear()
input_field.send_keys('cancel orders', Keys.ENTER)
sleep(4)
result = driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]")
assert result.text == 'Cancel Items or Orders', f'expected result cancel orders but got {result.text} '
driver.quit()

