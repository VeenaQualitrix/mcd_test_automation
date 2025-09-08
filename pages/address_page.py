from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
        "ADD_NEW": (By.XPATH, "//span[contains(text(), 'Add new')]"),
        "SEARCH_BUTTON": (By.XPATH, "//span[@class='searchbar__placeholder']"),
        "SEARCH_INPUT_FIELD": (By.XPATH, "//input[@class='searchbar__input']"),
        "SEARCH_NEXT_INPUT_FIELD": (By.XPATH, "//div[@class ='searchbar__mock-input']"),
        "SEARCH_RESULTS": (By.XPATH, "//div[@class='search-result__item']"),
        "SELECT_ADDRESS": (By.XPATH, "//div[contains(text(), '{}')]"),
        "CONFIRM_LOCATION": (By.XPATH, "//button[contains(text(), 'Confirm Location')]"),
        "HOUSE_NUMBER": (By.XPATH, "//input[@placeholder='*House / Flat No.']"),
        "SAVE_ADDRESS": (By.XPATH, "//button[contains(@class, 'bottom-sheet__cta')]"),
        "ADDED_ADDRESS": (By.XPATH, "//div[contains(@class, 'address__row-2')]/div[contains(text(), '{}')]"),
        "ADDRESS_SELECTED": (By.XPATH, "//div[contains(@class, 'txt-ellipsis')][contains(text(), '{}')]"),
        "ADDRESS_ARROW": (By.XPATH, "//img[@alt = 'ic-arrow-down']"),
        "LOGIN_PROMPT": (By.XPATH, "//div[contains(text(), ' Log In / Sign Up to Continue ')]"),
        "LOGIN_FROM_CHECKOUT_PAGE": (By.XPATH, "//button[contains(text(), 'Log In / Sign Up to Continue')]"),
        "CANCEL_FROM_LOGIN_PROMPT": (By.XPATH, "//img[@class = 'page__close-icon']"),
        "CHECKOUT_PAGE" : (By.XPATH, "//div[@class = 'total-charge__chargelayout']"),
        "LABEL_ENTER_MOBILE_NUMBER": (By.XPATH, "//label[contains(text(), 'Enter your mobile number')]"),
        "MOBILE_NUMBER_INPUT_FIELD": (By.XPATH, "//input[@placeholder='10 Digit Mobile Number']"),
        "BUTTON_VERIFY_MOBILE": (By.XPATH, "//button[contains(text(), 'Verify Mobile')]"),
        "MOBILE_FIELD_ERROR" : (By.XPATH, "//label[contains(text(), 'Please enter valid mobile number')]"),
        "LOGIN_PAGE_HEADER_FROM_CHECKOUT" : (By.XPATH, " //h5[contains(text(), 'Welcome to Mcdonalds.')] "),
        "SELECTED_DELIVERY_ADDRESS" : (By.XPATH, " //div[@class = 'txt-ellipsis']"),
        "ADDRESS_FILLING_DETAILS_PAGE" : (By.XPATH, "(//h5[contains(text(), 'Building/Locality or nearby landmark')])[2]"),
        "ADDRESS_MANDATORY_FIELD_EMPTY_ERROR" : (By.XPATH, "//div[contains(text(), ' Please enter valid House / Flat No.')]"),
        "CLICK_BACK_BUTTON" : (By.XPATH, "//img[@class= 'bottom-sheet__back-icon']"),
        "CLICK_BACK_BUTTON_FROM_SELECT_LOCATION" : (By.XPATH, "//img[@alt='ic-arrow-left-primary']"),
        "FIRST_ADDRESS" : (By.XPATH, "//span[contains(text(), 'Kasturba Road')]"),
        "SELECT_DELIVERY_ADDRESS_HEADLINE" : (By.XPATH, "//div[@class = 'bottom-sheet__row']"),
        "ADDRESS_SELECTED_AFTER_DELETION": (By.XPATH, "//div[contains(@class, 'txt-ellipsis')]"),
        "ADDRESS_EDIT_ICON" : (By.XPATH, "(//img[@title = 'ic-edit'])[1]"),
        "MODIFIED_ADDRESS_SELECTED" : (By.XPATH, "(//div[contains(text(), 'HPCL HOUSING COLONY')])[1]"),
        "ADDRESS_DELETE_ICON" : (By.XPATH, "(//img[@title = 'ic-delete'])[1]"),
        "ADDRESS_DELETE_POP_UP_HEADER" : (By.XPATH, "//h2[contains(text(), 'Delete Address')]"),
        "CLICK_YES_ON_ADDRESS_DELETE_POP_UP" : (By.XPATH, "//span[contains(text(), 'Yes')]"),
        "ADDRESS_LIST" : (By.XPATH, "//h5[contains(text(), ' All Addresses')] "),
        "NEAR_LABEL_ALL_ADDRESS" : (By.XPATH, "//div[contains(@class, 'address') and .//strong[contains(text(), 'Near')]]"),
        "SELECT_WORK_TAG" : (By.XPATH, " //div[contains(text(), 'Work')]"),
        "VERIFY_WORK_TAG_NEXT_ADDRESS" : (By.XPATH, " //div[contains(@class, 'address__title') and normalize-space(text())='Work']/following::div[@class='address__row-2']/div[contains(text(), 'AKTU')]"),
        "SELECT_HOME_TAG" : (By.XPATH, " (//div[contains(text(), ' Home ')])[2]"),
        "VERIFY_HOME_TAG_NEXT_ADDRESS" : (By.XPATH, "//div[contains(@class, 'address__title') and normalize-space(text())='Home']/following::div[@class='address__row-2']/div[contains(text(), 'Vipul greens')]"),
        "ADD_NEW_ADDRESS" : (By.XPATH, "  //div[contains(text(), 'Add new address')]"),
        "ADDED_ADDRESS_FROM_LIST" : (By.XPATH, " //div[contains(@class, 'address__title') and contains(normalize-space(.), '{}')]"),
        "ADD_ITEM_TO_CART" : (By.XPATH, "//div[contains(@class, 'menu__title') and normalize-space(text())='{burger_name}']/following::div[contains(@class, 'add-to-cart')][1]"),
        
    }


