from selenium.webdriver.common.by import By

locator = (By.XPATH, "test")
available_categories_loc = (By.XPATH, "//div[@class='categories-menu']/strong/span")
sale_in_navigation_section_loc = (By.XPATH, "//ul[@id='ui-id-2']/li[6]")
sale_title_loc = (By.XPATH, "//h1[@id='page-title-heading']")
privacy_btn_loc = (By.XPATH, "//a[@id='qc-cmp2-persistent-link']")
privacy_modal_window_loc = (By.XPATH, "//a[@id='qc-cmp2-ui']")

first_policy_loc = (
    By.XPATH, "//button[@aria-controls='stack-item-id:1-expandable']/descendant::li[@class='qc-cmp2-list-item-status']"
)
second_policy_loc = (
    By.XPATH, "//button[@aria-controls='stack-item-id:42-expandable']/descendant::li[@class='qc-cmp2-list-item-status']"
)
third_policy_loc = (By.XPATH, "//p[@class='qc-cmp2-list-item-status']")
