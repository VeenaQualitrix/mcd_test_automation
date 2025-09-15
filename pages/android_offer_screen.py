from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "OFFERS_PAGE":(AppiumBy.XPATH, "//android.widget.TextView[@text='Offers For You']"),
        "APPLY_FIRST_OFFER": (AppiumBy.XPATH, "(//android.widget.Button[@text='Apply'])[1]"),
        "CHOOSE_FIRST_ITEM": (AppiumBy.XPATH, "(//android.widget.Button[@text='Select'])[1]"),
        "DISCOUNT_COUPON": (AppiumBy.XPATH, "//android.widget.TextView[@text= 'Discount Coupon']"),
        "OFFER_APPLIED_SUCCESS_MESSAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text= 'Promo Applied Successfully']"),
        "SUCCESS_MESSAGE_OK_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='OK']"),
        "FIRST_OFFER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='SPD82AA49EE9040']"),
        "SECOND_OFFER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='SPDB28292DD88C1']"),
        "OFFER_CODE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Offer Applied!']/following-sibling::android.widget.TextView[1]"),
        "COUPON_LIST_CODES": (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'SPD')]"),
        "OFFER_APPLIED_TEXT": (AppiumBy.XPATH, "//android.view.View[@text='Offer Applied! View All']"),
        "CHANGE_OFFER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Change Offer']"),
        "OFFER_SERCHBAR": (AppiumBy.XPATH, "//android.widget.EditText"),
        "OFFER_APPLY_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Apply']"),
        "PROMO_HEADLINE": (AppiumBy.XPATH, "//android.widget.TextView[@text = 'Promo Not Applied']"),
        "PROMO_EXPIRED_MESSAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text = 'Promo Code Expired']"),
        "FLAT10_COUPON_CODE": (AppiumBy.XPATH, "//android.widget.TextView[@text='FLAT 10 OFF']"),
        "COUPON_DESCRIPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='10% Discount on purchase of ₹300']"),
        "SHOW_MORE": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Show More'])[1]"),
        "APPLY_BUTTON": (AppiumBy.XPATH, "(//android.widget.Button[@text='Apply'])[1]"),
        "FREEDELIVERY_COUPON_CODE": (AppiumBy.XPATH, "//android.widget.TextView[@text='freedelivery@199']"),
        "FREEDELIVERY_FREEPRODUCT_COUPON_CODE": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Freedelivery+Free product'])[1]"),
}

