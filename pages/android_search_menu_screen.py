from pages.base_page import BasePage
from pages.android_view_screen import AndroidViewScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "SEARCH_MENU_SCREEN": (AppiumBy.XPATH, "//android.widget.TextView[@text='Search Menu']"),
        "SEARCH_MENU_TEXTFIELD": (AppiumBy.XPATH, "//android.widget.EditText"),
        "SEARCH_MENU_ICON": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-search'])[1]"),
        "BURGER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='McVeggie Burger']"),
        "ADD_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-add']"),
        "ADD_TO_CART_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Add to Cart']"),
        "VIEW_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='View Cart']"),
        "CART_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-cart-outline']"),
        "HOME_ICON": (AppiumBy.XPATH, "//android.widget.TextView[@text='Home']"),
        "FRIES_MENU": (AppiumBy.XPATH, "//android.widget.TextView[@text='Fries (Medium)']"),
        "ITEM_NOT_FOUND_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Oops, no results found!']"),
        "SEARCH_MENU_ITEM_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Search menu item']"),
        "VEG_FILTER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Veg']"),
        "VEG_ICON_SYMBOL": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-veg'])[1]"),
        "NON_VEG_FILTER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Non-Veg']"),
        "NON_VEG_ICON_SYMBOL": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-nonveg'])[1]"),
        "CLICK_CLEAR_ALL": (AppiumBy.XPATH, "//android.widget.TextView[@text='Clear All']"),
        "POPULAR_ITEMS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Popular Items']"),
        "RECENT_SEARCHES": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your Recent Searches']"),
        "BURGER_SEARCH_RESULT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Burger']"),
        "WRAP_SEARCH_RESULT": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Wrap'])[2]"),
        "WRAP_ITEM": (AppiumBy.XPATH, "//android.widget.TextView[@text='Big Spicy Paneer Wrap Combo']"),
        "VEG_FILTER_CLOSE_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-close-red']"),
        "BACK_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-left-primary']"),

         }


