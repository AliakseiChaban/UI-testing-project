from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendlyClothes(BasePage):
    page_url = "/collections/eco-friendly.html"
    expected_message = "You have no items in your shopping cart."

    def sort_clothes_by(self, option_text):
        dropdown = self.find_element(loc.sort_by_dropdown_loc)
        self.select_from_dropdown_by_value(dropdown, option_text)

    def set_descending_direction(self):
        self.click(loc.desc_sorting_btn_loc)

    def select_clothe_parameters_and_add_to_cart(self):
        clothe = self.find_element(loc.last_clothe_on_page_loc)
        self.scroll_to_element(loc.last_clothe_on_page_loc)
        size = self.find_element(loc.last_clothe_xs_size_loc)
        self.on_hover_and_click(clothe, size)
        self.click(loc.last_clothe_first_color_loc)
        self.click(loc.add_to_cart_btn_loc)

    def check_sorting_by_price_desc(self):
        prices = self.find_elements(loc.clothes_price_loc)
        prices_list = []
        for price in prices:
            price_to_float = float(price.text.replace("$", ""))
            prices_list.append(price_to_float)
        sorted_prices_list = sorted(prices_list, reverse=True)
        assert prices_list == sorted_prices_list, "Prices sorted incorrectly"

    def check_clothe_added_message(self):
        clothe_name = self.get_text(loc.last_clothe_name_loc)
        self.wait_for_element_is_present(loc.add_success_message_loc)
        self.scroll_to_top()
        success_msg = self.get_text(loc.add_success_message_loc)
        assert success_msg == f"You added {clothe_name} to your shopping cart.", "The wrong message text is displayed"

    def open_not_empty_cart(self):
        self.wait_for_class_change(loc.cart_counter_parent_loc, "empty")
        self.wait_for_text_in_element(loc.cart_counter_child_loc, "1")
        self.click(loc.my_cart_loc)

    def remove_the_first_clothe_from_cart(self):
        self.wait_for_element_to_be_clickable(loc.remove_btn_loc)
        self.click(loc.remove_btn_loc)
        self.wait_for_element_to_be_clickable(loc.confirm_modal_loc)
        self.click(loc.confirm_modal_loc)

    def check_cart_is_empty(self):
        self.wait_for_element_is_present(loc.empty_cart_block_loc)
        self.wait_for_element_is_present(loc.empty_cart_text_loc)
        assert self.expected_message == self.get_text(loc.empty_cart_text_loc), (
            "There is a wrong message, or item isn't removed"
        )

    def check_counter_is_not_visible(self):
        attribute = self.get_attribute(loc.cart_counter_parent_loc, "class")
        assert attribute == "counter qty empty"
