from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
        "MYMCD_LOGO": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-MyMcD_Logo']"),
        "LOGIN_BUTTON": (AppiumBy.XPATH, "//android.widget.TextView[@text='Login/Sign Up']"),
        "LOG_OUT_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='ic-logoutIcon Logout ic-arrow-right']"),
        "PROFILE_EDIT_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-editIcon']"),
        "POPUP_DO_LATER": (By.XPATH, "//android.widget.Button[@text='I'll Do It Later']"),
    
    }


class AndroidViewScreen(BasePage):

    def verify_view_screen_navigation(self):
        is_displayed = self.actions.is_element_displayed(*locators['MYMCD_LOGO'])
        print(f"View screen element displayed: {is_displayed}")
        return is_displayed
    
    def click_on_login_or_sign_up_button(self):
        time.sleep(2)
        self.actions.click_button(*locators['LOGIN_BUTTON'])
        print("Clicked Login button")

    def Click_log_out_button(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MYMCD_LOGO'])

        # Scroll and get the Logout element directly
        logout_element = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().textContains("Logout"));'
        )

        # Click it
        logout_element.click()
        print("Clicked on Log out button")
        time.sleep(2)
        self.actions.click_button(*locators['POPUP_DO_LATER'])

    def click_profile_edit_icon(self):
        time.sleep(2)
        self.actions.click_button(*locators['PROFILE_EDIT_ICON'])
        print("Clicked Profile edit icon")


    def Verify_current_profile_info(self, user_data_store):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MYMCD_LOGO'])
        time.sleep(2)
        user_data_store["original_name"] = self.driver.find_element(*locators['PROFILE_NAME']).get_attribute("value")
        user_data_store["original_mobile"] = self.driver.find_element(*locators['PROFILE_MOBILE']).get_attribute("value")
        user_data_store["original_email"] = self.driver.find_element(*locators['PROFILE_EMAIL']).get_attribute("value")
        print("Captured profile info: ")
        print(user_data_store)
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON'])
        self.actions.click_button(*locators['MCDELIVERY_ICON'])

    def Verify_profile_info_remian_unchanged(self, user_data_store):
        time.sleep(2)
        current_name = self.driver.find_element(*locators['PROFILE_NAME']).get_attribute("value")
        current_mobile = self.driver.find_element(*locators['PROFILE_MOBILE']).get_attribute("value")
        current_email = self.driver.find_element(*locators['PROFILE_EMAIL']).get_attribute("value")

        assert current_name == user_data_store["original_name"], f"Expected name: {user_data_store['original_name']}, but got: {current_name}"
        assert current_mobile == user_data_store["original_name"], f"Expected name: {user_data_store['original_mobile']}, but got: {current_name}"
        assert current_email == user_data_store["original_email"], f"Expected email: {user_data_store['original_email']}, but got: {current_email}"
        print(" Profile info remains unchanged after switching business model.")

    
