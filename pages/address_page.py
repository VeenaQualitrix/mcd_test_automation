from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "ADD_NEW": (By.XPATH, "//span[contains(text(), 'Add new')]"),
        "SEARCH_BUTTON": (By.XPATH, "//span[@class='searchbar__placeholder']"),
        "SEARCH_INPUT_FIELD": (By.XPATH, "//input[@class='searchbar__input']"),
        "SEARCH_RESULTS": (By.XPATH, "//div[@class='search-result__item']"),
        "SELECT_ADDRESS": (By.XPATH, "//div[contains(text(), '{}')]"),
        "CONFIRM_LOCATION": (By.XPATH, "//button[contains(text(), 'Confirm Location')]"),
        "HOUSE_NUMBER": (By.XPATH, "//input[@placeholder='*House / Flat No.']"),
        "SAVE_ADDRESS": (By.XPATH, "//button[contains(@class, 'bottom-sheet__cta')]"),
        "ADDED_ADDRESS": (By.XPATH, "//div[contains(@class, 'address__row-2')]/div[contains(text(), '{}')]"),
        "ADDRESS_SELECTED": (By.XPATH, "//div[contains(@class, 'txt-ellipsis')][contains(text(), '{}')]"),
        "ADD_ITEM": (By.XPATH, "//div[contains(@class, 'menu__title') and contains(normalize-space(), 'McVeggie Burger')]/following::div[contains(@class, 'add-to-cart')][1]"),
        "ITEM_DETAIL_PAGE": (By.XPATH, "//h5[contains(text(), ' Customise Your McVeggie Burger ')]"),
        "CLICK_NEXT": (By.XPATH, "//button[contains(text(), 'Next')]"),
        "CLICK_ADD_TO_CART": (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
        "CART_ICON": (By.XPATH, "//img[@class = 'toolbar-desktop__icon']"),
        "YOUR_ORDER": (By.XPATH, "//h1[contains(text(), ' Your Order')]"),
        "ADDED_ITEM_DISPLAY_IN_CART": (By.XPATH, "//h4[contains(text(), ' McVeggie Burger ')]"),
        "ADDRESS_ARROW": (By.XPATH, "//img[@alt = 'ic-arrow-down']"),
        "LOGIN_PROMPT": (By.XPATH, "//div[contains(text(), ' Log In / Sign Up to Continue ')]"),
        "LOGIN_FROM_CHECKOUT_PAGE": (By.XPATH, "//button[contains(text(), 'Log In / Sign Up to Continue')]"),

    }


class AddressPage(BasePage):

    def search_for_new_address(self):
        time.sleep(5)
        self.actions.click_button(*locators['ADD_NEW'])
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Bangalore")
        
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)

    def select_address_from_search_results(self):
        Multiple_locations = self.actions.wait_for_elements(*locators["SEARCH_INPUT_FIELD"])
        if len(Multiple_locations) != 0:
            print("Search Results are displayed for the entered location")
            self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Next To Victoria Hospital Gate"))
            time.sleep(3)
            self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
            self.actions.click_button(*locators["CONFIRM_LOCATION"])
            print("Clicked Confirm Location Button")
            time.sleep(5)
            self.actions.enter_text(*locators['HOUSE_NUMBER'], "987")
            self.actions.click_button(*locators["SAVE_ADDRESS"])
        else:
            print("No Search Reslts Displayed For The Given Input Field. Try Another Loocation!")

    def verify_address_is_added_and_selected(self):
        time.sleep(5)
        return self.actions.is_element_displayed(locators['ADDRESS_SELECTED'][0], locators['ADDRESS_SELECTED'][1].format("987"))
        
    def select_address_from_the_list(self):
        time.sleep(5)
        Address_Displayed = self.actions.is_element_displayed(locators['ADDED_ADDRESS'][0], locators['ADDED_ADDRESS'][1].format("987"))
        if Address_Displayed:
            self.actions.click_button(locators['ADDED_ADDRESS'][0], locators['ADDED_ADDRESS'][1].format("987"))
            time.sleep(3)
            return self.actions.is_element_displayed(locators['ADDRESS_SELECTED'][0], locators['ADDRESS_SELECTED'][1].format("987"))
        else:
            return False
        

    def add_item_in_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADD_ITEM'])
        self.actions.click_button(*locators['ADD_ITEM'])

    def verify_items_details_popup(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ITEM_DETAIL_PAGE'])
    
    def click_next_button(self):
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        time.sleep(2)

    def click_add_to_cart(self):
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        time.sleep(2)

    def verify_item_added_in_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['YOUR_ORDER'])
        self.actions.is_element_displayed(*locators['ADDED_ITEM_DISPLAY_IN_CART'])

    def click_add_address_arrow(self):
        self.actions.is_element_displayed(*locators['ADDRESS_ARROW'])
        self.actions.click_button(*locators['ADDRESS_ARROW'])
        time.sleep(2)

    def verify_redirect_to_login_or_signup_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PROMPT'])

