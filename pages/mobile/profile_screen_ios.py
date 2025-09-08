from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.ios_actions import iOSActions
from selenium.webdriver.common.keys import Keys
import time
import allure
import pytest
import pyperclip


locators = {
    "FULL_NAME_FIELD": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[1]'
),
"SAVE_CHANGES_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Save Changes"),

"SAVE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Save"),

"VALID_MOBILE_NUMBER": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[2]'
),
"EDIT_ICON": (
    AppiumBy.ACCESSIBILITY_ID,
    "ic-editIcon"
),
"NAME_FIELD": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[@value="Enter your full name"]'
),
"CLEAR_NAME_FIELD": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[@value="John Doe"]'
),
"CLEAR_EMAIL_FIELD": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[3]'
),
'LABEL_ENTER_OTP': (
    AppiumBy.XPATH,
    '//XCUIElementTypeStaticText[@name="One time Password (OTP) has been sent to"]'
    ),
'OTP_INPUT_FIELD': (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField'),

'BUTTON_VERIFY_OTP': ( AppiumBy.ACCESSIBILITY_ID,"Verify"),

"EMAIL_FIELD": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[@value="Enter Your Email ID here"]'
),
"EMAIL_FIELD_WITHOUT_HERE": (
    AppiumBy.XPATH,
    '//XCUIElementTypeTextField[@value="Enter Your Email ID"]'
),
"DOB_FIELD":(AppiumBy.XPATH, '//XCUIElementTypeTextField[4]'),

"DOB_SAVE_BUTTON":(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Select"]'),

"FUTURE_DATE":(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Sunday, 31 August"]'),

"CLICK_CHANGE_PICTURE":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Change Picture"]'),

"FROM_PHOTO":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="From Photos"]'),

"TAKE_PICTURE":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Take Picture"]'),

"SAVE_IS_DISABLED": (AppiumBy.ACCESSIBILITY_ID, "Save"),

"NAME_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-user"]'),

"PHONE_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-mobile"]'),

"EMAIL_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-message"]'),

"DOB_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-calender"]'),

"COLOR_BLIND":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Click to select colour blind friendly mode"]'),

"MCDELIVERY_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-delivery-active"]'),

"DINEIN_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-dine-in"]'),

"ONTHEGO_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-otg"]'),

