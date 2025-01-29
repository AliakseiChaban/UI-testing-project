from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

disagree_btn_loc = (By.XPATH, "//div[@class='qc-cmp2-summary-buttons']/button[2]")


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    def decline_privacy_policy(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(disagree_btn_loc))
        disagree_btn = self.driver.find_element(*disagree_btn_loc)
        disagree_btn.click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def wait_for_element_is_present(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.find_element(locator).text