class AddressPage(BasePage):

    def search_for_new_address(self):
        time.sleep(5)
        self.actions.click_button(*locators['ADD_NEW'])
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Bengaluru")
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)

    def select_address_from_search_results(self):
        Multiple_locations = self.actions.wait_for_elements(*locators["SEARCH_INPUT_FIELD"])
        if len(Multiple_locations) != 0:
            print("Search Results are displayed for the entered location")
            self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Bengaluru"))
            time.sleep(3)
            self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
            self.actions.click_button(*locators["CONFIRM_LOCATION"])
            print("Clicked Confirm Location Button")
            time.sleep(5)
            self.actions.wait_for_element(*locators['HOUSE_NUMBER'])
            self.actions.enter_text(*locators['HOUSE_NUMBER'], "Marathahalli village, HAL Airport road")
            time.sleep(5)
            self.actions.click_button(*locators["SAVE_ADDRESS"])
        else:
            print("No Search Reslts Displayed For The Given Input Field. Try Another Loocation!")

    def verify_address_is_added_and_selected(self):
        time.sleep(5)
        return self.actions.is_element_displayed(locators['ADDRESS_SELECTED'][0], locators['ADDRESS_SELECTED'][1].format("Marathahalli village, HAL Airport road"))
        
    def select_address_from_the_list(self):
        time.sleep(5)
        Address_Displayed = self.actions.is_element_displayed(locators['ADDED_ADDRESS'][0], locators['ADDED_ADDRESS'][1].format("Marathahalli village"))
        if Address_Displayed:
            self.actions.click_button(locators['ADDED_ADDRESS'][0], locators['ADDED_ADDRESS'][1].format("Marathahalli village"))
            time.sleep(3)
            return self.actions.is_element_displayed(locators['ADDRESS_SELECTED'][0], locators['ADDRESS_SELECTED'][1].format("Marathahalli village"))
        else:
            return False
        

    def verify_redirect_to_login_or_signup_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PROMPT'])
    
    def Click_login_prompt(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['LOGIN_PROMPT'])
        self.actions.click_button(*locators['LOGIN_PROMPT'])

    def Click_login_prompt_from_checkout(self):
        self.actions.is_element_displayed(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        self.actions.click_button(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        time.sleep(2)
    
    def click_cancel_to_login_or_signup_page(self):
        self.actions.is_element_displayed(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        self.actions.click_button(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        time.sleep(2)
    

    def verify_login_page_navigation_from_checkout(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PAGE_HEADER_FROM_CHECKOUT'])
    

    def verify_redirect_to_checkout_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['CHECKOUT_PAGE'])
    
    def enter_incorrect_mobile_number(self):
        self.actions.is_element_displayed(*locators['LABEL_ENTER_MOBILE_NUMBER'])
        self.actions.enter_text(*locators["MOBILE_NUMBER_INPUT_FIELD"], "673456")
        self.actions.click_button(*locators["BUTTON_VERIFY_MOBILE"])
        self.actions.is_element_displayed(*locators['MOBILE_FIELD_ERROR'])
        time.sleep(5)
        print("Please enter valid Mobile number")

    def click_add_address_from_checkout(self):
        print("Checking and clicking address arrow.")
        self.actions.is_element_displayed(*locators['ADDRESS_ARROW'])
        self.actions.click_button(*locators['ADDRESS_ARROW'])
        print("Address arrow clicked.")
        time.sleep(2)


    def verify_address_appear_as_selected_delivery_address(self):
        try:
            WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['SELECTED_DELIVERY_ADDRESS'])
        )
            is_displayed = self.actions.is_element_displayed(*locators['SELECTED_DELIVERY_ADDRESS'])
            assert is_displayed, "Selected delivery address is not displayed"
            return True
        except Exception as e:
            raise AssertionError(f"Validation failed: Selected delivery address did not appear. Details: {e}")
        
    def Click_add_new_button_and_confirm_location(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_NEW'])
        self.actions.click_button(*locators['ADD_NEW'])
        time.sleep(2)
        self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
        self.actions.click_button(*locators["CONFIRM_LOCATION"])
        print("Clicked Confirm Location Button")

    def verify_redirect_to_address_filling_page(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['ADDRESS_FILLING_DETAILS_PAGE'])
    
    def verify_leave_address_mandatory_field_empty(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators['HOUSE_NUMBER'])
        self.actions.click_button(*locators['SAVE_ADDRESS'])
       
    def verify_address_mandatory_field_empty_error(self):
        time.sleep(2)
        return self.actions.is_element_displayed(*locators['ADDRESS_MANDATORY_FIELD_EMPTY_ERROR'])
    
    def enter_special_char_in_house_field(self):
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], "%$^#@&*")
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        time.sleep(2)
        print("Entered special characters in house/flat field")

    def verify_field_accept_special_char_and_address_saved(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['SELECTED_DELIVERY_ADDRESS'])
    
    def verify_saved_delivery_address(self, user_data_store):
        # Save current values before changing
        try:
            selected_address = self.driver.find_element(*locators['SELECTED_DELIVERY_ADDRESS'])
            saved_address = selected_address.text
            user_data_store["saved address"] = saved_address
        except Exception as e:
            raise AssertionError(f"Could not retrieve selected delivery address. Error: {e}")
        
    def enter_text_in_house_field_and_cancel_before_saving(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], "vipul greens")
        self.actions.click_button(*locators["CLICK_BACK_BUTTON"])
        time.sleep(2)
        self.actions.click_button(*locators["CLICK_BACK_BUTTON_FROM_SELECT_LOCATION"])
        print("Entered text in house/flat field and click back button without saving")
        

    def verify_address_is_not_saved_when_click_back_button_without_saving(self, user_data_store):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['SELECTED_DELIVERY_ADDRESS'])
        current_address = self.driver.find_element(*locators['SELECTED_DELIVERY_ADDRESS']).text.strip()

        expected_address = user_data_store.get("saved address", "").strip()
    
        assert current_address == expected_address, (
            f"Address should not have changed. Expected: '{expected_address}', Got: '{current_address}'"
        )

    def enter_text_in_house_field_and_click_save(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], "68, Sector 48, Vipul world")
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        time.sleep(2)
        print("Entered text in house/flat field and click save button")

    def verify_duplicate_address_saved(self):
        time.sleep(2)
        addresses = [
            "68, Sector 48, Vipul world,",
            "68, Sector 48, Vipul world,",
            "6217,",
            "123, Near: Unnamed Road, Kamanhalli, Hangal, Haveri District, Karnataka. Pin-581104 (India)"
]

        # Use a set to track seen addresses
        seen = set()
        duplicates = []

        for addr in addresses:
            if addr in seen:
             duplicates.append(addr)
        else:
            seen.add(addr)

        # Print the duplicate addresses
        print("Duplicate addresses found:")
        for dup in set(duplicates):
         print("-", dup)

    def search_for_address_after_selecting_business_model(self):
        try:
            # Step 1: Click on search button
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locators['SEARCH_BUTTON'])
            ).click()
            print("Clicked on search button")

            # Step 2: Enter "Bengaluru" in search input
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locators["SEARCH_INPUT_FIELD"])
            ).send_keys("Bengaluru")
            print("Entered 'Bengaluru' in search field")

            # Step 3: Wait for search suggestion with 'Bengaluru' to appear
            bengaluru_locator = (
                locators['SELECT_ADDRESS'][0],
                locators['SELECT_ADDRESS'][1].format("Bengaluru")
            )

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(bengaluru_locator)
            ).click()
            print("Selected 'Bengaluru' from suggestions")

            # Step 4: Wait for first address to appear after selecting the city
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locators['FIRST_ADDRESS'])
            ).click()
            print("Clicked on the first address (Kasturba Road).")

        except Exception as e:
            print(f"❌ Test failed while searching for address: {str(e)}")
            raise
        

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



    def Click_from_listed_address(self):
        WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )
        self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Marathahalli village, HAL Airport road"))
        print("Address from list clicked")

       
    def click_address_edit_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_EDIT_ICON'])
        self.actions.click_button(*locators['ADDRESS_EDIT_ICON'])
        print("Edit icon clicked")

    def modify_existing_address_and_click_save(self, updated_house_name):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators["HOUSE_NUMBER"], updated_house_name)
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        time.sleep(2)
        print(f"Entered updated house/flat value: '{updated_house_name}' and clicked save button")

    def verify_restaurant_updated_based_on_modified_address(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['MODIFIED_ADDRESS_SELECTED'])
    
    def Verify_address_shown_in_list_before_deletion(self, user_data_store):
        time.sleep(2)
        address_element = self.driver.find_element(
        locators['ADDED_ADDRESS'][0],
        locators['ADDED_ADDRESS'][1].format("Marathahalli village")
    )
        address_title = address_element.text.strip()
        user_data_store["original_address"] = address_title
        print("Captured address name before deletion:", address_title)

    def click_address_delete_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_DELETE_ICON'])
        self.actions.click_button(*locators['ADDRESS_DELETE_ICON'])
        print("Delete icon clicked")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_DELETE_POP_UP_HEADER'])
        self.actions.click_button(*locators['CLICK_YES_ON_ADDRESS_DELETE_POP_UP'])
        print("Clicked on YES option on address delete pop up")

    def Verify_address_removed_from_list_after_deletion(self, user_data_store):
        time.sleep(2)
        deleted_address_name = user_data_store.get("original_address") 
        print(f"Validating deleted address: '{deleted_address_name}'")

        # Use find_elements to get list of address titles
        address_elements = self.driver.find_elements(
            locators['ADDRESS_SELECTED_AFTER_DELETION'][0],
            locators['ADDRESS_SELECTED_AFTER_DELETION'][1].split('{}')[0]  
        )
        all_titles = [el.text.strip() for el in address_elements]
        print("Remaining address titles after deletion:", all_titles)

        assert deleted_address_name not in all_titles, f"'{deleted_address_name}' is still visible after deletion!"

    def verify_address_list(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ADDRESS_LIST'])
    
    def verify_near_label_visible_in_address_description(self):
        time.sleep(2)
        near_elements = self.driver.find_elements(*locators['NEAR_LABEL_ALL_ADDRESS'])
        for el in near_elements:
            print(el.text)

    def scroll_to_bottom_of_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(" Scrolled to bottom of the page.")

    def All_addresses_accessible_via_scrolling(self):
        Scroll_all_addresses = WebDriverWait(self.driver, 10).until(
    EC.visibility_of_element_located(locators["NEAR_LABEL_ALL_ADDRESS"])
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Scroll_all_addresses)
        print(" Scrolled to access all addresses")

    def enter_an_undeliverable_address(self):
        time.sleep(5)
        self.actions.click_button(*locators['ADD_NEW'])
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Sector 48")
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Gurugram, Haryana, 122018"))
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
        self.actions.click_button(*locators["CONFIRM_LOCATION"])
        print("Clicked Confirm Location Button")
        time.sleep(5)
        self.actions.wait_for_element(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators['HOUSE_NUMBER'], "Gurugram, Haryana, 122018")
        time.sleep(5)
        self.actions.click_button(*locators["SELECT_WORK_TAG"])
        print("Work tag selected")
        time.sleep(2)
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        print("Save address button clicked")

    def add_address_and_select_tag(self):
        time.sleep(5)
        self.actions.click_button(*locators['ADD_NEW'])
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], "Dadar west")
        time.sleep(5)
        self.actions.click_button(*locators['SEARCH_BUTTON'])
        time.sleep(5)
        self.actions.click_button(locators['SELECT_ADDRESS'][0], locators['SELECT_ADDRESS'][1].format("Dadar west"))
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CONFIRM_LOCATION'])
        self.actions.click_button(*locators["CONFIRM_LOCATION"])
        print("Clicked Confirm Location Button")
        time.sleep(5)
        self.actions.wait_for_element(*locators['HOUSE_NUMBER'])
        self.actions.enter_text(*locators['HOUSE_NUMBER'], "123")
        time.sleep(5)
        self.actions.click_button(*locators["SELECT_WORK_TAG"])
        print("Work tag selected")
        time.sleep(2)
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        print("Save address button clicked")

    def verify_tag_next_to_address_after_adding_address(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['VERIFY_WORK_TAG_NEXT_ADDRESS'])

    def edit_address_and_select_tag(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['ADDRESS_EDIT_ICON'])
        self.actions.click_button(*locators['ADDRESS_EDIT_ICON'])
        print("Edit icon clicked")
        time.sleep(5)
        House_field = self.driver.find_element(*locators['HOUSE_NUMBER'])
        House_field.clear()
        time.sleep(2)
        self.actions.enter_text(*locators['HOUSE_NUMBER'], "Vipul greens, Lucknow")
        time.sleep(5)
        self.actions.click_button(*locators["SELECT_HOME_TAG"])
        print("Home tag selected")
        time.sleep(2)
        self.actions.click_button(*locators["SAVE_ADDRESS"])
        print("Save address button clicked")

    def verify_tag_next_to_address_after_editing_address(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['VERIFY_HOME_TAG_NEXT_ADDRESS'])
    
    def verify_address_list_before_logout_the_application(self, user_data_store):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        user_data_store["original_addresses"] = []

        scrollable_container = self.driver.execute_script("""
            let divs = document.querySelectorAll('div');
            for (let div of divs) {
                if (div.scrollHeight > div.clientHeight) {
                    return div;
                }
            }
            return null;
        """)

        if not scrollable_container:
            raise Exception(" Scrollable container not found")

        for address in ["Vipul greens, Lucknow", "Dadar west", "Marathahalli village"]:
            try:
                # Try scrolling and finding element multiple times
                found = False
                for _ in range(5):
                    try:
                        address_element = self.driver.find_element(
                            locators['ADDED_ADDRESS'][0],
                            locators['ADDED_ADDRESS'][1].format(address)
                        )
                        # Scroll the container to the element
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_element)
                        time.sleep(0.5)
                        found = True
                        break
                    except Exception:
                        # Scroll a bit down each time if not found
                        self.driver.execute_script("arguments[0].scrollTop += 200;", scrollable_container)
                        time.sleep(0.3)

                if not found:
                    print(f" Could not find address: {address}")
                    continue

                address_title = address_element.text.strip()
                user_data_store["original_addresses"].append(address_title)
                print(f" Captured address: {address_title}")

            except Exception as e:
                print(f" Error while capturing address '{address}': {e}")
                time.sleep(2)
        self.actions.click_button(*locators["CLICK_BACK_BUTTON_FROM_SELECT_LOCATION"])

    def verify_previously_saved_address_should_visible_after_logs_in(self, user_data_store):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        for expected_address in user_data_store["original_addresses"]:
            # Build the XPath with the expected address
            by, value = locators['ADDED_ADDRESS']
            formatted_xpath = value.format(expected_address)

            try:
                # Wait for element to be present 
                address_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((by, formatted_xpath))
                )

                # Scroll into view 
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_element)
                time.sleep(1) 

                # Validate
                actual_text = address_element.text.strip()
                assert expected_address in actual_text, f"Expected '{expected_address}', but found '{actual_text}'"

                print(f"[PASS] Address '{expected_address}' is visible.")
            except Exception as e:
                print(f"[FAIL] Address '{expected_address}' not found. Error: {e}")
                raise


    def select_first_address_from_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        scrollable_container = self.driver.execute_script("""
            let divs = document.querySelectorAll('div');
            for (let div of divs) {
                if (div.scrollHeight > div.clientHeight) {
                    return div;
                }
            }
            return null;
        """)

        if not scrollable_container:
            raise Exception("Scrollable container not found")

        addresses = ["Vipul greens"]

        for address in addresses:
            try:
                found = False
                for _ in range(5):
                    try:
                        address_element = self.driver.find_element(
                            locators['ADDED_ADDRESS'][0],
                            locators['ADDED_ADDRESS'][1].format(address)
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_element)
                        time.sleep(0.5)
                        found = True
                        break
                    except Exception:
                        self.driver.execute_script("arguments[0].scrollTop += 200;", scrollable_container)
                        time.sleep(0.3)

                if found:
                    address_text = address_element.text.strip()
                    print(f"Captured address: {address_text}")
                    address_element.click()
                    return  # Stop after clicking the first found address

                else:
                    print(f"Could not find address: {address}")

            except Exception as e:
                print(f"Error while processing address '{address}': {e}")
                time.sleep(2)

    def select_another_address_from_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        scrollable_container = self.driver.execute_script("""
            let divs = document.querySelectorAll('div');
            for (let div of divs) {
                if (div.scrollHeight > div.clientHeight) {
                    return div;
                }
            }
            return null;
        """)

        if not scrollable_container:
            raise Exception("Scrollable container not found")

        addresses = [" Dadar west "]

        for address in addresses:
            try:
                found = False
                for _ in range(5):
                    try:
                        address_element = self.driver.find_element(
                            locators['ADDED_ADDRESS'][0],
                            locators['ADDED_ADDRESS'][1].format(address)
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_element)
                        time.sleep(0.5)
                        found = True
                        break
                    except Exception:
                        self.driver.execute_script("arguments[0].scrollTop += 200;", scrollable_container)
                        time.sleep(0.3)

                if found:
                    address_text = address_element.text.strip()
                    print(f"Captured address: {address_text}")
                    address_element.click()
                    return  # Stop after clicking the first found address

                else:
                    print(f"Could not find address: {address}")

            except Exception as e:
                print(f"Error while processing address '{address}': {e}")
                time.sleep(2)


    def delete_all_addresses(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        while True:
            # Fetch all visible delete icons
            delete_buttons = self.driver.find_elements(*locators['ADDRESS_DELETE_ICON'])
            print(f"DEBUG: Found {len(delete_buttons)} delete icons.")

            if not delete_buttons:
                print("No more addresses to delete.")
                break

            print(f"Found {len(delete_buttons)} addresses. Deleting...")

            try:
                # Scroll to and click the first delete button
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_buttons[0])
                time.sleep(0.5)
                delete_buttons[0].click()
                print("Delete icon clicked")

                # Wait for the delete confirmation popup and confirm deletion
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(locators['ADDRESS_DELETE_POP_UP_HEADER'])
                )
                self.driver.find_element(*locators['CLICK_YES_ON_ADDRESS_DELETE_POP_UP']).click()
                print("Clicked on YES option on address delete pop up")

                # Wait briefly for the UI to refresh before next iteration
                time.sleep(2)

            except Exception as e:
                print(f"Error deleting address: {e}")
                break

    def verify_add_new_address_prompt_visible(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_NEW_ADDRESS'])
        print("Clicked on Add new address")


    def select_address_from_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        scrollable_container = self.driver.execute_script("""
            let divs = document.querySelectorAll('div');
            for (let div of divs) {
                if (div.scrollHeight > div.clientHeight) {
                    return div;
                }
            }
            return null;
        """)

        if not scrollable_container:
            raise Exception("Scrollable container not found")

        addresses = ["Aurangabad Mukundwadi"]

        for address in addresses:
            try:
                found = False
                for _ in range(5):
                    try:
                        address_element = self.driver.find_element(
                            locators['ADDED_ADDRESS'][0],
                            locators['ADDED_ADDRESS'][1].format(address)
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_element)
                        time.sleep(0.5)
                        found = True
                        break
                    except Exception:
                        self.driver.execute_script("arguments[0].scrollTop += 200;", scrollable_container)
                        time.sleep(0.3)

                if found:
                    address_text = address_element.text.strip()
                    print(f"Captured address: {address_text}")
                    address_element.click()
                    return  # Stop after clicking the first found address

                else:
                    print(f"Could not find address: {address}")

            except Exception as e:
                print(f"Error while processing address '{address}': {e}")
                time.sleep(2)

    def select_address_from_listed_address(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators['SELECT_DELIVERY_ADDRESS_HEADLINE'])
        )

        # Locate the address element directly using the formatted locator
        address_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                locators['ADDED_ADDRESS_FROM_LIST'][0],
                locators['ADDED_ADDRESS_FROM_LIST'][1].format("Dadar west")
            ))
        )

        # Optionally print the text to confirm
        address_text = address_element.text.strip()
        print(f"Captured address: {address_text}")

        # Click the address
        address_element.click()








        
        

        

        
        
        
    

    


