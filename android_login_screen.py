from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from actions.android_actions import AndroidActions
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import allure
import pytest

locators = {
    "LOGIN_SCREEN_HEADER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Welcome to Mcdonalds.']"),
    "LABEL_ENTER_MOBILE_NUMBER": (AppiumBy.XPATH, "//android.view.View[@text='Enter your mobile number']"),
    "MOBILE_NUMBER_INPUT_FIELD": (AppiumBy.XPATH, "//android.widget.EditText"),
    "BUTTON_VERIFY_MOBILE": (AppiumBy.XPATH, "//android.widget.Button[@text='Verify Mobile']"),
    "LABEL_ENTER_OTP": (AppiumBy.XPATH, "//android.widget.TextView[@text='Enter OTP']"),
    "OTP_INPUT_FIELD": (AppiumBy.XPATH, "(//android.widget.EditText)[{}]"),
    "BUTTON_VERIFY_OTP": (AppiumBy.XPATH, "//android.widget.Button[@text='Verify']"),
    "EMPTY_MOBILE_TEXTFIELD_ERROR": (AppiumBy.XPATH, "//android.view.View[@text='Please enter valid mobile number']"),
    "REFERRAL_CODE_LINK": (AppiumBy.XPATH, "//android.widget.TextView[@text='Click here if you have a referral code.']"),
    "REFERRAL_CODE_TEXT_FIELD": (AppiumBy.XPATH, "(//android.widget.EditText)[2]"),
    "TERMS_AND_CONDITIONS_LINK": (AppiumBy.XPATH, "//android.widget.Button[@text='Terms and Conditions']"),
    "TERMS_AND_CONDITIONS_HEADER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Terms and conditions']"),
    "REFERRAL_CODE_ERROR" : (AppiumBy.XPATH, "//android.view.View[@text='Please enter minimum 8 characters']"),
    "Entered_MOBILE_NUMBER_FIELD": (AppiumBy.XPATH, "//android.widget.EditText[@text='7777777777']"),
    }


class AndroidLoginScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.actions = AndroidActions(driver)  # <-- instantiate AndroidActions here

    def verify_login_screen_navigation(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_SCREEN_HEADER'])
  
    def enter_mobile_number(self, mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        time.sleep(5)
        print("Entered Mobile Number And Clicked On Verify Mobile Button")

    def enter_otp(self, otp):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
        by, value = locators["OTP_INPUT_FIELD"]

        for index, digit in enumerate(otp):
            field_locator = (by, value.format(index + 1))
            field = self.driver.find_element(*field_locator)
            field.click()
            time.sleep(0.2)

            self.driver.press_keycode(7 + int(digit))  # KEYCODE_0 is 7
            time.sleep(0.3)

        self.actions.tap_on_coordinates(100, 100)
        time.sleep(2)

        verify_by, verify_value = locators["BUTTON_VERIFY_OTP"]

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((verify_by, verify_value))
        )

        self.actions.click_button(verify_by, verify_value)
        print("OTP entered and Verify clicked.")
   
    def leave_mobile_field_empty(self):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        time.sleep(2)

        try:
            self.driver.hide_keyboard()
            print("Hide keyboard")
        except Exception as e:
            print(f"Keyboard might already be hidden: {e}")


    def verify_mobile_button_is_disabled(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, "//android.widget.Button[@text='Verify Mobile']")
        assert not element.is_enabled(), "Verify button should be disabled for empty or invalid input"
        print("Verified: Button is disabled as expected")
        # Always close the app, regardless of test pass/fail
        self.actions.close_app()

    def enter_invalid_mobile_number(self, invalid_mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], invalid_mobile_number)
        print("Entered invalid Mobile Number")

    def enter_alphabets_in_mobile_text_field(self, alphabets_in_mobile_number):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], alphabets_in_mobile_number)
        print("Entered alphabets in mobile number")

    def enter_mobile_number_with_space(self, mobile_number_with_space):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], mobile_number_with_space)
        print("Entered mobile number with spaces And Clicked On Verify Mobile Button")

    def enter_mobile_number_with_special_char(self, special_characters_in_mobile_field):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], special_characters_in_mobile_field)
        print("Entered mobile number with special characters And Clicked On Verify Mobile Button")

    def click_referral_code_link(self):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_LINK'])
        self.actions.click_button(*locators["REFERRAL_CODE_LINK"])
        time.sleep(5)
        print("Click here if you have a referral code text is displayed")

    def verify_referral_text_field_is_displayed(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
    
    def enter_referral_code(self, Referral_code):
        self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD'])
        self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], Referral_code)
        time.sleep(5)
        print("Entered referral code")

    def verify_referral_code_accepted_without_error(self):
        try:
            # Wait for the error message to disappear or not be present at all
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(locators["REFERRAL_CODE_ERROR"])
            )
            return True
        except TimeoutException:
            print("Referral code error is still visible or failed to disappear.")
            return False
        finally:
            # Always close the app, regardless of test pass/fail
            self.actions.close_app()
        
    def hide_keyboard_by_tapping_outside(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            print("Native hide_keyboard failed, falling back to tap.")

        mobile_field = self.driver.find_element(*locators['MOBILE_NUMBER_INPUT_FIELD'])
        rect = mobile_field.rect

        tap_x = rect['x'] + rect['width'] // 2
        tap_y = rect['y'] + rect['height'] + 10  # just below the input

        self.actions.tap_on_coordinates(tap_x, tap_y)

    def click_verify_mobile(self):
        time.sleep(5)
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        # print(verify_button)
        # verify_button.click()
        print("Clicked on 'Verify Mobile' button.")
        
    def enter_referral_code_click_verify(self, referral_code):
            if self.actions.is_element_displayed(*locators['REFERRAL_CODE_TEXT_FIELD']):
                self.actions.enter_text(*locators["REFERRAL_CODE_TEXT_FIELD"], referral_code)
                time.sleep(2)
                self.actions.click_button(*locators["MOBILE_NUMBER_INPUT_FIELD"])
                #self.click_verify_mobile()
                # ✅ Since we're in the same class, this works
                self.hide_keyboard_by_tapping_outside()

                print("Entered referral code and clicked verify")
            else:
                print("Referral code field not displayed")

    def mobile_field_empty_error(self):
            time.sleep(5)
            is_displayed = self.actions.is_element_displayed(*locators['EMPTY_MOBILE_TEXTFIELD_ERROR'])
            if is_displayed:
                print("Error displayed: 'Please enter the mobile number'")
            else:
                print("No error message for empty mobile field")
            return is_displayed

    def verify_otp_screen_is_displayed(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
    
    def click_terms_and_conditions_link(self):
        self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_LINK'])
        self.actions.click_button(*locators["TERMS_AND_CONDITIONS_LINK"])
        time.sleep(5)
        print("Terms and conditions clicked and redirected to the page")

    def verify_terms_and_conditions_header(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_HEADER'])
    
    def enter_mobile_number_one_by_one(self, mobile_number_11_digits):
        if not mobile_number_11_digits:
            raise ValueError("Mobile number test data is missing or empty.")

        self.actions.is_element_displayed(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field.clear()

        print("Entering mobile number one digit at a time (cumulative input):")
        typed_so_far = ""

        for digit in mobile_number_11_digits:
            typed_so_far += digit
            input_field.clear()
            input_field.send_keys(typed_so_far)
            time.sleep(0.3)

            # Debug: print current field value
            current_value = input_field.get_attribute("text")
            print(f"Typed so far: '{typed_so_far}', Field now shows: '{current_value}'")

            # Stop if field is full (max 10 digits)
            if len(current_value) >= 10:
                print("Field restricted at 10 digits. Stopping further input.")
                break
   
    def get_entered_mobile_number(self):
        locator = locators["MOBILE_NUMBER_INPUT_FIELD"]
        print(f"DEBUG: Waiting for visibility of element: {locator}")

        input_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        
        # Get current value of the input field
        current_value = input_field.get_attribute("text")
        print(f"DEBUG: Retrieved mobile number value: '{current_value}'")
        return current_value


    def copy_mobile_number_to_clipboard(self, mobile_number):
        self.driver.set_clipboard_text(mobile_number)
        print(f"Set Mobile Number '{mobile_number}' to device clipboard")

    def paste_mobile_number_using_clipboard(self):
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        input_field.click()
        time.sleep(1)

        # 🔁 Skip long press / paste tap — directly paste from clipboard
        clipboard_text = self.driver.get_clipboard_text()
        print(f"Clipboard Text Retrieved: {clipboard_text}")

        input_field.send_keys(clipboard_text)
        print("Sent clipboard text to input field using send_keys")
        time.sleep(2)
        

    def get_pasted_mobile_number(self):
        input_field = self.driver.find_element(*locators["MOBILE_NUMBER_INPUT_FIELD"])
        return input_field.get_attribute("text")
    
    def inspect_mobile_field(self):
        time.sleep(5)
        if self.actions.is_element_displayed(*locators['MOBILE_NUMBER_INPUT_FIELD']):
            return self.driver.find_element(*locators['MOBILE_NUMBER_INPUT_FIELD'])
        return None  

    def inspect_referral_link(self):
        if self.actions.is_element_displayed(*locators['REFERRAL_CODE_LINK']):
            return self.driver.find_element(*locators['REFERRAL_CODE_LINK'])
        return None

    def inspect_verify_button(self):
        if self.actions.is_element_displayed(*locators['BUTTON_VERIFY_MOBILE']):
            return self.driver.find_element(*locators['BUTTON_VERIFY_MOBILE'])
        return None

    def inspect_footer_link(self):
        if self.actions.is_element_displayed(*locators['TERMS_AND_CONDITIONS_LINK']):
            return self.driver.find_element(*locators['TERMS_AND_CONDITIONS_LINK'])
        return None
    
    def get_element_bounds(self, element):
        """
        Returns the bounding box of an element as a dictionary.
        """
        location = element.location
        size = element.size
        return {
            "left": location["x"],
            "top": location["y"],
            "right": location["x"] + size["width"],
            "bottom": location["y"] + size["height"],
        }

    def is_native_overlapping(self, el1, el2):
        """
        Determines if two native Android UI elements overlap based on their screen coordinates.
        """
        r1 = self.get_element_bounds(el1)
        r2 = self.get_element_bounds(el2)
        return not (
            r1["right"] <= r2["left"] or
            r1["left"] >= r2["right"] or
            r1["bottom"] <= r2["top"] or
            r1["top"] >= r2["bottom"]
        )

    
    def validate_login_screen_ui(self):
        print("Validating visibility, alignment, and non-overlapping of UI elements")

        elements = {
            "Mobile Field": self.inspect_mobile_field(),
            "Referral Link": self.inspect_referral_link(),
            "Verify Button": self.inspect_verify_button(),
            "Footer Link": self.inspect_footer_link(),
        }

        for name, element in elements.items():
            if element is None:
                self.driver.save_screenshot(f"{name.replace(' ', '_').lower()}_not_found.png")
                allure.attach.file(
                    f"{name.replace(' ', '_').lower()}_not_found.png",
                    name=f"{name} Not Found",
                    attachment_type=allure.attachment_type.PNG
                )
                pytest.fail(f"❌ Element not found or not visible: {name}")
            elif not element.is_displayed():
                self.driver.save_screenshot(f"{name.replace(' ', '_').lower()}_not_visible.png")
                allure.attach.file(
                    f"{name.replace(' ', '_').lower()}_not_visible.png",
                    name=f"{name} Not Visible",
                    attachment_type=allure.attachment_type.PNG
                )
                pytest.fail(f"❌ Element not visible: {name}")

        # Check for overlap
        element_list = list(elements.items())
        for i in range(len(element_list)):
            for j in range(i + 1, len(element_list)):
                name_i, el_i = element_list[i]
                name_j, el_j = element_list[j]
                overlapping = self.is_native_overlapping(el_i, el_j)
                if overlapping:
                    screenshot_name = f"overlap_{name_i}_{name_j}.png".replace(" ", "_").lower()
                    self.driver.save_screenshot(screenshot_name)
                    allure.attach.file(
                        screenshot_name,
                        name=f"Overlapping: {name_i} & {name_j}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    pytest.fail(f"❌ Elements overlapping: {name_i} and {name_j}")
    
    