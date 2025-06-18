from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        "VIEW_CART": (By.XPATH, "//div[@class='cart-status-bar__cta' and contains(text(), 'View Cart')]"),
        "BUSINESS_MODEL_DROPDOWN": (By.XPATH, "//img[@alt = 'ic-arrow-down-white']"),
        "MCDELIVERY_OPTION": (By.XPATH, "//span[contains(text(), 'McDelivery')]"),
        "DINE_IN_OPTION": (By.XPATH, "//span[contains(text(), 'Dine-In')]"),
        "ON_THE_GO_OPTION": (By.XPATH, "//span[contains(text(), 'On the Go')]"),
        "TAKE_AWAY_OPTION": (By.XPATH, "//span[contains(text(), 'Take Away')]"),
        "MCDELIVERY_ORDERING_PAGE": (By.XPATH, "//div[@class = 'popular__menu-row']"),
        "DINE_IN_LOCATION_PAGE": (By.XPATH, "//div[@class = 'toolbar-desktop show-toolbar']"),
        "ON_THE_GO_LOCATION_PAGE": (By.XPATH, "//div[@class = 'toolbar-desktop show-toolbar']"),
        "TAKE_AWAY_LOCATION_PAGE": (By.XPATH, "//div[@class = 'toolbar-desktop__lhs']"),
        "TOAST_MESSAGE_LOCATION_ENABLED": (By.XPATH, "//div[contains(@class, 'toast') and contains(text(), 'Sorry')]"),
        "SELECTED_MODEL": (By.XPATH, "//div[@class = 'bm-select link']"),
        "MCDELIVERY_ICON_AND_TEXT": (By.XPATH, "//img[@alt='ic-bm-delivery-active']/following-sibling::span[text()='McDelivery']"),
        "DINE_IN_ICON_AND_TEXT": (By.XPATH, "//img[@alt='ic-bm-dine-in']/following-sibling::span[text()='Dine-In']"),
        "ON_THE_GO_ICON_AND_TEXT": (By.XPATH, "//img[@alt='ic-bm-otg']/following-sibling::span[text()='On the Go']"),
        "TAKE_AWAY_ICON_AND_TEXT": (By.XPATH, "//img[@alt='ic-bm-delivery']/following-sibling::span[text()='Take Away']"),
        "MODIFIED_ADDRESS": (By.XPATH, " (//div[contains(text(), 'HPCL HOUSING COLONY')])[5]"),
        "CLICK_BACK_BUTTON_FROM_SELECT_LOCATION" : (By.XPATH, "//img[@alt='ic-arrow-left-primary']"),
        "SELECTED_ADDRESS_LABEL" : (By.XPATH, "(//div[contains(text(), 'HPCL HOUSING COLONY')])[1]"),
        "HOME_PAGE_ADDRESS" : (By.XPATH, "//div[contains(@class, 'toolbar-v1__location')]"),
        "ERROR_MESSAGE_FOR_UNDELIVERABLE_ADDRESS" : (By.XPATH, "//div[@class = 'banner-v1__container']"),
       
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


    def Click_business_model_dropdown(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['BUSINESS_MODEL_DROPDOWN'])
        self.actions.click_button(*locators['BUSINESS_MODEL_DROPDOWN'])
        print("Clicked on business model dropdown")

    def verify_dropdown_displays_all_business_model(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        print("Mcdelivery displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        print("Dine-In displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['ON_THE_GO_OPTION'])
        print("On the Go displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['TAKE_AWAY_OPTION'])
        print("Take Away displayed on business model dropdown")

    def verify_Selection_of_McDelivery_option_from_dropdown(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        self.actions.click_button(*locators['MCDELIVERY_OPTION'])
        print("Clicked on McDelivery from dropdown")

    def verify_user_redirect_to_McDelivery_ordering_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['MCDELIVERY_ORDERING_PAGE'])

    def verify_Selection_of_Dine_In_option_from_dropdown(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        self.actions.click_button(*locators['DINE_IN_OPTION'])
        print("Clicked on Dine-In from dropdown")

    def verify_user_redirect_to_Dine_In_location_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['DINE_IN_LOCATION_PAGE'])
    
    def verify_Selection_of_On_the_go_option_from_dropdown(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ON_THE_GO_OPTION'])
        self.actions.click_button(*locators['ON_THE_GO_OPTION'])
        print("Clicked On the go from dropdown")
    
    def verify_user_redirect_to_On_the_go_pick_up_location_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ON_THE_GO_LOCATION_PAGE'])
    
    def verify_Selection_of_take_away_option_from_dropdown(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['TAKE_AWAY_OPTION'])
        self.actions.click_button(*locators['TAKE_AWAY_OPTION'])
        print("Clicked on take away from dropdown")
    
    def verify_user_redirect_to_take_away_location_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['TAKE_AWAY_LOCATION_PAGE'])
    
    def verify_McDelivery_selected_by_default(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        print("McDelivery selected by default in business model")

    def show_toast(self):
        try:
        # Wait up to 5 seconds for the toast message to appear
            toast = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locators['TOAST_MESSAGE_LOCATION_ENABLED'])
        )
            web_toast_message = toast.text.strip()
            expected_message = "Sorry, we do not serve this location yet"
        
            if web_toast_message == expected_message:
                print("Toast message matches.")
            else:
                print(f"Toast message not matched: '{web_toast_message}'")
        except Exception as e:
            print(f"Toast message not found: {e}")

    def step_select_first_model(self):
        time.sleep(5)
        model_elements = self.driver.find_elements(*locators['DINE_IN_OPTION'])
        model_elements[0].click()

    def step_select_second_model(self):
        time.sleep(5)
        self.actions.click_button(*locators['BUSINESS_MODEL_DROPDOWN'])
        print("Clicked on business model dropdown")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['TAKE_AWAY_OPTION'])
        self.actions.click_button(*locators['TAKE_AWAY_OPTION'])

    def step_check_only_one_active(self):
        # Combine all model elements
        dine_in_models = self.driver.find_elements(*locators['DINE_IN_OPTION'])
        takeaway_models = self.driver.find_elements(*locators['TAKE_AWAY_OPTION'])
        all_models = dine_in_models + takeaway_models

        # Filter those that have 'active' in class attribute
        active_models = [model for model in all_models if 'active' in model.get_attribute('class')]

        assert len(active_models) == 1, f"Expected 1 active model, found {len(active_models)}"

    def open_new_tab(self):
        time.sleep(5)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.uat.mcdapp.co/")

    def verify_take_away_option_is_still_selected(self):
        time.sleep(5)
        selected_option = self.driver.find_element(*locators['SELECTED_MODEL'])
        selected_text = selected_option.text.strip()
        if not selected_text:
            for attr in ['aria-label', 'title', 'value', 'innerHTML']:
                selected_text = selected_option.get_attribute(attr)
                if selected_text:
                    selected_text = selected_text.strip()
                    break
        assert selected_text.lower() == "take away", f"Expected 'Take Away', but found '{selected_text}'"
        print("Take Away option is still selected in the new tab.")


    def verify_icons_and_text_display_on_each_business_model(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON_AND_TEXT'])
        print("Mcdelivery text is displayed with icon")
        self.actions.is_element_displayed(*locators['DINE_IN_ICON_AND_TEXT'])
        print("Dine-In text is displayed with icon")
        self.actions.is_element_displayed(*locators['ON_THE_GO_ICON_AND_TEXT'])
        print("On the Go text is displayed with icon")
        self.actions.is_element_displayed(*locators['TAKE_AWAY_ICON_AND_TEXT'])
        print("Take Away text is displayed with icon")

    def verify_switching_from_one_model_to_another(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        self.actions.click_button(*locators['DINE_IN_OPTION'])
        time.sleep(5)
        self.actions.click_button(*locators['BUSINESS_MODEL_DROPDOWN'])
        print("Clicked on business model dropdown")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['TAKE_AWAY_OPTION'])
        self.actions.click_button(*locators['TAKE_AWAY_OPTION'])

    def step_select_third_model(self):
        time.sleep(5)
        self.actions.click_button(*locators['BUSINESS_MODEL_DROPDOWN'])
        print("Clicked on business model dropdown")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ON_THE_GO_OPTION'])
        self.actions.click_button(*locators['ON_THE_GO_OPTION'])

    def step_select_fourth_model(self):
        time.sleep(5)
        self.actions.click_button(*locators['MCDELIVERY_ICON'])
        time.sleep(3)
        self.actions.click_button(*locators['BUSINESS_MODEL_DROPDOWN'])
        print("Clicked on business model dropdown")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        self.actions.click_button(*locators['MCDELIVERY_OPTION'])

    def verify_browse_menu(self):
        time.sleep(5)
        burger_name = "McAloo Tikki Burger"
        add_item_locator = locators['ADD_ITEM_TO_CART']
        formatted_xpath = add_item_locator[1].format(burger_name=burger_name)
        # Click on add to cart for the selected burger
        self.actions.click_button(add_item_locator[0], formatted_xpath)
        print("'Add Item' button clicked.")
        # Click on Next
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")
        time.sleep(2)
        # Final Add to Cart
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")

    def verify_Dine_In_selected_until_manually_changed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        print("Dine In selected after browsing menu and returning back to homepage")

    def verify_updated_address_display_in_address_list(self, expected_partial_text):
        self.actions.click_button(*locators['ADDRESS_DROPDOWN'])
        print("CLicked on add address dropdown")
        # Assert that the modified address appears in the list
        time.sleep(10)
        assert self.actions.is_element_displayed(*locators['MODIFIED_ADDRESS']), "Modified address not shown in list"
        modified_address_text = self.actions.get_text(*locators['MODIFIED_ADDRESS'])
        print(f"Found modified address: {modified_address_text}")
        # Optional: Click on the modified address to select it
        self.actions.click_button(*locators['MODIFIED_ADDRESS'])
        print("Modified address clicked in the address list")
        # Validate that it becomes the selected address
        selected_address_text = self.actions.get_text(*locators['SELECTED_ADDRESS_LABEL'])
        assert expected_partial_text.strip() in selected_address_text.strip(), f"Expected '{expected_partial_text}' in selected address, but found '{selected_address_text}'"
        print("Updated address is correctly displayed as selected")
        # Exit from popup
        self.actions.click_button(*locators['CLICK_BACK_BUTTON_FROM_SELECT_LOCATION'])
        print("Clicked on back button from select location popup")

    def verify_address_selected_and_restaurant_updated_accordingly(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['HOME_PAGE_ADDRESS'])
    
    def verify_recently_used_address_is_auto_selected_after_login(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['HOME_PAGE_ADDRESS'])
    
    def verify_error_message_for_undeliverable_address(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ERROR_MESSAGE_FOR_UNDELIVERABLE_ADDRESS'])
