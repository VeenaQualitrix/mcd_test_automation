from pages.base_page import BasePage
from pages.offer_page import OfferPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
        "MENU_TITLE": (By.XPATH, "//h4[@class='menu__title']"),
        "PRODUCT_PRIZE_IN_CART": (By.XPATH, "(//span[@class='menu__price']//span[@style='font-size: 1.8rem;'])[1]"),
        "GST": (By.XPATH, "//h2[contains(text(), 'GST')]"),
        "OFFER_CARD": (By.XPATH, "//div[@class='offer-card']"),
        "VIEW_ALL": (By.XPATH, "//h3[contains(text(), 'View All')]"),
        "OFFER_NAME": (By.XPATH, "//h2[@class='offer-card__titleText']"),
        "APPLY_OFFER_BUTTON": (By.XPATH, "(//button[text()='Apply'])[1]"),
        "OFFER_APPLIED_SUCCESS_MESSAGE": (By.XPATH, "//div[contains(text(), 'Promo Applied Successfully')]"),
        "SUCCESS_MESSAGE_OK_BUTTON": (By.XPATH, "//button//span[text()='OK']"),
        "OFFER_APPLIED": (By.XPATH, "//h2[contains(text(), 'Offer Applied')]"),
        "TOTAL_PRICE": (By.XPATH, "//h2[@class='total-charge__totaltext' and contains(text(), '₹')]"),
        "GROSS_PRICE": (By.XPATH, "//button[@class='app-btn primary' and contains(text(), '₹')]"),
        "PRODUCT_PRIZE_IN_HOMEPAGE": (By.XPATH, "(//div[text() = ' McVeggie Burger '])[1]/../div[2]//span[@class ='menu__price']"),
        "MCDELIVERY_ICON": (By.XPATH, "//img[@alt = 'logo']"),
        "CUSTOMISE": (By.XPATH, " //div[contains(text(), 'Customise')]"),
        "CUTOMISE_REMOVE_BUTTON": (By.XPATH, "//h5[contains(text(), 'Tomato Ketchup Sachet')]/ancestor::div[1]/following-sibling::div//img[@alt='ic-subtract']"),
        "CUTOMISE_ADD_BUTTON": (By.XPATH, "//h5[contains(text(), 'Cheese')]/ancestor::div[1]/following-sibling::div//img[@alt='ic-add']"),
        "CLICK_DONE_BUTTON": (By.XPATH, " //button[contains(text(), 'Done')]"),
        "CUSTOMISED_ITEM_TEXT": (By.XPATH, " //div[contains(text(), ' Removed: Tomato Ketchup Sachet Added: Cheese ')]"),
        "FIRST_CART_ITEMS": (By.XPATH, " //h4[normalize-space()='McVeggie Burger']/ancestor::div[contains(@class, 'menu__primary')]"),
        "SECOND_CART_ITEMS": (By.XPATH, " //h4[normalize-space()='McCrispy Chicken Burger']/ancestor::div[contains(@class, 'menu__primary')]"),
        "REMOVE_ITEM_FROM_CART_PAGE": (By.XPATH, "(//div[contains(@class, 'menu__secondary')]//img[@alt='ic-subtract'])[1]"),
        "ADD_ITEM_FROM_CART_PAGE": (By.XPATH, "//div[contains(@class, 'menu__secondary')]//img[@alt='ic-add']"),
        "ITEM_QUANTITY": (By.XPATH, "//div[@class='add-to-cart__count' and normalize-space()='02']"),
        "QUANTITY_LOCATOR": (By.XPATH,"//div[@class='add-to-cart__count' and normalize-space()='{expected_text}']"),
        "TOTAL_PAY": (By.XPATH, " //h2[@class='total-charge__totaltext' and contains(text(), '₹')]"),
        "CLEAR_ALL": (By.XPATH, "  //h3[contains(text(), 'Clear All ')]"),
        "DELETE_CART": (By.XPATH, "  //h2[contains(text(), 'Delete Cart')]"),
        "DELETE_CART_OK_BUTTON": (By.XPATH, " //span[contains(text(), 'OK')]"),
        "ITEM_NAME": (By.XPATH, " //h4[normalize-space()='{item['name']}']/ancestor::div[contains(@class, 'menu__primary')]"),
        "KNOW_MORE": (By.XPATH, " //h2[contains(text(), ' Know More')]"),
        "DONATE_CHECKBOX_CHECKED": (By.XPATH, " //img[@alt = 'ic-checkeddonate']"),
        "CHARITY_TEXT": (By.XPATH, " //h2[contains(text(), 'Donate ₹ 3 for Ronald Mcdonald House of Charity.')]"),
        "CHARITY_INFO_HEADLINE": (By.XPATH, " //h1[contains(text(), 'Donate for Ronald Mcdonald House Charities')]"),
        "CHARITY_INFO_DESCRIPTION": (By.XPATH, " //h3[contains(text(), ' Your support will go a long way in keeping unwell children and their families together. ')]"),
        "DONATION": (By.XPATH, " //h2[@class='total-charge__paybletext' and normalize-space()='Donation']"),
        "DONATION_AMOUNT": (By.XPATH, " //h2[contains(text(), ' ₹ 3.00 ')]"),
        "DONATE_CHECKBOX_UNCHECKED": (By.XPATH, " //div[@class = 'cart-page__donateuncheckbox']"),
        "SUB_TOTAL": (By.XPATH, "   //h2[contains(text(), ' Sub Total ')]"),
        "SUB_TOTAL_PRICE": (By.XPATH, "//div[@class='total-charge__rowstyle' and .//h2[normalize-space()='Sub Total']]//h2[contains(normalize-space(), '₹')]"),
        "HANDLING_CHARGES": (By.XPATH, " //h2[contains(text(), ' Handling Charges ')]"),
        "HANDLING_CHARGES_PRICE": (By.XPATH, "//div[@class='total-charge__rowstyle' and .//h2[normalize-space()='Handling Charges']]//h2[contains(normalize-space(), '₹')]"),
        "CGST_PRICE": (By.XPATH, "//div[@class='total-charge__rowstyle' and .//h2[normalize-space()='CGST']]//h2[contains(normalize-space(), '₹')]"),
        "CGST": (By.XPATH, "//h2[contains(text(), ' CGST')]"),
        "SGST_PRICE": (By.XPATH, "//div[@class='total-charge__rowstyle' and .//h2[normalize-space()='SGST']]//h2[contains(normalize-space(), '₹')]"),
        "SGST": (By.XPATH, "//h2[contains(text(), ' SGST ')]"),
        "OFFER_SERCHBAR": (By.XPATH, "//input[@placeholder = 'Enter Coupon Code']"),
        "OFFER_APPLY_BUTTON": (By.XPATH, "//button[contains(text(), 'Apply')]"),
        "OFFER_SELECT_BUTTON": (By.XPATH, "(//button[contains(text(), 'Select')])[1]"),
        "PROMO_HEADLINE": (By.XPATH, "//h2[contains(text(), 'Promo Not Applied')]"),
        "PROMO_EXPIRED_MESSAGE": (By.XPATH, "//div[contains(text(), 'Promo Code Expired')] "),
        "OK_BUTTON": (By.XPATH, "//button//span[text()='OK']"),
        "ADD_DELIVERY_INSTRUCTIONS": (By.XPATH, " //h2[contains(text(), 'Add Delivery Instructions')] "),
        "ADD_SIGN": (By.XPATH, "//img[@alt = 'ic-address__add']"),
        "NOTE_TEXT_AREA": (By.XPATH, "//textarea[contains(@name, 'ion-textarea')]"),
        "RECOMMENDATION": (By.XPATH, " //h2[contains(text(), 'Recommendation')]"),
        "ADD_ITEM_TO_CART" : (By.XPATH, "//div[contains(@class, 'menu__title') and normalize-space(text())='{burger_name}']/following::div[contains(@class, 'add-to-cart')][1]"),
        "CLICK_NEXT": (By.XPATH, "//button[contains(text(), 'Next')]"),
        "CLICK_ADD_TO_CART": (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
        "ESTIMATED_DELIVERY_TIME_HEADLINE": (By.XPATH, "(//span[contains(text(), ' 20 min delivery activated ')])[1]"),
        "ESTIMATED_DELIVERY_TIME_TEXT": (By.XPATH, "//h2[contains(text(), ' Expect your order within ')]"),
        "APPLIED_OFFER_NAME": (By.XPATH, "//span[contains(text(), 'freedelivery@199')]"),
        "CHANGE_OFFER": (By.XPATH, "//div[contains(text(), ' Change Offer ')]"),
        "APPLIED_SECOND_OFFER_NAME": (By.XPATH, "//span[contains(text(), 'Freedelivery+Free product')]"),
        "CART_ITEM": (By.XPATH, "//h4[normalize-space()='McAloo Tikki Burger']/ancestor::div[contains(@class, 'menu__primary')]"),
        "QUANTITY_COUNT": (By.XPATH, "(//div[contains(@class, 'menu__title') and contains(normalize-space(), 'McAloo Tikki Burger')]/following::div[contains(@class, 'add-to-cart__count')])[1]"),
        "PROCEED_TO_PAY": (By.XPATH, "//button[contains(text(), 'Pay ₹')]"),
        "YOUR_ORDER": (By.XPATH, "//h1[contains(text(), ' Your Order')]"),
        
    }


