from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "MENU_TITLE": (By.XPATH, "//h4[@class='menu__title']"),
        "PRODUCT_PRIZE": (By.XPATH, "(//span[@class='menu__price']//span[@style='font-size: 1.8rem;'])[1]"),
        "GST": (By.XPATH, "//h2[contains(text(), 'GST')]")
    }


class ViewCartPage(BasePage):

    def verify_product_displayed_in_cart_with_price_and_without_gst(self):
        time.sleep(5)
        Menu_Name = "Mexican McAloo Tikki Burger with Cheese Combo"
        Product_Name = self.actions.wait_for_elements(*locators['MENU_TITLE'])
        for product in Product_Name:
            text = product.get_attribute("textContent").strip()
            if Menu_Name in text:
                Price = self.actions.is_element_displayed(*locators["PRODUCT_PRIZE"])
                if Price:
                    return not self.actions.is_element_displayed(*locators["GST"])
                else:
                    print("Price Is Not Displayed In Cart")
                    return False
            else:
                print("Product Is Not Found In View Cart")
                return False
    