"TAKEAWAY_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-delivery"]'),

}
class ProfileScreenIos(BasePage):


    def enter_full_name(self, name):
        time.sleep(2)
        self.actions.click_button(*locators["FULL_NAME_FIELD"])
        self.actions.clear_text(*locators["FULL_NAME_FIELD"])  # use your own clear_text method here
        self.actions.enter_text(*locators["FULL_NAME_FIELD"], name)
        print(f"Entered name: {name}")

    def clear_full_name(self):
        print("Trying to clear full name field")
        self.actions.clear_text(*locators['CLEAR_NAME_FIELD'])
        print("Cleared full name field")



    
    def enter_otp(self, OTP):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
        self.actions.enter_text(*locators["OTP_INPUT_FIELD"], OTP)
        self.actions.click_button(*locators["BUTTON_VERIFY_OTP"])
        time.sleep(5)
        print("Entered OTP And Clicked On Verify Mobile Button")
        
    def click_save_changes(self):
        self.actions.click_button(*locators["SAVE_CHANGES_BUTTON"])
        print("Clicked on Save Changes button")

    def click_save(self):
        self.actions.click_button(*locators["SAVE_BUTTON"])
        print("Clicked on Save Changes button")    

    def invalid_character(self, name):
        time.sleep(2)
        # self.actions.click_button(*locators['NAME_FIELD'])  # Focus the field
        self.actions.enter_text(*locators['NAME_FIELD'], name)  # Enter invalid name
        print(f"Entered invalid name: {name}")
    
    def tap_edit_icon(self):
        time.sleep(2)
        self.actions.click_button(*locators['EDIT_ICON'])
        print("Tapped on the Edit icon")

    def verify_the_number(self, valid_number):
        time.sleep(2)
        self.actions.is_element_displayed(*locators["VALID_MOBILE_NUMBER"])
        print(f"Verified the number: {valid_number}")

        
    
    def enter_email(self, email):
        time.sleep(2)
        self.actions.enter_text(*locators["EMAIL_FIELD"], email)
        print(f"Entered email: {email}")

    
    def enter_invalid_email_address(self, email):
        time.sleep(2)
        self.actions.clear_text(*locators['CLEAR_EMAIL_FIELD'])
        time.sleep(2)
        self.actions.enter_text(*locators["EMAIL_FIELD_WITHOUT_HERE"], email)
        print(f"Entered email: {email}")  

    def click_DOB(self):
        time.sleep(5)
        self.actions.click_button(*locators['DOB_FIELD'])
        print("Tapped on the DOB")

    def save_button_on_DOB(self):
        time.sleep(3)
        self.actions.click_button(*locators['DOB_SAVE_BUTTON'])
        print("Tapped on the DOB save")    

    def validate_future_dates(self):
        time.sleep(3)
        self.actions.click_button(*locators['DOB_FIELD'])
        self.actions.is_element_displayed(*locators['FUTURE_DATE']) 
        print("Future date element displayed") 

    
    def click_change_pictures_link(self):
        time.sleep(3)
        self.actions.click_button(*locators['CLICK_CHANGE_PICTURE'])
        print("Tapped on the change picture") 

    
    def verify_profile_picture_field(self):
        time.sleep(3)
        from_photo_visible = self.actions.is_element_displayed(*locators['FROM_PHOTO'])
        print(f"From Photo option visible: {from_photo_visible}")
        take_picture_visible = self.actions.is_element_displayed(*locators['TAKE_PICTURE'])
        print(f"Take Picture option visible: {take_picture_visible}")

    def verify_save_button_disabled(self):
        self.actions.click_button(*locators["SAVE_IS_DISABLED"])
        print("Clicked on Save button disabled")


    def click_color_blinded_toggle(self):
        time.sleep(3)
        self.actions.click_button(*locators['COLOR_BLIND'])
        self.actions.click_button(*locators[''])


    def verify_field_icons(self):
        time.sleep(3)
        name_icon_visible = self.actions.is_element_displayed(*locators['NAME_ICON'])
        print(f"Name icon visible: {name_icon_visible}")
        phone_icon_visible = self.actions.is_element_displayed(*locators['PHONE_ICON'])
        print(f"Phone icon visible: {phone_icon_visible}")
        email_icon_visible = self.actions.is_element_displayed(*locators['EMAIL_ICON'])
        print(f"Email icon visible: {email_icon_visible}")
        dob_icon_visible = self.actions.is_element_displayed(*locators['DOB_ICON'])
        print(f"DOB icon visible: {dob_icon_visible}")


    def click_business_model_dropdown(self):
        time.sleep(3)  # Consider replacing with explicit waits for better reliability
        print("Clicking on MCDELIVERY icon...")
        if self.actions.is_element_displayed(*locators['MCDELIVERY_ICON']):
            self.actions.click_button(*locators['MCDELIVERY_ICON'])
        else:
            print("MCDELIVERY icon not visible.")
        print("Clicking on DINEIN icon...")
        if self.actions.is_element_displayed(*locators['DINEIN_ICON']):
            self.actions.click_button(*locators['DINEIN_ICON'])
        else:
            print("DINEIN icon not visible.")
        print("Clicking on ONTHEGO icon...")
        if self.actions.is_element_displayed(*locators['ONTHEGO_ICON']):
            self.actions.click_button(*locators['ONTHEGO_ICON'])
        else:
            print("ONTHEGO icon not visible.")

        print("Clicking on TAKEAWAY icon...")
        if self.actions.is_element_displayed(*locators['TAKEAWAY_ICON']):
            self.actions.click_button(*locators['TAKEAWAY_ICON'])
        else:
            print("TAKEAWAY icon not visible.")
       

    # def enter_otp(self, otp):
    #     self.actions.is_element_displayed(*locators['LABEL_ENTER_OTP'])
    #     by, value = locators["OTP_INPUT_FIELD"]
        
    #     for index, digit in enumerate(otp):
    #         field_locator = (by, value.format(index + 1))
    #         field = self.driver.find_element(*field_locator)
    #         field.click()
    #         time.sleep(0.2)

    #         field.send_keys(digit)  # ✅ Use send_keys instead of press_keycode

    #         time.sleep(0.3)

    #     self.actions.tap_on_coordinates(100, 100)
    #     time.sleep(2)

    #     verify_by, verify_value = locators["BUTTON_VERIFY_OTP"]

    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((verify_by, verify_value))
    #     )

    #     self.actions.click_button(verify_by, verify_value)
    #     print("OTP entered and Verify clicked.")
       