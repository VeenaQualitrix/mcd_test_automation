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


        