class AndroidSearchMenuScreen(BasePage):
    
    def verify_search_menu_screen_navigation(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_SCREEN'])
        print("Navigated to search menu screen")

    def click_on_search_textfield_in_search_menu_screen(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_TEXTFIELD'])
        self.actions.click_button(*locators["SEARCH_MENU_TEXTFIELD"])
        print("Clicked on search menu textfield")

    def enter_burger_name_and_click_search(self):
        time.sleep(3)
        self.actions.enter_text(*locators['SEARCH_MENU_TEXTFIELD'], "Mcveggie Burger")
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")

    def verify_item_name_displays(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['BURGER_NAME'])
        print("'Mcveggie' burger name is displayed ")

    def click_on_add_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ADD_BUTTON'])
        self.actions.click_button(*locators["ADD_BUTTON"])
        print("Clicked on add button")

    def click_on_add_to_cart_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ADD_TO_CART_BUTTON'])
        self.actions.click_button(*locators["ADD_TO_CART_BUTTON"])
        print("Clicked on 'add to cart' button")

    def click_on_view_cart_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['VIEW_CART'])
        self.actions.click_button(*locators["VIEW_CART"])
        print("Clicked on 'view cart' button")

    def verify_browse_menu(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_SCREEN'])
        time.sleep(3)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_TEXTFIELD'])
        self.actions.click_button(*locators["SEARCH_MENU_TEXTFIELD"])
        print("Clicked on search menu textfield")
        time.sleep(2)
        self.actions.enter_text(*locators['SEARCH_MENU_TEXTFIELD'], "Mcveggie Burger")
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ADD_BUTTON'])
        self.actions.click_button(*locators["ADD_BUTTON"])
        print("Clicked on add button")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ADD_TO_CART_BUTTON'])
        self.actions.click_button(*locators["ADD_TO_CART_BUTTON"])
        print("Clicked on 'add to cart' button")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['VIEW_CART'])
        print("'view cart' is displayed")
        self.actions.is_element_displayed(*locators['CART_ICON'])
        print("'cart icon' is displayed")
        time.sleep(2)
        self.actions.click_button(*locators["HOME_ICON"])
        time.sleep(2)

    def enter_fries_and_click_search(self, menu_item):
        time.sleep(3)
        self.actions.enter_text(*locators["SEARCH_MENU_TEXTFIELD"], menu_item)
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")


    def verify_search_result_display_fries_menu_items(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['FRIES_MENU'])
        print("Fries menu items is displayed")

    def enter_pasta_and_click_search(self, menu_item_nonexistent):
        time.sleep(3)
        self.actions.enter_text(*locators["SEARCH_MENU_TEXTFIELD"], menu_item_nonexistent)
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")

    def verify_message_when_items_not_found(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ITEM_NOT_FOUND_TEXT'])
        print("No matching item found text is displayed")

    def click_search_with_empty_input(self):
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_MENU_ICON'])
        print("Clicked search menu Icon On menu Page")

    def verify_prompt_display(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['POPULAR_ITEMS'])
        print("No action should be taken")

    def click_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VEG_FILTER'])
        print("Veg filter is displayed")
        self.actions.click_button(*locators['VEG_FILTER'])
        print("Clicked veg filter On menu Page")

    def verify_display_of_veg_items(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['VEG_ICON_SYMBOL'])
        print("Veg itmes is displayed after appling the veg filter")

    def click_non_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['NON_VEG_FILTER'])
        print("Non-Veg filter is displayed")
        self.actions.click_button(*locators['NON_VEG_FILTER'])
        print("Clicked non-veg filter On menu Page")

    def verify_display_of_non_veg_items(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['NON_VEG_ICON_SYMBOL'])
        print("Non-Veg itmes is displayed after appling the Non-veg filter")

    def enter_burger_and_click_search(self, search_burger):
        time.sleep(3)
        self.actions.enter_text(*locators["SEARCH_MENU_TEXTFIELD"], search_burger)
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")

    def clear_search_input_field(self):
        time.sleep(3)
        self.actions.click_button(*locators["CLICK_CLEAR_ALL"])
        print("Cleared the entered input from search field")

    def verify_default_view_restored(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['POPULAR_ITEMS'])
        print("popular items text is displayed after clearing the recent serarch")

    def verify_burger_search_result_persist_post_add(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['RECENT_SEARCHES'])
        print("'Your Recent searches' text is displayed")
        self.actions.is_element_displayed(*locators['BURGER_SEARCH_RESULT'])
        print("burger search result is persist post add the burger")

    def enter_wrap_and_click_search(self, search_wrap):
        time.sleep(3)
        self.actions.enter_text(*locators["SEARCH_MENU_TEXTFIELD"], search_wrap)
        self.actions.click_button(*locators["SEARCH_MENU_ICON"])
        print("Clicked on search menu icon")

    def verify_veg_wrap_item_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['RECENT_SEARCHES'])
        print("'Your Recent searches' text is displayed")
        self.actions.is_element_displayed(*locators['WRAP_SEARCH_RESULT'])
        print("Wrap search result is displayed")
        time.sleep(1)
        self.actions.is_element_displayed(*locators['WRAP_ITEM'])
        print("'Big Spicy Paneer Wrap Combo' text is displayed")

    def verify_placeholder_shows_search_here(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_TEXTFIELD'])
        print("Search here text is displayed")

    def click_close_icon_on_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VEG_FILTER_CLOSE_ICON'])
        print("Veg filter close icon is displayed")
        self.actions.click_button(*locators['VEG_FILTER_CLOSE_ICON'])
        print("Clicked on close icon of veg filter")

    def Click_back_button_from_search_menu(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['BACK_BUTTON'])
        self.actions.click_button(*locators['BACK_BUTTON'])
        print("Back button clicked")
        

    


        