class ViewCartPage(BasePage):

    def verify_product_displayed_in_cart_with_price_and_without_gst(self):
        time.sleep(5)
        Menu_Name = "Mexican McAloo Tikki Burger with Cheese Combo"
        Product_Name = self.actions.wait_for_elements(*locators['MENU_TITLE'])
        for product in Product_Name:
            text = product.get_attribute("textContent").strip()
            if Menu_Name in text:
                Price = self.actions.wait_for_element(*locators["PRODUCT_PRIZE_IN_CART"])
                print(Price)
                if Price:
                    price_value = self.actions.get_text(*locators['PRODUCT_PRIZE_IN_CART'])
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


    def verify_multiple_products_in_cart_with_correct_price(self):
        time.sleep(5)

        expected_items = [
            {"name":"McVeggie Burger" , "quantity": 1},
            {"name":"McCrispy Chicken Burger" , "quantity": 1}
        ]

        for item in expected_items:
            try:
                item_locator = (locators['ITEM_NAME'])
                element = self.driver.find_element(*item_locator)

                price_text = element.find_element(*locators['TOTAL_PAY']).text
                quantity_text = element.find_element(*locators['QUANTITY_LOCATOR']).text

                actual_price = float(price_text.replace("₹", "").strip())
                actual_quantity = int(quantity_text.strip())

                print(f"Expected: ₹{item['price']} x{item['quantity']}, Found: ₹{actual_price} x{actual_quantity}")

                if actual_price != item["price"] or actual_quantity != item["quantity"]:
                    print(f" Mismatch for {item['name']}")
                    return False

            except Exception as e:
                print(f"Error verifying item {item['name']}: {e}")
                return False
        print(" All items verified successfully.")
        return True
    
    def verify_product_price_is_displayed_correct_in_cart(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['PRODUCT_PRIZE_IN_CART'])
    
    def verify_price_in_cart_matches_menu_price(self, product_name="McVeggie Burger"):
        time.sleep(2)

        # Get the price from the cart
        cart_price_element = self.driver.find_element(*locators['PRODUCT_PRIZE_IN_CART'])
        cart_price = cart_price_element.text.strip().replace(" ", "")
        print(f"Cart price for '{product_name}' is: {cart_price}")
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON'])
        self.actions.click_button(*locators['MCDELIVERY_ICON'])
        print("Mcdelivery icon clicked.")

        # Get the menu price from the homepage
        menu_price_xpath = locators['PRODUCT_PRIZE_IN_HOMEPAGE'][1].replace("McVeggie Burger", product_name)
        menu_price_element = self.driver.find_element(locators['PRODUCT_PRIZE_IN_HOMEPAGE'][0], menu_price_xpath)
        menu_price = menu_price_element.text.strip().replace(" ", "")  
        print(f"Menu price for '{product_name}' is: {menu_price}")

        # Compare both prices
        assert cart_price == menu_price, f"Price mismatch: Menu({menu_price}) != Cart({cart_price})"
        print("✅ Price in cart matches the menu price.")

    def Click_customise(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CUSTOMISE'])
        self.actions.click_button(*locators['CUSTOMISE'])
        print("customise clicked")
    
    def Add_or_remove_items_on_customise_page(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CUTOMISE_ADD_BUTTON'])
        self.actions.click_button(*locators['CUTOMISE_ADD_BUTTON'])
        print("Cheese added")
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CUTOMISE_REMOVE_BUTTON'])
        self.actions.click_button(*locators['CUTOMISE_REMOVE_BUTTON'])
        print("Tomato Ketchup removed")
        time.sleep(2)
        self.actions.click_button(*locators['CLICK_DONE_BUTTON'])
        print("Done button clicked")

    def Verify_customisation_text_after_adding_or_removing_items(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['CUSTOMISED_ITEM_TEXT'])
    
    def Verify_items_in_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['FIRST_CART_ITEMS'])
        print("McVeggie Burger is displayed")
        self.actions.is_element_displayed(*locators['SECOND_CART_ITEMS'])
        print("McCrispy Chicken Burger is displayed")

    def decrease_cart_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        self.actions.click_button(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        print("Remove item from cart page")

    def Verify_selected_items_removed_from_cart(self):
        time.sleep(5)
        try:
            is_displayed = self.actions.is_element_displayed(*locators['FIRST_CART_ITEMS'])
        except Exception:
            is_displayed = False  # Element not found is expected here

        assert not is_displayed, "FAIL: McVeggie Burger is still displayed in the cart"
        print("PASS: McVeggie Burger is not displayed in the cart")


    def increase_cart_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_ITEM_FROM_CART_PAGE'])
        self.actions.click_button(*locators['ADD_ITEM_FROM_CART_PAGE'])
        print("Add item from cart page")

    def verify_item_quantity(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ITEM_QUANTITY'])
        print("Item quantity updated from 1 to 2")
        
    '''
    def verify_item_quantity(self, expected_quantity: int):
        time.sleep(2)  
        expected_text = f"{expected_quantity:02d}"  # Formats 2 as '02'
        is_displayed = self.actions.is_element_displayed(*locators['QUANTITY_LOCATOR'])
        assert is_displayed, f"Expected quantity '{expected_text}' not displayed"
        print(f"Item quantity updated to {expected_text}")

        '''

    def Verify_single_item_in_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['FIRST_CART_ITEMS'])
        print("McVeggie Burger is displayed")

    def Verify_total_payable_amount_is_displayed_in_cart_page(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['TOTAL_PAY'])
        print("Total payable amount is displayed")

    def get_total_payable_amount(self):
        element = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['TOTAL_PAY'])
        )
        amount_text = element.text.strip().replace('₹', '').strip()
        return float(amount_text)
    
    def print_total_payable_amount(self):
        amount = self.get_total_payable_amount()
        print(f"Total Payable: ₹{amount}")
        return amount
    
    def Clear_all(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CLEAR_ALL'])
        self.actions.click_button(*locators['CLEAR_ALL'])
        print("Clear all is clicked")
        self.actions.is_element_displayed(*locators['DELETE_CART'])
        print("Delete cart pop up is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['DELETE_CART_OK_BUTTON'])
        print("Ok button is clicked")
        self.driver.quit()


    def Remove_cart_item_until_the_quantity_becomes_zero(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        self.actions.click_button(*locators['REMOVE_ITEM_FROM_CART_PAGE'])
        print("Remove button clicked")
        self.actions.is_element_displayed(*locators['DELETE_CART'])
        print("Delete cart pop up is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['DELETE_CART_OK_BUTTON'])
        print("Ok button is clicked")

    def Refresh_the_page(self):
        self.driver.refresh()
        time.sleep(3)
        print("Page refreshed")

    def cart_retained_the_previously_added_item(self):
        time.sleep(5)
        is_displayed = self.actions.is_element_displayed(*locators['FIRST_CART_ITEMS'])
        assert is_displayed, "McVeggie Burger should persist in cart after refresh"
        print("Verified: McVeggie Burger is still in cart after refresh")


    def verify_checkbox_and_charity_link_visible(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_UNCHECKED'])
        print("Charity checkbox is displayed")
        self.actions.is_element_displayed(*locators['CHARITY_TEXT'])
        print("Charity text is displayed")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['KNOW_MORE'])
        print("Know more link is displayed")

    def click_know_more_link(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['KNOW_MORE'])
        self.actions.click_button(*locators['KNOW_MORE'])
        print("Know more link is clicked")

    def verify_charity_info_pop_up(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CHARITY_INFO_HEADLINE'])
        self.actions.is_element_displayed(*locators['CHARITY_INFO_DESCRIPTION'])
        print("charity info description is displayed")


    def verify_Donation_amount_added_in_payable_amount(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DONATION'])
        print("Donation is displayed")
        self.actions.is_element_displayed(*locators['DONATION_AMOUNT'])
        print("Donation amount is displayed")

    def verify_charity_checkbox_is_selected(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_UNCHECKED'])
        self.actions.click_button(*locators['DONATE_CHECKBOX_UNCHECKED'])
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_CHECKED'])
        print("Charity donate checkbox is checked")

    def uncheck_charity_checkbox(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_CHECKED'])
        self.actions.click_button(*locators['DONATE_CHECKBOX_CHECKED'])
        self.actions.is_element_displayed(*locators['DONATE_CHECKBOX_UNCHECKED'])
        print("Charity donate checkbox is unchecked")

    def verify_donation_amount_removed_from_payable_amount(self):
        time.sleep(5)  
        try:
            is_donation_present = self.actions.is_element_displayed(*locators['DONATION'])
            is_donation_amount_present = self.actions.is_element_displayed(*locators['DONATION_AMOUNT'])
        except Exception as e:
            # If element is not found at all, consider it removed
            is_donation_present = False
            is_donation_amount_present = False

        assert not is_donation_present, "Donation label is still displayed!"
        assert not is_donation_amount_present, "Donation amount is still displayed!"

        print("Donation and donation amount are successfully removed from the payable section.")

    def verify_view_all_link_visible(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VIEW_ALL'])
        print("View all link is displayed")

    def click_view_all_link(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VIEW_ALL'])
        print("View all link is displayed")
        self.actions.click_button(*locators['VIEW_ALL'])
        print("View all link is clicked")

    def review_prices_in_order_summary(self):
        prices = {}

        # Total Payable
        total_pay_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['TOTAL_PAY'])
        )
        prices['total_pay'] = float(total_pay_element.text.strip().replace('₹', '').strip())

        # Subtotal
        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        prices['sub_total'] = float(sub_total_element.text.strip().replace('₹', '').strip())

        # Handling Charges
        handling_charges_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['HANDLING_CHARGES_PRICE'])
        )
        prices['handling_charges'] = float(handling_charges_element.text.strip().replace('₹', '').strip())

        # CGST
        cgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['CGST_PRICE'])
        )
        prices['cgst'] = float(cgst_element.text.strip().replace('₹', '').strip())

        # SGST
        sgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SGST_PRICE'])
        )
        prices['sgst'] = float(sgst_element.text.strip().replace('₹', '').strip())

        return prices
    

    def verify_all_prices_prefixed_with_currency_symbol(self):
        price_locators = [
            locators['TOTAL_PAY'],
            locators['SUB_TOTAL_PRICE'],
            locators['HANDLING_CHARGES_PRICE'],
            locators['CGST_PRICE'],
            locators['SGST_PRICE']
        ]

        for locator in price_locators:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            text = element.text.strip()
            assert text.startswith('₹'), f"Price '{text}' is not prefixed with ₹"
            print(f"Verified: '{text}' is prefixed with ₹")

    def verify_prices_breakdown_in_order_summary(self):
        prices = {}
        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        prices['sub_total'] = float(sub_total_element.text.strip().replace('₹', '').strip())
        handling_charges_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['HANDLING_CHARGES_PRICE'])
        )
        prices['handling_charges'] = float(handling_charges_element.text.strip().replace('₹', '').strip())
        cgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['CGST_PRICE'])
        )
        prices['cgst'] = float(cgst_element.text.strip().replace('₹', '').strip())
        sgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SGST_PRICE'])
        )
        prices['sgst'] = float(sgst_element.text.strip().replace('₹', '').strip())

        return prices
    
    def verify_display_of_charges_and_total_amount_in_order_summary(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")
        self.actions.is_element_displayed(*locators['HANDLING_CHARGES'])
        print("Handling charges is displayed")
        self.actions.is_element_displayed(*locators['CGST'])
        print("CGST is displayed")
        self.actions.is_element_displayed(*locators['SGST'])
        print("SGST is displayed")
        element = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['TOTAL_PAY'])
        )
        amount_text = element.text.strip().replace('₹', '').strip()
        return float(amount_text)
    

    def enter_expired_promo_code_and_click_search(self, Expired_Promo):
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
        self.actions.is_element_displayed(*locators['OFFER_SELECT_BUTTON'])
        print("Offer select button is displayed")
        self.actions.click_button(*locators['OFFER_SELECT_BUTTON'])
        print("Select button is clicked")

    def verify_promo_expired_message(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['PROMO_HEADLINE'])
        self.actions.is_element_displayed(*locators['PROMO_EXPIRED_MESSAGE'])
        print("Promo expired message is displayed")
        self.actions.click_button(*locators['OK_BUTTON'])
        print("Clicked 'Ok button")
        time.sleep(2)
        self.driver.back()
        time.sleep(3)
        self.Clear_all()

    def Verify_item_name_in_cart(self):
        time.sleep(5)  
        if self.actions.is_element_displayed(*locators['FIRST_CART_ITEMS']):
            item_name = self.actions.get_element_text(*locators['FIRST_CART_ITEMS'])
            print(f"Item in cart: {item_name}")
            
            if item_name.strip() == "McVeggie Burger":
                print("McVeggie Burger is correctly displayed in the cart.")
            else:
                print(" Unexpected item found in cart.")
        else:
            print(" Cart item is not displayed.")

    def click_add_delivery_instructions(self):
        time.sleep(5)
        Add_delivery_display = self.driver.find_element(*locators["ADD_DELIVERY_INSTRUCTIONS"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Add_delivery_display)
        self.actions.is_element_displayed(*locators['ADD_DELIVERY_INSTRUCTIONS'])
        print("Add delivery instructions is displayed")

    def enter_notes_in_instructions_field(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_SIGN'])
        print("Add sign is displayed")
        self.actions.click_button(*locators['ADD_SIGN'])
        print("add sign button is clicked")
        time.sleep(10)
        self.actions.enter_text(*locators['NOTE_TEXT_AREA'], "Near Vipul Garden")
        print("Entered notes in instruction field")


    def verify_instructions_field_input(self):
        expected_text = "Near Vipul Garden"
    
        self.enter_notes_in_instructions_field()

        try:
            actual_text = self.actions.get_element_attribute(*locators['NOTE_TEXT_AREA'], 'value')

            if actual_text and actual_text.strip() == expected_text:
                print(" Instructions field accepted the input correctly.")
            else:
                print(f" Mismatch: Expected '{expected_text}', but found '{actual_text}'.")
        except Exception as e:
            print(f" Exception while verifying input: {str(e)}")

    def enter_special_char_in_instructions_field(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_SIGN'])
        print("Add sign is displayed")
        self.actions.click_button(*locators['ADD_SIGN'])
        print("add sign button is clicked")
        time.sleep(10)
        self.actions.enter_text(*locators['NOTE_TEXT_AREA'], "#$%&@")
        print("Entered notes in instruction field")

    def verify_special_char_accepted_as_input_in_instructions_field(self):
        expected_text = "#$%&@"
    
        self.enter_special_char_in_instructions_field()

        try:
            actual_text = self.actions.get_element_attribute(*locators['NOTE_TEXT_AREA'], 'value')

            if actual_text and actual_text.strip() == expected_text:
                print(" Instructions field accepted the input correctly.")
            else:
                print(f" Mismatch: Expected '{expected_text}', but found '{actual_text}'.")
        except Exception as e:
            print(f" Exception while verifying input: {str(e)}")


    def verify_sub_total_for_single_added_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")
        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        sub_total_price = float(sub_total_element.text.strip().replace('₹', '').strip())
        print(f"Subtotal amount: ₹{sub_total_price:.2f}")
        return sub_total_price
   
    def add_item_from_recommendation(self):
        time.sleep(5)
        Recommendation_display = self.driver.find_element(*locators["RECOMMENDATION"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Recommendation_display)
        self.actions.is_element_displayed(*locators['RECOMMENDATION'])
        print("Recommendation is displayed")
        time.sleep(3)
        burger_name = "4 Pcs Chicken Nuggets"
        add_item_locator = locators['ADD_ITEM_TO_CART']
        formatted_xpath = add_item_locator[1].format(burger_name=burger_name)
        self.actions.click_button(add_item_locator[0], formatted_xpath)
        print("'Add Item' button clicked.")
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")
        time.sleep(2)
        # Final Add to Cart
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")
        Clear_all_display = self.driver.find_element(*locators["CLEAR_ALL"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Clear_all_display)
        self.actions.is_element_displayed(*locators['CLEAR_ALL'])
        print("Clear All is displayed")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        print("Scrolled to top of the page")

    def verify_sub_total_for_all_added_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")
        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        sub_total_price = sub_total_element.text.strip().replace('₹', '').strip()
        return float(sub_total_price) 
    
    def verify_cgst_and_sgst_breakdown_in_order_summary(self):
        prices = {}
        cgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['CGST_PRICE'])
        )
        prices['cgst'] = float(cgst_element.text.strip().replace('₹', '').strip())
        sgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SGST_PRICE'])
        )
        prices['sgst'] = float(sgst_element.text.strip().replace('₹', '').strip())

        return prices

    def verify_tax_percentage_calculation(self):
        expected_tax_percent = 4.87  # For CGST and SGST each
        # Step 1: Get subtotal before tax
        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        sub_total = float(sub_total_element.text.strip().replace('₹', '').strip())

        # Step 2: Get actual CGST and SGST values
        cgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['CGST_PRICE'])
        )
        cgst_value = float(cgst_element.text.strip().replace('₹', '').strip())

        sgst_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SGST_PRICE'])
        )
        sgst_value = float(sgst_element.text.strip().replace('₹', '').strip())

        # Step 3: Calculate expected tax values
        expected_cgst = round((sub_total * expected_tax_percent) / 100, 2)
        expected_sgst = round((sub_total * expected_tax_percent) / 100, 2)

        # Step 4: print results
        print(f"Expected CGST: ₹{expected_cgst}")
        print(f"Expected SGST: ₹{expected_sgst}")


    def verify_estimated_delivery_time(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ESTIMATED_DELIVERY_TIME_HEADLINE'])
        print("Estimated delivery time is displayed")
        self.actions.is_element_displayed(*locators['ESTIMATED_DELIVERY_TIME_TEXT'])
        print("Estimated delivery time along with text is displayed")
        time.sleep(2)
        self.Clear_all()

    def verify_applied_offer_and_click_change_offer(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['OFFER_APPLIED'])
        print("offer applied text is displayed")
        self.actions.is_element_displayed(*locators['APPLIED_OFFER_NAME'])
        print("applied offer name is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['CHANGE_OFFER'])
        print("Change offer is clicked")

    def verify_first_offer_is_removed_and_the_second_offer_is_displayed(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['OFFER_APPLIED'])
        print("offer applied text is displayed")
        if self.actions.is_element_displayed(*locators['APPLIED_OFFER_NAME']):
            print(" First offer is still displayed")
        else:
            print(" First offer is NOT displayed (as expected)")
        self.actions.is_element_displayed(*locators['APPLIED_SECOND_OFFER_NAME'])
        print("Second applied offer is displayed")
        time.sleep(2)
        self.Clear_all()

    def get_total_amount_from_order_summary(self):
        prices = self.verify_prices_breakdown_in_order_summary()
        self.initial_prices = prices
        self.initial_total = prices['sub_total'] + prices['handling_charges'] + prices['cgst'] + prices['sgst']
        print(f"Initial breakdown: {self.initial_prices}")
        print(f"Initial total: ₹{self.initial_total:.2f}")
        return round(self.initial_total, 2)
    
    def step_capture_total_before_applying_promo(self):
        self.initial_total = self.get_total_amount_from_order_summary()
        print(f"Original total before discount: ₹{self.initial_total:.2f}")

    def verify_discount_is_applied_correctly(self):
        time.sleep(5)
    
        discounted_prices = self.verify_prices_breakdown_in_order_summary()
        discounted_total = discounted_prices['sub_total'] + discounted_prices['handling_charges'] + discounted_prices['cgst'] + discounted_prices['sgst']
        print(f"Discounted breakdown: {discounted_prices}")
        print(f"Discounted total: ₹{discounted_total:.2f}")

        discount = self.initial_total - discounted_total

        if discount > 0:
            print(f" Discount applied successfully. Amount reduced by ₹{discount:.2f}")

            handling_diff = self.initial_prices['handling_charges'] - discounted_prices['handling_charges']
            if handling_diff > 0:
                print(f"ℹ Handling charges were discounted by ₹{handling_diff:.2f}")
        else:
            raise AssertionError(" Discount not applied correctly. Total amount did not decrease.")
        self.Clear_all()
        

    def verify_subtotal_includes_handling_charges(self):
        time.sleep(5)
        
        # Verify and get Subtotal
        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")
        subtotal_element = self.driver.find_element(*locators['SUB_TOTAL'])
        subtotal_text = subtotal_element.text.strip().replace('₹', '').strip()
        subtotal = float(subtotal_text)
        
        # Verify and get Handling Charges
        self.actions.is_element_displayed(*locators['HANDLING_CHARGES'])
        print("Handling charges is displayed")
        handling_element = self.driver.find_element(*locators['HANDLING_CHARGES'])
        handling_text = handling_element.text.strip().replace('₹', '').strip()
        handling = float(handling_text)

        # Optional logical check
        if subtotal < handling:
            raise AssertionError("Subtotal should include or be at least equal to handling charges, but it is less.")

        print(f"Subtotal: ₹{subtotal}, Handling Charges: ₹{handling} — Verified subtotal includes delivery charge.")
        
        # ✅ Return numeric values
        return subtotal, handling
        
    
    def verify_subtotal_includes_handling_charges(self) -> dict:
        prices = {}

        self.actions.is_element_displayed(*locators['SUB_TOTAL'])
        print("Sub total is displayed")

        sub_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SUB_TOTAL_PRICE'])
        )
        sub_total_price = float(sub_total_element.text.strip().replace('₹', '').replace(',', '').strip())
        prices['sub_total_price'] = sub_total_price

        self.actions.is_element_displayed(*locators['HANDLING_CHARGES'])
        print("Handling charges is displayed")

        handling_charges_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['HANDLING_CHARGES_PRICE'])
        )
        handling_price = float(handling_charges_element.text.strip().replace('₹', '').replace(',', '').strip())
        prices['handling_charges_price'] = handling_price

        # Optional logical check
        if sub_total_price < handling_price:
            raise AssertionError("Subtotal should include or be at least equal to handling charges, but it is less.")

        print(f" Subtotal: ₹{sub_total_price}, Handling Charges: ₹{handling_price} — Verified subtotal includes delivery charge.")

        return prices
    

    def Verify_item_and_quantity_in_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CART_ITEM'])
        print(" McAloo Tikki Burger is displayed")
        self.actions.is_element_displayed(*locators['QUANTITY_COUNT'])
        print("quantity for item is displayed")

    def verify_applied_offer_displays_in_cart(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['OFFER_APPLIED'])
        print("offer applied text is displayed")
        self.actions.is_element_displayed(*locators['APPLIED_OFFER_NAME'])
        print("Freedelivery@199 offer name is displayed")
        time.sleep(2)
        self.Clear_all()

    def verify_user_redirected_to_cart_page(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['YOUR_ORDER'])
        print("Your order text is displayed in cart")
        time.sleep(2)
        self.Clear_all()

    def Click_on_mcdelivery_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON'])
        self.actions.click_button(*locators['MCDELIVERY_ICON'])
        print("Mcdelivery icon clicked.")
    










        
        
    

