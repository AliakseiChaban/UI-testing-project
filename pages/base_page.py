from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    def select_from_dropdown_by_value(self, dropdown, text):
        select = Select(dropdown)
        select.select_by_visible_text(text)

    def on_hover_and_click(self, on_hover_element, element_to_click):
        ActionChains(self.driver).move_to_element(on_hover_element).click(element_to_click).perform()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))

    def wait_for_element_is_present(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_class_change(self, locator, class_to_disappear, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            lambda d: class_to_disappear in d.find_element(*locator).get_attribute("class")
        )

    def wait_for_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def switch_to_modal_and_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def switch_to_iframe(self, iframe_locator, confirm_btn_loc):
        iframe = self.driver.find_element(*iframe_locator)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*confirm_btn_loc).click()
        self.driver.switch_to.default_content()
