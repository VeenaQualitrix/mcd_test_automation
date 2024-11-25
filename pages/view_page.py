from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "PROFILE_PAGE_NAVIGATION": (By.XPATH, "//div[@class='profile-page']"),
        "LOGIN_BUTTON": (By.XPATH, "//h2[contains(text(), 'Login/Sign Up')]")
    }


class ViewPage(BasePage):

    def verify_view_page_is_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['PROFILE_PAGE_NAVIGATION'])
 
    def click_on_login_or_sign_up_button(self):
        self.actions.click_button(*locators['LOGIN_BUTTON'])
        print("Clicked Profile Icon On Home Page")
