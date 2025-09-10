from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

locators = {
        "HEADER_BANNER": (By.XPATH, "//ion-header[@role='banner']"),
        "VIEW_ICON": (By.XPATH, "//div[@title='View Profile']"),
        "ADDRESS_DROPDOWN": (By.XPATH, "(//div[@class='toolbar-v1__location-type txt-ellipsis']/img[@title='ic-arrow-down'])[1]"),
        "NEARBY_RESTAURANTS": (By.XPATH, '//span[contains(@class, "toolbar-desktop__menu") and contains(text(), "Restaurants Nearby")]'),
        "NEAR_ME_STORES": (By.XPATH, "//div[@class='near-me__store']"),
        #"3_PC_MEALS": (By.XPATH, "//img[@title='Burger Combos ( 3 Pc Meals )']"),
        "3_PC_MEALS": (By.XPATH, "//div[@class='grid-container__item'][.//span[text()='Burger Combos ( 3 Pc Meals )']]"),
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
        "MODIFIED_ADDRESS": (By.XPATH, " //div[contains(text(), ' 123, Marathahalli, Aeromedical Consultancy ')]"),
        "CLICK_BACK_BUTTON_FROM_SELECT_LOCATION" : (By.XPATH, "//img[@alt='ic-arrow-left-primary']"),
        "SELECTED_ADDRESS_LABEL" : (By.XPATH, "(//div[contains(text(), 'HPCL HOUSING COLONY')])[1]"),
        "HOME_PAGE_ADDRESS" : (By.XPATH, "//div[contains(@class, 'toolbar-v1__location')]"),
        "ERROR_MESSAGE_FOR_UNDELIVERABLE_ADDRESS" : (By.XPATH, "//div[@class = 'banner-v1__container']"),
        "ADD_ITEM_TO_CART" : (By.XPATH, "//div[contains(@class, 'menu__title') and normalize-space(text())='{burger_name}']/following::div[contains(@class, 'add-to-cart')][1]"),
        "CART_ITEM" : (By.XPATH, "//div[@class = 'cart-page__order-summary-card']"),
        "ADD_ITEM": (By.XPATH, "//div[contains(@class, 'menu__title') and contains(normalize-space(), 'McVeggie Burger')]/following::div[contains(@class, 'add-to-cart')][1]"),
        "ITEM_DETAIL_PAGE": (By.XPATH, "//h5[contains(text(), ' Customise Your McVeggie Burger ')]"),
        "CLICK_NEXT": (By.XPATH, "//button[contains(text(), 'Next')]"),
        "CLICK_ADD_TO_CART": (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
        "CART_ICON": (By.XPATH, "//img[@class = 'toolbar-desktop__icon']"),
        "YOUR_ORDER": (By.XPATH, "//h1[contains(text(), ' Your Order')]"),
        "ADDED_ITEM_DISPLAY_IN_CART": (By.XPATH, "//h4[contains(text(), ' McVeggie Burger ')]"),
        "MCDELIVERY_ICON": (By.XPATH, "//img[@alt = 'logo']"),
        #"PRODUCT_PRIZE": (By.XPATH, "(//div[text() = ' McVeggie Burger '])[1]/../div[2]//span[@class ='menu__price']"),
        "PRODUCT_PRIZE": (By.XPATH, "(//div[contains(@class, 'menu__title') and normalize-space(text())='{}'])[1]/../div[2]//span[@class = 'menu__price']"),
        "SOLD_OUT": (By.XPATH, "(//strong[contains(text(), 'Sold out')])[1]"),
        "OUR_MENU": (By.XPATH, "(//div[contains(text(), 'Our Menu')])[3]"),
        "3PC_MEALS_CATEGORY": (By.XPATH, "(//div[@class = 'popular__menu-row'])[2]"),
        "CART_DELETE_POP_UP": (By.XPATH, " //div[contains(text(), 'cart deleted sucessfully')]"),
        "FIRST_CART_ITEMS": (By.XPATH, " //h4[normalize-space()='McVeggie Burger']/ancestor::div[contains(@class, 'menu__primary')]"),
        "HOME_SEARCH_ICON": (By.XPATH, "//img[@title = 'ic-search-b']"),
        "SEARCH_MENU_HEADER": (By.XPATH, " //h1[contains(text(), 'Search Menu')]"),
        "SEARCH_MENU": (By.XPATH, "//input[@placeholder = 'Search here']"),
        "FRIES_MENU": (By.XPATH, "(//h4[contains(text(), '2 Fries (R)')])[1]"),
        "FRIES_AND_STRAWBERRY_MENU": (By.XPATH, "(//h4[contains(text(), 'Strawberry Shake + Fries (M)')])[1]"),
        "SEARCH_MENU_ITEM_TEXT": (By.XPATH, "//div[contains(text(), ' Search menu item')]"),
        "ITEM_NOT_FOUND_TEXT": (By.XPATH, " //div[contains(text(), 'No matching item found')]"),
        "VEG_FILTER": (By.XPATH, "  //span[contains(text(), ' Veg ')]"),
        "VEG_ICON_SYMBOL": (By.XPATH, "(//div[@class='menu'][.//img[@alt='ic-veg']]//h4[@class='menu__title']/text())[1]"),
        "NON_VEG_FILTER": (By.XPATH, "  //span[contains(text(), ' Non-Veg ')]"),
        "NON_VEG_ICON_SYMBOL": (By.XPATH, " (//div[@class='menu'][.//img[@alt='ic-nonveg']]//h4[@class='menu__title']/text())[1]"),
        "VEG_FILTER_CLOSE_ICON": (By.XPATH, " //img[@alt = 'ic-close-red']"),
        #"ADD_BURGER_ITEM": (By.XPATH, " //div[contains(@class, 'menu') and normalize-space(text())='{burger_name}']/ancestor::div[@class='menu']/div[@class='menu__price-cta']//div[contains(@class, 'add-to-cart__cta-btn-full') and contains(text(), 'Add')]"),
        "ADD_BURGER_ITEM": (By.XPATH, " //div[@class='menu']//h4[text()='McAloo Tikki Burger']/ancestor::div[@class='menu']/div[@class='menu__price-cta']//div[contains(@class, 'add-to-cart__cta-btn-full') and contains(text(), 'Add')]"),
        "ITEM_COUNT": (By.XPATH, " //div[contains(@class, 'menu__title') and contains(normalize-space(), 'McAloo Tikki Burger')]/following::div[contains(@class, 'add-to-cart__count')]"),
        "BURGER_SEARCH_RESULT": (By.XPATH, " (//h4[contains(text(), 'Chicken Surprise Burger + McChicken Burger')])[1]"),
        "REMOVE_ITEM_MINUS_SIGN": (By.XPATH, "(//img[@alt='ic-subtract'])[1]"),
        "DELETE_CART": (By.XPATH, "  //h2[contains(text(), 'Delete Cart')]"),
        "DELETE_CART_OK_BUTTON": (By.XPATH, " //span[contains(text(), 'OK')]"),
    

       
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
        
    def select_product_from_3PC_meals_category(self):
        time.sleep(5)
        burger_name = " McChicken Burger "
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
        dine_in_models = self.driver.find_elements(*locators['DINE_IN_OPTION'])
        takeaway_models = self.driver.find_elements(*locators['TAKE_AWAY_OPTION'])
        all_models = dine_in_models + takeaway_models

        for model in all_models:
            print("Model class:", model.get_attribute("class"))

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

        # List of burger names to try in order
        burger_names = ["McAloo Tikki Burger", "McVeggie Burger", "McChicken Burger"]

        add_item_locator = locators['ADD_ITEM_TO_CART']
        burger_found = False

        # Try each burger until one is found and added
        for burger_name in burger_names:
            try:
                formatted_xpath = add_item_locator[1].format(burger_name=burger_name)

                # Wait and click on the burger's 'Add' button
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((add_item_locator[0], formatted_xpath))
                ).click()
                print(f"'Add Item' button clicked for {burger_name}")
                burger_found = True
                break  # Exit loop after successfully adding a burger

            except Exception as e:
                print(f"⚠️ '{burger_name}' not found or not clickable. Trying next burger...")

        if not burger_found:
            raise Exception("❌ None of the burgers were available to add to cart.")

        # Step 2: Click on 'Next'
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")

        time.sleep(2)

        # Step 3: Final Add to Cart
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")

    def verify_Dine_In_selected_until_manually_changed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        print("Dine In selected after browsing menu and returning back to homepage")

    def verify_updated_address_display_in_address_list(self):
        # Open dropdown
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locators['ADDRESS_DROPDOWN'])
        ).click()
        print("Clicked on address dropdown")

        # Wait for list to appear and target address to be present/visible
        modified_el = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locators['MODIFIED_ADDRESS'])
        )
        assert modified_el.is_displayed(), "Modified address not shown in list"

        modified_address_text = modified_el.text.strip()
        print(f"Found modified address: {modified_address_text}")

        # Click the modified address
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['MODIFIED_ADDRESS'])
        ).click()
        print("Modified address clicked in the address list")

        # Close the select-location popup
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators['CLICK_BACK_BUTTON_FROM_SELECT_LOCATION'])
        ).click()
        print("Clicked on back button from select location popup")

    def Click_back_button_from_select_location_page(self):
       time.sleep(5)
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
    

    def add_multiple_items_to_cart(self):
        time.sleep(5)
        # Step 1: List of items to add
        item_names = [
            "McVeggie Burger",
            "McCrispy Chicken Burger"
        ]

        for item in item_names:
            print(f"\n Attempting to add item: {item}")
            add_item_locator = locators['ADD_ITEM_TO_CART']
            formatted_xpath = add_item_locator[1].format(burger_name=item)

            # Step 2: Click on Add button
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((add_item_locator[0], formatted_xpath))
                )
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((add_item_locator[0], formatted_xpath))
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                element.click()
                print(f" 'Add' clicked for: {item}")
            except Exception as e:
                print(f" Failed to add '{item}': {e}")
                self.driver.save_screenshot(f"error_adding_{item}.png")
                continue

            # Step 3: Click "Next" button
            if self.actions.is_element_displayed(*locators['CLICK_NEXT']):
                self.actions.click_button(*locators['CLICK_NEXT'])
                print(f"'Next' clicked for: {item}")

            time.sleep(2)

            # Step 4: Final Add to Cart
            if self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART']):
                self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
                print(f"'{item}' added to cart successfully")

            time.sleep(2)

    def add_item_in_cart(self):
        time.sleep(2)
        print("Attempting to display and click 'Add Item' button.")
        self.actions.is_element_displayed(*locators['ADD_ITEM'])
        self.actions.click_button(*locators['ADD_ITEM'])
        print("'Add Item' button clicked.")

    def verify_items_details_popup(self):
        time.sleep(5)
        print("Verifying item details popup is displayed.")
        return self.actions.is_element_displayed(*locators['ITEM_DETAIL_PAGE'])

    def click_next_button(self):
        print("Checking and clicking 'Next' button.")
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")
        time.sleep(2)

    def click_add_to_cart(self):
        print("Checking and clicking 'Add to Cart' button.")
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")
        time.sleep(2)

    def verify_item_added_in_cart(self):
        time.sleep(5)
        print("Opening cart to verify item.")
        self.actions.is_element_displayed(*locators['CART_ICON'])
        self.actions.click_button(*locators['CART_ICON'])
        print("Cart icon clicked.")
        self.actions.is_element_displayed(*locators['YOUR_ORDER'])
        self.actions.is_element_displayed(*locators['ADDED_ITEM_DISPLAY_IN_CART'])
        print("Item is displayed in cart.")

    def navigate_to_cart(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CART_ICON'])
        self.actions.click_button(*locators['CART_ICON'])
        print("Cart icon clicked.")


    '''
    def verify_price_is_visible_for_items(self):
        time.sleep(5)
        menu_name = "McVeggie Burger"
        price_xpath = locators['PRODUCT_PRIZE'][1].format(menu_name)
        locator = (locators['PRODUCT_PRIZE'][0], price_xpath)
        self.actions.is_element_displayed(*locator)
        print(f"Price is displayed for item: {menu_name}")

        '''


    def verify_price_is_visible_for_items(self):
        time.sleep(5)
        menu_names = ["McVeggie Burger", "McCrispy Chicken Burger", "Fries (M) + Piri Piri Mix"]
        for name in menu_names:
            xpath = locators['PRODUCT_PRIZE'][1].format(name)
            locator = (locators['PRODUCT_PRIZE'][0], xpath)
            assert self.actions.is_element_displayed(*locator), f"Price not shown for {name}"
            print(f"Price is displayed for item: {name}")

    def add_single_item_in_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADD_ITEM'])
        self.actions.click_button(*locators['ADD_ITEM'])
        print("'Add Item' button clicked.")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")

    def Verify_display_item_marked_as_sold_out(self):
       time.sleep(5)
       self.actions.is_element_displayed(*locators['SOLD_OUT'])
       print("Sold out display for items")

    def verify_sold_out_item_not_clickable(self):
        time.sleep(5)
        # Verify that 'Sold Out' label is visible
        Sold_out_display = self.driver.find_element(*locators["SOLD_OUT"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Sold_out_display)

        try:
            # Try to check if "Add to Cart" button is visible
            is_displayed = self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        except Exception:
            # If it's not found or causes error, treat it as not visible
            is_displayed = False

        # Final assertion
        assert not is_displayed, "Add to Cart button should not be visible"


    def select_3PC_meal_under_menu(self):
        time.sleep(5)
        Three_Pc_Meals = self.driver.find_element(*locators["3_PC_MEALS"])
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", Three_Pc_Meals)
        Three_Pc_Meals.click()
        print("Clicked on 3PC meals")

    def verify_display_of_3PC_meal_category(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['3PC_MEALS_CATEGORY'])
    

    def verify_cart_icon_does_not_appear_if_cart_is_empty(self):
        time.sleep(5)
        try:
            if self.actions.is_element_displayed(*locators['CART_ICON']):
                self.actions.click_button(*locators['CART_ICON'])
                print("Cart icon clicked.")
            else:
                print("Cart icon is not displayed on the homepage.")
        except Exception as e:
            print("Cart icon not found. Exception:", str(e))

    def Cart_delete_pop_up(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['CART_DELETE_POP_UP'])
        print("Cart delete pop up is displayed")


    def add_random_item_in_cart(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADD_ITEM'])
        self.actions.click_button(*locators['ADD_ITEM'])
        print("'Add Item' button clicked.")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLICK_NEXT'])
        self.actions.click_button(*locators['CLICK_NEXT'])
        print("'Next' button clicked.")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CART_ICON'])
        self.actions.click_button(*locators['CART_ICON'])
        print("Cart icon clicked.")
        # Get the cart item name before refresh
        time.sleep(3)
        item_element = self.driver.find_element(*locators['FIRST_CART_ITEMS'])
        item_text = item_element.text
        print(f"Item before refresh: {item_text}")

    def click_on_search_icon_on_home_page(self):
        time.sleep(3)
        self.actions.click_button(*locators['HOME_SEARCH_ICON'])
        print("Clicked search Icon On Home Page")

    def verify_navigate_to_menu_search_page(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_HEADER'])
        print("Search menu page is displayed")

    def click_on_menu_search_icon_and_enter_fries(self):
        time.sleep(3)
        self.actions.click_button(*locators['SEARCH_MENU'])
        print("Clicked search menu Icon On menu Page")
        self.actions.enter_text(*locators['SEARCH_MENU'], "Fries")

    def verify_search_result_display_fries_menu_items(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['FRIES_MENU'])
        self.actions.is_element_displayed(*locators['FRIES_AND_STRAWBERRY_MENU'])
        print("Fries menu items is displayed")

    def click_search_with_empty_input(self):
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_MENU'])
        print("Clicked search menu Icon On menu Page")

    def verify_prompt_display(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['SEARCH_MENU_ITEM_TEXT'])
        print("Search menu item text is displayed")

    def enter_non_existance_menu_and_click_search(self):
        time.sleep(3)
        self.actions.click_button(*locators['SEARCH_MENU'])
        print("Clicked search menu Icon On menu Page")
        self.actions.enter_text(*locators['SEARCH_MENU'], "$%^#")

    def verify_message_when_items_not_found(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ITEM_NOT_FOUND_TEXT'])
        print("No matching item found text is displayed")

    def verify_placeholder_shows_search_here(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['SEARCH_MENU'])
        print("Search here text is displayed")

    def clear_search_input_field(self):
        time.sleep(3)
        search_field = self.driver.find_element(*locators['SEARCH_MENU'])
        search_field.clear()
        print("Cleared the entered input from search field")

    def click_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VEG_FILTER'])
        print("Veg filter is displayed")
        self.actions.click_button(*locators['VEG_FILTER'])
        print("Clicked veg filter On menu Page")

    def verify_display_of_veg_items(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['VEG_ICON_SYMBOL'])
        print("Veg itmes is displayed after appling the veg filter")

    def click_non_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['NON_VEG_FILTER'])
        print("Non-Veg filter is displayed")
        self.actions.click_button(*locators['NON_VEG_FILTER'])
        print("Clicked non-veg filter On menu Page")

    def verify_display_of_non_veg_items(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['NON_VEG_ICON_SYMBOL'])
        print("Non-Veg itmes is displayed after appling the Non-veg filter")

    def click_close_icon_on_veg_filter(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['VEG_FILTER_CLOSE_ICON'])
        print("Veg filter close icon is displayed")
        self.actions.click_button(*locators['VEG_FILTER_CLOSE_ICON'])
        print("Clicked on close icon of veg filter")

    def search_for_burger_item(self):
        time.sleep(3)
        self.actions.click_button(*locators['SEARCH_MENU'])
        print("Clicked search menu Icon On menu Page")
        self.actions.enter_text(*locators['SEARCH_MENU'], "burger")

    def add_burger_item(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_BURGER_ITEM'])
        self.actions.click_button(*locators['ADD_BURGER_ITEM'])
        print("'Add' button clicked and burger added to the cart")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART'])
        self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
        print("'Add to Cart' button clicked.")

    def verify_burger_search_result_persist_post_add(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ITEM_COUNT'])
        print("burger added count is displayed")
        self.actions.is_element_displayed(*locators['BURGER_SEARCH_RESULT'])
        print("burger search result is persist post add the burger")
        time.sleep(3)
        self.actions.is_element_displayed(*locators['REMOVE_ITEM_MINUS_SIGN'])
        self.actions.click_button(*locators['REMOVE_ITEM_MINUS_SIGN'])
        print("Remove button clicked")
        self.actions.is_element_displayed(*locators['DELETE_CART'])
        print("Delete cart pop up is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['DELETE_CART_OK_BUTTON'])
        print("Ok button is clicked")

    def add_visible_burger_to_cart(self):
        time.sleep(5)

        # Step 1: List of preferred burger items to try
        item_names = [
            "McVeggie Burger",
            "McCrispy Chicken Burger",
            " Filet-O-Fish Burger "
        ]

        for item in item_names:
            print(f"\nAttempting to locate visible item: {item}")
            add_item_locator = locators['ADD_ITEM_TO_CART']
            formatted_xpath = add_item_locator[1].format(burger_name=item)

            try:
                # Step 2: Check if burger is visible on the page
                elements = self.driver.find_elements(add_item_locator[0], formatted_xpath)
                visible_elements = [el for el in elements if el.is_displayed()]

                if not visible_elements:
                    print(f"'{item}' is not currently visible. Skipping.")
                    continue

                element = visible_elements[0]

                # Step 3: Scroll and click on visible element
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((add_item_locator[0], formatted_xpath)))
                element.click()
                print(f"'Add' clicked for: {item}")

                # Step 4: Click "Next" if visible
                if self.actions.is_element_displayed(*locators['CLICK_NEXT']):
                    self.actions.click_button(*locators['CLICK_NEXT'])
                    print(f"'Next' clicked for: {item}")

                time.sleep(2)

                # Step 5: Final Add to Cart
                if self.actions.is_element_displayed(*locators['CLICK_ADD_TO_CART']):
                    self.actions.click_button(*locators['CLICK_ADD_TO_CART'])
                    print(f"'{item}' added to cart successfully")

                time.sleep(2)

            except Exception as e:
                print(f"Failed to add '{item}': {e}")
                self.driver.save_screenshot(f"error_adding_{item}.png")
                continue



    
        

        





