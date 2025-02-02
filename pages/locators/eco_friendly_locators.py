from selenium.webdriver.common.by import By

sort_by_dropdown_loc = (By.XPATH, "//select[@id='sorter']")
desc_sorting_btn_loc = (By.XPATH, "//a[@title='Set Descending Direction']")
asc_sorting_btn_loc = (By.XPATH, "//a[@title='Set Ascending Direction']")
clothes_price_loc = (By.XPATH, "//span[contains(@id, 'product-price-')]")

last_clothe_on_page_loc = (By.XPATH, "//ol[contains(@class, 'products')]/li[12]")
last_clothe_xs_size_loc = (By.XPATH, "//li[@class='item product product-item'][12]/descendant::div[text()='XS']")
last_clothe_first_color_loc = (
    By.XPATH, "//li[@class='item product product-item'][12]/descendant::div[@class='swatch-option color'][1]"
)
add_to_cart_btn_loc = (
    By.XPATH, "//li[@class='item product product-item'][12]/descendant::button[@title='Add to Cart']"
)
last_clothe_name_loc = (
    By.XPATH, "//li[@class='item product product-item'][12]/descendant::a[@class='product-item-link']"
)
add_success_message_loc = (By.XPATH, "//div[@data-ui-id='message-success']/div")

my_cart_loc = (By.XPATH, "//a[@class='action showcart']")
cart_counter_parent_loc = (By.XPATH, "//span[@class='counter qty empty']")
cart_counter_child_loc = (By.XPATH, "//span[@class='counter-number']")
remove_btn_loc = (By.XPATH, "//a[@title='Remove item']")
confirm_modal_loc = (By.XPATH, "//button[contains(@class, 'action-accept')]")
empty_cart_block_loc = (By.XPATH, "//div[@id='ui-id-1']")
empty_cart_text_loc = (By.XPATH, "//div[@id='ui-id-1']/descendant::strong[@class='subtitle empty']")
