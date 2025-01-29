from selenium.webdriver.common.by import By

f_name_field_loc = (By.XPATH, "//input[@id='firstname']")
l_name_field_loc = (By.XPATH, "//input[@id='lastname']")
address_field_loc = (By.XPATH, "//input[@id='email_address']")
pwd_field_loc = (By.XPATH, "//input[@id='password']")
pwd_confirmation_field_loc = (By.XPATH, "//input[@id='password-confirmation']")

f_name_field_error_loc = (By.XPATH, "//div[@id='firstname-error']")
l_name_field_error_loc = (By.XPATH, "//div[@id='lastname-error']")
address_field_error_loc = (By.XPATH, "//div[@id='email_address-error']")
pwd_field_error_loc = (By.XPATH, "//div[@id='password-error']")
pwd_confirmation_field_error_loc = (By.XPATH, "//div[@id='password-confirmation-error']")
create_btn_loc = (By.XPATH, "//button[@title='Create an Account']")