class AndroidOfferPage(BasePage):


        def verify_user_redirected_to_offers_page(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFERS_PAGE'])
                print("ALL available offers is displayed")
                # Navigate back after verification
                self.driver.back()
                time.sleep(1)
                self.driver.back()
                time.sleep(1)

        def verify_coupon_switch(self):
                try:
                        # Step 1: Apply the first coupon
                        WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable(locators['APPLY_FIRST_OFFER'])
                        )
                        self.driver.find_element(*locators['APPLY_FIRST_OFFER']).click()
                        self.actions.click_button(*locators['CHOOSE_FIRST_ITEM'])

                        # Wait for success message and dismiss it
                        WebDriverWait(self.driver, 20).until(
                        EC.visibility_of_element_located(locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                        )
                        self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                        print("First coupon applied successfully")

                        # Wait for "Offer Applied!" section to appear
                        WebDriverWait(self.driver, 20).until(
                        EC.visibility_of_element_located(locators['OFFER_APPLIED_TEXT'])
                        )

                        applied_coupon = WebDriverWait(self.driver, 30).until(
                                EC.visibility_of_element_located(locators['FIRST_OFFER_NAME'])
                                ).text.strip()

                        print(f"Fetched first applied coupon: {applied_coupon}")
                        assert applied_coupon != "", "First coupon code is empty!"

                        # Step 2: Click on "Change Offer"
                        self.actions.click_button(*locators['CHANGE_OFFER'])
                        print("Clicked on Change Offer")

                        # Wait for coupon list to reload
                        WebDriverWait(self.driver, 20).until(
                        EC.presence_of_all_elements_located(locators['APPLY_FIRST_OFFER'])
                        )

                        # Apply second coupon
                        self.driver.find_element(*locators['APPLY_FIRST_OFFER']).click()
                        self.actions.click_button(*locators['CHOOSE_FIRST_ITEM'])

                        # Wait for success message and dismiss it
                        WebDriverWait(self.driver, 20).until(
                        EC.visibility_of_element_located(locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                        )
                        self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                        print("Second coupon applied successfully")

                        final_applied_coupon = WebDriverWait(self.driver, 30).until(
                                EC.visibility_of_element_located(locators['SECOND_OFFER_NAME'])
                                ).text.strip()

                        print(f"Fetched second applied coupon: {final_applied_coupon}")

                        #  Validate coupon switch
                        assert final_applied_coupon != applied_coupon, (
                        f"Coupon did not switch! Expected a different coupon but found: {final_applied_coupon}"
                        )

                        print(f" Successfully switched from {applied_coupon} to {final_applied_coupon}!")

                except Exception as e:
                        print(f" Test failed: {str(e)}")
                        raise


        def enter_expired_promo_code_and_click_search(self, Expired_Promo):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Expired_Promo)
                self.actions.click_button(*locators["OFFER_SERCHBAR"])
                time.sleep(5)
                print("Entered expired promo code And Clicked On search Button")

        def click_offer_apply_and_select_button(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFER_APPLY_BUTTON'])
                print("Offer apply button is displayed")
                self.actions.click_button(*locators['OFFER_APPLY_BUTTON'])
                print("apply button is clicked")
                time.sleep(3)
                self.actions.is_element_displayed(*locators['CHOOSE_FIRST_ITEM'])
                print("Offer select button is displayed")
                self.actions.click_button(*locators['CHOOSE_FIRST_ITEM'])
                print("Select button is clicked")

        def verify_promo_expired_message(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['PROMO_HEADLINE'])
                self.actions.is_element_displayed(*locators['PROMO_EXPIRED_MESSAGE'])
                print("Promo expired message is displayed")
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Clicked 'Ok button")
                time.sleep(2)
                self.driver.back()
                time.sleep(1)
                self.driver.back()

        def verify_input_box_for_entering_coupon_code_visible_and_functional(self, Coupon_code):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Coupon_code)
                time.sleep(1)
                self.actions.click_button(*locators["OFFER_SERCHBAR"])
                print("Input box for entering coupon code is visible and functional")

        def verify_freedelivery_offer_card_visible(self):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['FREEDELIVERY_COUPON_CODE'])
                print("FreeDelivery@199 offercard should visible")
                time.sleep(2)
                self.driver.back()
                time.sleep(1)
                self.driver.back()

        def enter_a_Flat10_coupon_code_into_the_input_box(self, Flat10_Coupon_code):
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Flat10_Coupon_code)
                time.sleep(3)
                self.actions.click_button(*locators["OFFER_SERCHBAR"])
                print("Entered a flat10 coupon code and hit search button")

        def verify_flat10_offer_card_visible(self):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['FLAT10_COUPON_CODE'])
                print("Flat10 offercard should visible")
                self.driver.back()
                time.sleep(1)
                self.driver.back()
                time.sleep(1)
                self.driver.back()

        def verify_offer_card_displays_correctly(self):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['FLAT10_COUPON_CODE'])
                print("Freedelivery coupon code is displayed")
                self.actions.is_element_displayed(*locators['COUPON_DESCRIPTION'])
                print("Coupon description is displayed")
                self.actions.is_element_displayed(*locators['SHOW_MORE'])
                print("Show more link is displayed")
                self.actions.is_element_displayed(*locators['APPLY_BUTTON'])
                print("Apply button is displayed")
                self.driver.back()
                time.sleep(1)
                self.driver.back()
                time.sleep(1)
                self.driver.back()

        def enter_Flat10_coupon_code_click_apply_button(self, Flat10_Coupon_code):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Flat10_Coupon_code)
                print("Entered a flat10 coupon code and hit search button")
                time.sleep(3)
                self.actions.click_button(*locators['APPLY_BUTTON'])
                print("Apply button is clicked")
                time.sleep(1)
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Clicked 'Ok button")

        def enter_Flat10_coupon_code(self, Flat10_Coupon_code):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Flat10_Coupon_code)
                print("Entered a flat10 coupon code and hit search button")
                time.sleep(3)
                self.actions.click_button(*locators['APPLY_BUTTON'])
                print("Apply button is clicked")

        def verify_coupon_restriction_message(self):
                time.sleep(3)
                self.actions.is_element_displayed(*locators['PROMO_HEADLINE'])
                print("promo not applied message is displayed")
                time.sleep(2)
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Clicked 'Ok button")
                time.sleep(2)
                self.driver.back()
                time.sleep(1)
                self.driver.back()

        def verify_offers_screen_is_diplayed(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFERS_PAGE'])
                print("ALL available offers is displayed")

        def verify_all_buttons_are_functional_and_displays_correctly(self,Flat10_Coupon_code ):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Flat10_Coupon_code)
                time.sleep(3)
                self.actions.click_button(*locators["OFFER_SERCHBAR"])
                print("Entered a flat10 coupon code and hit search button")
                self.actions.is_element_displayed(*locators['FLAT10_COUPON_CODE'])
                print("Freedelivery coupon code is displayed")
                self.actions.is_element_displayed(*locators['COUPON_DESCRIPTION'])
                print("Coupon description is displayed")
                self.actions.is_element_displayed(*locators['SHOW_MORE'])
                print("Show more link is displayed")
                self.actions.is_element_displayed(*locators['APPLY_BUTTON'])
                print("Apply button is displayed")   
                time.sleep(3)
                self.actions.click_button(*locators["APPLY_BUTTON"])
                print("Entered coupon code and clicked apply button")
                self.actions.is_element_displayed(*locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                time.sleep(2)
                self.actions.click_button(*locators["SUCCESS_MESSAGE_OK_BUTTON"])
                self.driver.back()
                time.sleep(1)
                self.driver.back()
                time.sleep(1)
                self.driver.back() 

        def verify_offers_page_should_be_scrollable_if_many_offer_exists(self):
                time.sleep(5)

                try:
                        # Use UiScrollable to scroll until the element is visible
                        self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true))'
                        '.scrollIntoView(new UiSelector().textContains("Freedelivery+Free product"));'
                        )

                        # Verify element is displayed
                        self.actions.is_element_displayed(*locators['FREEDELIVERY_FREEPRODUCT_COUPON_CODE'])
                        print("Freedelivery+Free product coupon code is displayed")

                except Exception as e:
                        raise AssertionError(f"Unable to find or scroll to Freedelivery+Free product coupon code. Error: {e}")
                
                self.driver.back()
                time.sleep(1)
                self.driver.back()


