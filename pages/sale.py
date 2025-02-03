from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_url = "/sale.html"

    def check_categories_presence(self, list_of_categories):
        self.wait_for_element_is_present(loc.available_categories_loc)
        categories = self.find_elements(loc.available_categories_loc)
        for category in categories:
            assert category.text in list_of_categories, "Some of the categories is wrong or isn't present"

    def check_sale_is_selected(self):
        sale_attributes = self.get_attribute(loc.sale_in_navigation_section_loc, "class")
        assert "active" in sale_attributes, "The 'Sale' isn't selected in navigation section"

    def check_sale_page_title(self, sale_page_name):
        assert self.get_text(loc.sale_title_loc) == sale_page_name, "The wrong page title"

    def open_privacy_policy(self):
        self.click(loc.privacy_btn_loc)

    def check_policy_parameters_off(self):
        self.wait_for_element_is_present(loc.first_policy_loc)
        first = self.get_text(loc.first_policy_loc)
        second = self.get_text(loc.second_policy_loc)
        third = self.get_text(loc.third_policy_loc)
        list_of_policies = [first, second, third]

        for policy in list_of_policies:
            assert policy == "OFF", "Policy status is wrong"
