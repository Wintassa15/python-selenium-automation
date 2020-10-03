"""
amazon_logo=driver.find element(By.xpath, "//h1[@class= 'a-spacing-small']")
or amazon_logo= driver.find element(By.xpath,"//h1[contains(@class, 'spacing-small')]")

email_field= driver.find element(By.Id , 'ap_email')
continue_field= driver.find element(By.id, 'continue')
need_help= driver.find element(By.xpath,"//span[contains(@class, 'a-expander-prompt')]")
forgot_password= driver.find element(By.id, 'auth-fpp-link-bottom')
other_issues= driver.find element(By.id, 'ap-other-signin-issues-link')
create_account= driver.find element(By.id, 'createAccountSubmit')
conditions_of_use= driver.find element (By.xpath, "//a[@href='https://www.amazon.com/gp/aw/help/ref=ap_mobile_signin_notification_condition_of_use?id=508088']")
privacy_notice = driver.find element(By.xpath, "//a[@href='https://www.amazon.com/gp/aw/help/ref=ap_mobile_signin_notification_privacy_notice?id=468496']")
"""