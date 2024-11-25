from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "ADD_NEW": (By.XPATH, "//span[contains(text(), 'Add new')]"),
        "SEARCH_BUTTON": (By.XPATH, "//div[@class='searchbar__mock-input']"),
        "SEARCH_INPUT_FIELD": (By.XPATH, "//input[@class='searchbar__input']"),
        "SEARCH_RESULTS": (By.XPATH, "//div[@class='search-result__item']"),
        "SELECT_ADDRESS": (By.XPATH, "//div[contains(text(), '{}')]"),
        "CONFIRM_LOCATION": (By.XPATH, "//button[contains(text(), 'Confirm Location')]"),
        "HOUSE_NUMBER": (By.XPATH, "//input[@placeholder='*House / Flat No.']"),
        "SAVE_ADDRESS": (By.XPATH, "//button[contains(@class, 'bottom-sheet__cta')]"),
        "ADDED_ADDRESS": (By.XPATH, "//div[contains(@class, 'address__row-2')]/div[contains(text(), '{}')]"),
        "ADDRESS_SELECTED": (By.XPATH, "//div[contains(@class, 'txt-ellipsis')][contains(text(), '{}')]")
    }


class AddressPage(BasePage):

    def search_for_new_address(self):
        time.sleep(5)
        self.actions.click_button(*locators['ADD_NEW'])
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Chennai")
        time.sleep(5)

    def select_address_from_search_results(self):
        Multiple_locations = self.actions.wait_for_elements(*locators["SEARCH_INPUT_FIELD"])
        if len(Multiple_locations) != 0:
            print("Search Results are displayed for the entered location")
            self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Great Southern Trunk Road"))
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


