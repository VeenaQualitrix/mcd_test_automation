from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "HEADER_BANNER": (By.XPATH, "//ion-header[@role='banner']"),
        "VIEW_ICON": (By.XPATH, "//div[@title='View Profile']"),
        "ADDRESS_DROPDOWN": (By.XPATH, "(//div[@class='toolbar-v1__location-type txt-ellipsis']/img[@title='ic-arrow-down'])[1]"),
        "NEARBY_RESTAURANTS": (By.XPATH, '//span[contains(@class, "toolbar-desktop__menu") and contains(text(), "Restaurants Nearby")]'),
        "NEAR_ME_STORES": (By.XPATH, "//div[@class='near-me__store']"),
        "3_PC_MEALS": (By.XPATH, "//img[@title='Burger Combos ( 3 Pc Meals )']"),
        "MENU_TITLE": (By.XPATH, "//h4[@class='menu__title']"),
        "ADD_TO_CART_BUTTON": (By.XPATH, "(//div[text()=' Add '])[{}]"),
        "CONFIRM_ADD_TO_CART": (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
        "CART_LIST": (By.XPATH, "//div[@class='cart-details__card-list']"),
        "VIEW_CART": (By.XPATH, "//div[@class='cart-status-bar__cta' and contains(text(), 'View Cart')]")
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
        print("CLicked on add address dropdown")

    def click_on_restaurants_nearby(self):
        self.actions.click_button(*locators['NEARBY_RESTAURANTS'])
        print("CLicked on add address dropdown")

    def verify_nearby_restaurants_are_displayed(self):
        near_me_stores = self.actions.wait_for_elements(*locators['NEAR_ME_STORES'])
        if near_me_stores is not None:
            print("Number of Stores Near Selected Location : " + str(len(near_me_stores)))
            time.sleep(5)
            return True
        else:
            return False
        
    def add_multiple_product_with_customization_and_coke_convergence(self):
        time.sleep(5)
        Three_Pc_Meals = self.driver.find_element(*locators["3_PC_MEALS"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Three_Pc_Meals)
        Three_Pc_Meals.click()
        time.sleep(5)
        Menu_Name = "Mexican McAloo Tikki Burger with Cheese Combo"
        Product_Name = self.actions.wait_for_elements(*locators['MENU_TITLE'])
        for index, product in enumerate(Product_Name):
            text = product.get_attribute("textContent").strip()
            index = index + 1
            print(text)
            if Menu_Name in text:
                for i in range(10):
                    Add_Cart = self.driver.find_element(locators["ADD_TO_CART_BUTTON"][0], locators["ADD_TO_CART_BUTTON"][1].format(str(index)))
                    print(Add_Cart)
                    try:
                        Add_Cart.click()
                        print("Product Clicked")
                        break
                    except Exception:
                        self.driver.execute_script("arguments[0].scrollIntoView();", Add_Cart)
        time.sleep(2)
        self.actions.click_button(*locators['CONFIRM_ADD_TO_CART'])
        time.sleep(5)

    def verify_product_added_in_cart(self):
        return self.actions.is_element_displayed(*locators['CART_LIST'])
    
    def click_on_view_cart(self):
        self.actions.click_button(*locators['VIEW_CART'])
        print("Clicked on View Cart Button")
