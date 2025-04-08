from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "MENU_TITLE": (By.XPATH, "//h4[@class='menu__title']"),
        "PRODUCT_PRIZE": (By.XPATH, "(//span[@class='menu__price']//span[@style='font-size: 1.8rem;'])[1]"),
        "GST": (By.XPATH, "//h2[contains(text(), 'GST')]"),
        "OFFER_CARD": (By.XPATH, "//div[@class='offer-card']"),
        "VIEW_ALL": (By.XPATH, "//h3[contains(text(), 'View All')]"),
        "OFFER_NAME": (By.XPATH, "//h2[@class='offer-card__titleText']"),
        "APPLY_OFFER_BUTTON": (By.XPATH, "(//button[text()='Apply'])[1]"),
        "OFFER_APPLIED_SUCCESS_MESSAGE": (By.XPATH, "//div[contains(text(), 'Promo Applied Successfully')]"),
        "SUCCESS_MESSAGE_OK_BUTTON": (By.XPATH, "//button//span[text()='OK']"),
        "OFFER_APPLIED": (By.XPATH, "//h2[contains(text(), 'Offer Applied')]"),
        "TOTAL_PRICE": (By.XPATH, "//h2[@class='total-charge__totaltext' and contains(text(), '₹')]"),
        "GROSS_PRICE": (By.XPATH, "//button[@class='app-btn primary' and contains(text(), '₹')]")
    }


class ViewCartPage(BasePage):

    def verify_product_displayed_in_cart_with_price_and_without_gst(self):
        time.sleep(5)
        Menu_Name = "Mexican McAloo Tikki Burger with Cheese Combo"
        Product_Name = self.actions.wait_for_elements(*locators['MENU_TITLE'])
        for product in Product_Name:
            text = product.get_attribute("textContent").strip()
            if Menu_Name in text:
                Price = self.actions.wait_for_element(*locators["PRODUCT_PRIZE"])
                print(Price)
                if Price:
                    price_value = self.actions.get_text(*locators['PRODUCT_PRIZE'])
                    print(price_value)
                    if "GST" not in price_value:
                        return True
                    else:
                        return False
                else:
                    print("Price Is Not Displayed In Cart")
                    return False
            else:
                print("Product Is Not Found In View Cart")
                return False
    
    def select_offer(self):
        Offers_Available = self.actions.wait_for_elements(*locators['OFFER_CARD'])
        print("Nuumber of Offers Card Available For The Selected Product : " + str(len(Offers_Available)))
        self.actions.click_button(*locators["VIEW_ALL"])
        time.sleep(3)
        # Offer_To_Select = "McAloo tikki Burger+ Veg Pizza McPuff+ Piri Piri Spice Mix on MOV of 199"
        # Offer_Name = self.actions.wait_for_elements(*locators['OFFER_NAME'])
        # for index, offer in enumerate(Offer_Name):
        #     text = offer.get_attribute("textContent").strip()
        #     index = index + 1
        #     if Offer_To_Select in text:
        #         self.actions.click_button(locators["APPLY_OFFER_BUTTON"][0], locators["APPLY_OFFER_BUTTON"][1].format(str(index)))
        #         break
        self.actions.click_button(*locators['APPLY_OFFER_BUTTON'])
        success_message = self.actions.is_element_displayed(*locators['OFFER_APPLIED_SUCCESS_MESSAGE'])
        print(success_message)
        if success_message:
            self.actions.click_button(*locators['SUCCESS_MESSAGE_OK_BUTTON'])
        else:
            print("Offer Is Not Apllied For Selected Product")
        time.sleep(10)

    def verify_offer_applied_for_the_selected_product(self):
        return self.actions.is_element_displayed(*locators['OFFER_APPLIED'])
    
    def verify_gross_price_and_total_price_are_same(self):
        Total_Price = self.actions.wait_for_element(*locators['TOTAL_PRICE'])
        Gross_Price = self.actions.wait_for_element(*locators["GROSS_PRICE"])
        if Total_Price and Gross_Price:
            total_price_value = Total_Price.get_attribute("textContent").strip()
            gross_price_value = Gross_Price.get_attribute("textContent").strip()
            print(total_price_value)
            print(gross_price_value)
            gross_price_value = gross_price_value.replace("Pay ", "")
            print(gross_price_value)
            if total_price_value == gross_price_value:
                return True
            else:
                print("Total price and Gross price is not same")
                return False
        else:
            print("Total Price and Gross Price is not displayed")
            return False
        
    def click_on_pay_button_in_view_cart_page(self):
        self.actions.click_button(*locators['GROSS_PRICE'])
        print("Clicked on pay button in view cart page")
