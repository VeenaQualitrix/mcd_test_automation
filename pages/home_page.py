from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "HEADER_BANNER": (By.XPATH, "//ion-header[@role='banner']"),
        "VIEW_ICON": (By.XPATH, "//div[@title='View Profile']"),
        "ADDRESS_DROPDOWN": (By.XPATH, "(//div[@class='toolbar-v1__location-type txt-ellipsis']/img[@title='ic-arrow-down'])[1]")
    }


class HomePage(BasePage):

    def verify_website_header_banner(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['HEADER_BANNER'])
    
    def click_on_view_icon(self):
        self.actions.click_button(*locators['VIEW_ICON'])
        print("Clicked View Icon On Home Page")
    
    def click_on_add_address(self):
        self.actions.click_button(*locators['ADDRESS_DROPDOWN'])
