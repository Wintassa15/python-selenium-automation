from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/python-selenium-automation/chromedriver-2")

# amazon_logo = driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
#create_account = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
#your_name= driver.find_element(By.ID, 'ap_customer_name')
#email = driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
#password = driver.find_element(By.ID, 'ap_password')
#password_characters= driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini')
#reenter_password = driver.find_element(By.ID, 'ap_password_check')
#create_amazon_account = driver.find_element(By.CSS_SELECTOR, 'input#continue')
#sign_in= driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')
