from conftest import setup_platform
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.view_cart_page import ViewCartPage
import time

locators = {
        "JUSPAY_PAGE_VERIFICATION": (By.XPATH, "//img[@alt='juspay brand']"),
        "COD_PAYMENT_MODE": (By.XPATH, "//article[text()='Cash On Delivery']"),
        "COD_PAYMENT_MODE_SELECTED": (By.XPATH, "(//article[text()='Cash On Delivery'])[4]"),
        "PROCEED_TO_PAY_BUTTON": (By.XPATH, "//article[text()='Proceed to Pay']"),
        "ORDER_PLACED_SUCCESS_MESSAGE": (By.XPATH, "//span[contains(text(), 'Yayy Your Order is  Placed!')]"),
        "UPI_PAYMENT": (By.XPATH, "//div[@testid = 'nvb_upi']"),
        "CARD_PAYMENT": (By.XPATH, "//div[@testid = 'nvb_card']"),
        "NET_BANKING_PAYMENT": (By.XPATH, "//div[@testid = 'nvb_net_banking']"),
        "COD_PAYMENT": (By.XPATH, "//div[@testid = 'nvb_cod']"),
        "PLUXEE_PAYMENT": (By.XPATH, "//div[@testid = 'nvb_food_card']"),
        "UPI_ID_TEXT_SHOW": (By.XPATH, "//article[contains(text(), 'UPI ID')]"),
        "UPI_TEXT_FIELD": (By.XPATH, "//input[@placeholder = 'Username@bankname']"),
        "UPI_PAY_BUTTON": (By.XPATH, "//div[@aria-label = 'Verify and Pay']"),
        "INVALID_UPI_MSG": (By.XPATH, "//article[contains(text(), 'Invalid UPI ID')]"),
        "ENTER_CREDIT_DEBIT_CARD_DETAILS_TEXT": (By.XPATH, "//article[contains(text(), 'Enter Credit / Debit card details')]"),
        "CARD_NUMBER_TEXT": (By.XPATH, "//article[contains(text(), 'Card number')]"),
        "CARD_NUMBER_INPUT_FIELD": (By.XPATH, "//input[@placeholder = 'Enter Card Number']"),
        "EXPIRY_INPUT_FIELD": (By.XPATH, "//input[@placeholder = 'MM/YY']"),
        "CARD_NUMBER_VALIDATION_MSG": (By.XPATH, "//article[contains(text(), 'Recheck the card number')]"),
        "COD_TEXT": (By.XPATH, "(//article[contains(text(), 'Cash On Delivery')])[3]"),
        "COD_CHECKED": (By.XPATH, "//img[@aria-checked = 'true']"),
        "SECURE_PAYMENT_LABEL": (By.XPATH, "//img[@alt = 'juspay brand']"),
    }


class JuspayPage(BasePage):

    def verify_juspay_page_is_reached(self):
        time.sleep(10)
        return self.actions.is_element_displayed(*locators['JUSPAY_PAGE_VERIFICATION'])
        
    def select_payment_method(self):
        self.actions.click_button(*locators["COD_PAYMENT_MODE"])
        print("Clicked On Cash On Delivery Payment Method")

    def verify_selected_payment_method_is_displayed(self):
        return self.actions.is_element_displayed(*locators["COD_PAYMENT_MODE_SELECTED"])
    
    def click_on_proceed_to_pay(self):
        self.actions.click_button(*locators["PROCEED_TO_PAY_BUTTON"])
        print("Clicked On Proceed To Pay Button")
        time.sleep(10)

    def verify_order_placed_success_message(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators["ORDER_PLACED_SUCCESS_MESSAGE"])
    
    def verify_all_supported_payment_method_is_displayed(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["UPI_PAYMENT"])
        print("UPI payment method is displayed")
        self.actions.is_element_displayed(*locators["CARD_PAYMENT"])
        print("Card payment method is displayed")
        self.actions.is_element_displayed(*locators["NET_BANKING_PAYMENT"])
        print("Net Banking payment method is displayed")
        self.actions.is_element_displayed(*locators["COD_PAYMENT"])
        print("Cash on Delivery payment method is displayed")
        self.actions.is_element_displayed(*locators["PLUXEE_PAYMENT"])
        print("Pluxee payment method is displayed")
        time.sleep(2)  
        self.driver.back()
        time.sleep(3) 
        # call method 
        view_cart = ViewCartPage(self.driver)
        view_cart.Clear_all()

    def select_upi_payment_method(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["UPI_PAYMENT"])
        self.actions.click_button(*locators["UPI_PAYMENT"])
        print("Clicked On UPI payment method")

    def enter_invalid_upi_id(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["UPI_ID_TEXT_SHOW"])
        print("UPI ID text is displayed") 
        self.actions.enter_text(*locators['UPI_TEXT_FIELD'], "test@ybl")
        print("Entered invlaid UPI id in text field")
        time.sleep(3) 
        self.actions.click_button(*locators["UPI_PAY_BUTTON"])
        print("Clicked On UPI pay button")

    def verify_invalid_upi_error_message(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["INVALID_UPI_MSG"])
        print("Invalid UPI ID message is displayed")
        time.sleep(2) 
        self.driver.back()
        time.sleep(3) 
        # call method 
        view_cart = ViewCartPage(self.driver)
        view_cart.Clear_all()

    def select_card_payment_method(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["CARD_PAYMENT"])
        self.actions.click_button(*locators["CARD_PAYMENT"])
        print("Clicked On Credit/Debit card payment method")

    def enter_invalid_card_details(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["ENTER_CREDIT_DEBIT_CARD_DETAILS_TEXT"])
        print("Enter credit/debit card details text is displayed") 
        self.actions.is_element_displayed(*locators["CARD_NUMBER_TEXT"])
        print("card number text is displayed") 
        self.actions.enter_text(*locators['CARD_NUMBER_INPUT_FIELD'], "1234 5678 1234 5678 1234")
        print("Entered invalid card details in text field")
        time.sleep(3) 
        self.actions.click_button(*locators["EXPIRY_INPUT_FIELD"])
        print("Clicked On expiry input field")

    def verify_invalid_card_number_message(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["CARD_NUMBER_VALIDATION_MSG"])
        print("Invalid card number message is displayed")
        time.sleep(2) 
        self.driver.back()
        time.sleep(3) 
        # call method 
        view_cart = ViewCartPage(self.driver)
        view_cart.Clear_all()

    def click_back_button_from_payment_page(self):
        time.sleep(2) 
        self.driver.back()
        print("Clicked browser back button")

    def select_cod_payment_method(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["COD_PAYMENT"])
        self.actions.click_button(*locators["COD_PAYMENT"])
        print("Clicked On cash on delivery payment method")

    def click_proceed_to_pay_button(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["COD_TEXT"])
        print("Cash on delivery text is displayed")
        self.actions.is_element_displayed(*locators["COD_CHECKED"])
        print("COD checkbox is checked")
        self.actions.click_button(*locators["PROCEED_TO_PAY_BUTTON"])
        print("Clicked On Proceed to pay button")

    def verify_secure_payment_label(self):
        time.sleep(5)  
        self.actions.is_element_displayed(*locators["SECURE_PAYMENT_LABEL"])
        print("secured by 'JUSPAY' is displayed")
        time.sleep(2) 
        self.driver.back()
        time.sleep(3) 
        # call method 
        view_cart = ViewCartPage(self.driver)
        view_cart.Clear_all()
        
        

