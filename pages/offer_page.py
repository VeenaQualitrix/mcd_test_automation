from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
        "OFFERS_PAGE": (By.XPATH, "   //h1[contains(text(), 'Offers For You')]"),
        "FREE_DELIVERY199_OFFER": (By.XPATH, "//div[contains(@class, 'offer-card__card-layout')][.//span[contains(text(), 'freedelivery@199')]]//button[contains(text(), 'Apply')]"),
        "FREE_PRODUCT_OFFER": (By.XPATH, "//div[contains(@class, 'offer-card__card-layout')][.//span[contains(text(), 'Freedelivery+Free product')]]//button[contains(text(),'Apply')]"),
        "REMOVE_OFFER": (By.XPATH, "//div[contains(@class, 'offer-card__card-layout')][.//span[normalize-space(.)='ITEM_Flat 100']]//button[normalize-space(.)='Remove']"),
        "OFFER_APPLIED_SUCCESS_MESSAGE": (By.XPATH, "//div[contains(text(), 'Promo Applied Successfully')]"),
        "SUCCESS_MESSAGE_OK_BUTTON": (By.XPATH, "//button//span[text()='OK']"),
        "OFFER_SERCHBAR": (By.XPATH, "//input[@placeholder = 'Enter Coupon Code']"),
        "FLAT10_COUPON_CODE": (By.XPATH, "//div[contains(text(), ' FLAT 10 OFF ')]"),
        "FREEDELIVERY_COUPON_CODE": (By.XPATH, "(//span[contains(text(), 'freedelivery@199')])[2]"),
        "COUPON_DESCRIPTION": (By.XPATH, "(//p[contains(text(), 'Freedelivery')])[2]"),
        "SHOW_MORE": (By.XPATH, "//span[contains(text(),'Show More ')]"),
        "APPLY_BUTTON": (By.XPATH, "//button[contains(text(),'Apply')]"),
        "COUPON_RESTRICTION_MSG": (By.XPATH, "//h2[contains(text(), 'Promo Not Applied')]"),
        "FLAT10_APPLY_BUTTON": (By.XPATH, "(//button[contains(text(),'Apply')])[1]"),
}

class OfferPage(BasePage):


        def verify_user_redirected_to_offers_page(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFERS_PAGE'])
                print("ALL available offers is displayed")

        def Select_first_promo_code(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['FREE_DELIVERY199_OFFER'])
                self.actions.click_button(*locators['FREE_DELIVERY199_OFFER'])
                self.actions.is_element_displayed(*locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Free delivery@199 offer applied")

        def Select_second_promo_code(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['FREE_PRODUCT_OFFER'])
                self.actions.click_button(*locators['FREE_PRODUCT_OFFER'])
                self.actions.is_element_displayed(*locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Free product offer applied")

        def Select_remove_applied_offer(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['REMOVE_OFFER'])
                self.actions.click_button(*locators['REMOVE_OFFER'])
                print("Remove applied offer")
                time.sleep(3)
                self.driver.back()

        def verify_input_box_for_entering_coupon_code_visible_and_functional(self, Coupon_code):
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Coupon_code)
                time.sleep(3)
                self.actions.click_button(*locators["OFFER_SERCHBAR"])
                print("Input box for entering coupon code is visible and functional")

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

        def verify_offer_card_displays_correctly(self):
                self.actions.is_element_displayed(*locators['FREEDELIVERY_COUPON_CODE'])
                print("Freedelivery coupon code is displayed")
                self.actions.is_element_displayed(*locators['COUPON_DESCRIPTION'])
                print("Coupon description is displayed")
                self.actions.is_element_displayed(*locators['SHOW_MORE'])
                print("Show more link is displayed")
                self.actions.is_element_displayed(*locators['APPLY_BUTTON'])
                print("Apply button is displayed")

        def enter_coupon_code_and_click_apply_button(self):
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], 'freedelivery@199')
                time.sleep(3)
                self.actions.click_button(*locators["APPLY_BUTTON"])
                print("Entered coupon code and clicked apply button")
                self.actions.is_element_displayed(*locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
                time.sleep(2)
                self.actions.click_button(*locators["SUCCESS_MESSAGE_OK_BUTTON"])

        def enter_Flat10_coupon_code_click_apply_button(self, Flat10_Coupon_code):
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], Flat10_Coupon_code)
                print("Entered a flat10 coupon code and hit search button")
                time.sleep(3)
                self.actions.click_button(*locators['FLAT10_APPLY_BUTTON'])
                print("Apply button is clicked")

        def verify_coupon_restriction_message(self):
                self.actions.is_element_displayed(*locators['COUPON_RESTRICTION_MSG'])
                print("promo not applied message is displayed")
                time.sleep(2)
                self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
                print("Clicked 'Ok button")
                time.sleep(2)
                self.driver.back()
                time.sleep(3)
                self.Clear_all()

        def verify_offers_page_should_be_scrollable_if_many_offer_exists(self):
                time.sleep(5)
                Multiple_offers = self.driver.find_element(*locators["FLAT10_COUPON_CODE"])
                self.driver.execute_script("arguments[0].scrollIntoView();", Multiple_offers)
                self.actions.is_element_displayed(*locators['FLAT10_COUPON_CODE'])
                print("Flat10 coupon code is displayed")

        def window_resize(self):
                self.driver.set_window_size(800, 600)
                print("Window resized to 800x600")
                time.sleep(2)

        def verify_all_buttons_are_functional_and_displays_correctly(self):
                time.sleep(5)
                self.actions.is_element_displayed(*locators['OFFER_SERCHBAR'])
                self.actions.enter_text(*locators["OFFER_SERCHBAR"], 'freedelivery@199')
                time.sleep(3)
                self.actions.is_element_displayed(*locators['FREEDELIVERY_COUPON_CODE'])
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
                time.sleep(2)
                self.driver.back()
                time.sleep(3)
                self.Clear_all()  
                