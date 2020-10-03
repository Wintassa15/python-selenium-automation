from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/wintana/JobEasy-QAAutomation/python-selenium-automation/chromedriver-2')
driver.maximize_window()
driver.implicitly_wait(5)
input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
input_field.send_keys('Dress')