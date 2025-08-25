from pages.base_page import BasePage
from pages.android_view_screen import AndroidViewScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "HOME_ICON": (AppiumBy.XPATH, "//android.widget.TextView[@text='Home']"),
        "MYMCD_TEXT": (AppiumBy.XPATH, "//android.widget.TextView[@text='MyMcD']"),
        "HAMBURGER_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bottom-tab-mymcd']"),
        "MYMCD_LOGO": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-MyMcD_Logo']"),
        "MENU_TITLE": (By.XPATH, "//h4[@class='menu__title']"),
        "CONFIRM_ADD_TO_CART": (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
        "CART_LIST": (By.XPATH, "//div[@class='cart-details__card-list']"),
        "VIEW_CART": (By.XPATH, "//div[@class='cart-status-bar__cta' and contains(text(), 'View Cart')]"),
        "MCDELIVERY_OPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='McDelivery']"),
        "DINE_IN_OPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Dine-In']"),
        "ON_THE_GO_OPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='On the Go']"),
        "TAKE_AWAY_OPTION": (AppiumBy.XPATH, "//android.widget.TextView[@text='Take Away']"),
        "MCDELIVERY_ORDERING_PAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='No address selected']"),
        "DINE_IN_LOCATION_PAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='No store selected']"),
        "ON_THE_GO_LOCATION_PAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Store based on your Current Location']"),
        "TAKE_AWAY_LOCATION_PAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='No store selected']"),
        "TOAST_MESSAGE_LOCATION_ENABLED": (By.XPATH, "//div[contains(@class, 'toast') and contains(text(), 'Sorry')]"),
        "SEARCH_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bottom-tab-search']"),
        "SEARCH_MENU": (AppiumBy.XPATH, "//android.widget.EditText"),
        "SEARCH_MENU_ICON": (AppiumBy.XPATH, "(//android.widget.Image[@text='ic-search'])[1]"),
        "BURGER_NAME": (AppiumBy.XPATH, "//android.widget.TextView[@text='McVeggie Burger']"),
        "ADD_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-add']"),
        "ADD_TO_CART_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Add to Cart']"),
        "ADD_ADDRESS": (AppiumBy.XPATH, "//android.widget.TextView[@text='No address selected']"),
        "ADDRESS_DROP_DOWN": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-arrow-down']"),
        "MCDELIVERY_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bm-delivery-active']"),
        "DINE_IN_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bm-dine-in']"),
        "ON_THE_GO_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bm-otg']"),
        "TAKE_AWAY_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bm-delivery']"),
        "TOAST_MESSAGE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Sorry, we do not serve this location yet']"),
        "UNDELIVERABLE_AREA_MESSAGE": (AppiumBy.XPATH, "//android.widget.Image[@text='_banner1_img']"),
        "NO_STORES_NEAR_BY": (AppiumBy.XPATH, "//android.widget.TextView[@text='No stores nearby']"),
        "HOME_PAGE_ADDRESS": (AppiumBy.XPATH, "(//android.widget.TextView[@text='Home'])[1]"),
        "STORE_AVAILABLE": (AppiumBy.XPATH, "//android.widget.TextView[@text='Mantri Mall']"),
        "OPEN": (AppiumBy.XPATH, "//android.widget.TextView[@text='Open']"),
        "MENU_ICON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-bottom-tab-menu']"),

         }


class AndroidHomeScreen(BasePage):

    def verify_home_screen_navigation(self):
        try:
            by, locator = locators['HOME_ICON']
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((by, locator))
            )
            return True
        except Exception as e:
            print(f"[ERROR] Home icon not found: {e}")
            self.driver.save_screenshot("home_screen_failure.png")
            return False

    
    def click_on_MyMcD_hamburger_icon(self):
        time.sleep(10)
        self.actions.is_element_displayed(*locators['HAMBURGER_ICON'])
        time.sleep(5)
        self.actions.click_button(*locators["HAMBURGER_ICON"])
        time.sleep(1)
        print("Clicked on MyMcD hamburger icon")

    def click_on_Menu_icon(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MENU_ICON'])
        self.actions.click_button(*locators["MENU_ICON"])
        time.sleep(1)
        print("Clicked on Menu icon")

    def verify_displays_of_all_business_model(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        print("Mcdelivery displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        print("Dine-In displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['ON_THE_GO_OPTION'])
        print("On the Go displayed on business model dropdown")
        self.actions.is_element_displayed(*locators['TAKE_AWAY_OPTION'])
        print("Take Away displayed on business model dropdown")

    def verify_McDelivery_option(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        self.actions.click_button(*locators['MCDELIVERY_OPTION'])
        print("Clicked on McDelivery from dropdown")

    def verify_user_redirect_to_McDelivery_ordering_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['MCDELIVERY_ORDERING_PAGE'])

    def verify_Dine_In_option(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        self.actions.click_button(*locators['DINE_IN_OPTION'])
        print("Clicked on Dine-In from dropdown")

    def verify_user_redirect_to_Dine_In_location_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['DINE_IN_LOCATION_PAGE'])
    
    def verify_On_the_go_option(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ON_THE_GO_OPTION'])
        self.actions.click_button(*locators['ON_THE_GO_OPTION'])
        print("Clicked On the go from dropdown")
    
    def verify_user_redirect_to_On_the_go_pick_up_location_flow(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['ON_THE_GO_LOCATION_PAGE'])
    
    def verify_take_away_option(self):
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

    def click_on_search_icon_in_home_screen(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['SEARCH_ICON'])
        self.actions.click_button(*locators["SEARCH_ICON"])
        time.sleep(5)
        print("Clicked on search icon")

    def click_on_add_address_in_home_screen(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['ADD_ADDRESS'])
        self.actions.click_button(*locators["ADDRESS_DROP_DOWN"])
        time.sleep(5)
        print("Clicked on add address drop down icon")

    def verify_Dine_In_selected_until_manually_changed(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        print("Dine In selected after browsing menu and returning back to homepage")

    def verify_location_popup(self):
        try:
            toast_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Unable to access the location')]"))
            )
            print("Toast message found:", toast_element.text)
        except Exception as e:
            print("Toast message not found:", e)

    def step_check_only_one_active(self):
        wait = WebDriverWait(self.driver, 10)
        active_models = []

        highlight_xpaths = {
            "DINE_IN_OPTION": "//android.widget.Image[@text='ic-bm-dine-in-active']",
            "TAKE_AWAY_OPTION": "//android.widget.Image[@text='ic-bm-delivery-active']"
        }

        for key, highlight_xpath in highlight_xpaths.items():
            try:
                element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, highlight_xpath)))
                if element.is_displayed():
                    print(f"{key} is active")
                    active_models.append(key)
            except (TimeoutException, NoSuchElementException):
                print(f"{key} is not active")
            except StaleElementReferenceException:
                print(f"{key}: stale element exception")

        print(f"Total active models found: {len(active_models)}")
        assert len(active_models) == 1, f"Expected 1 active model, found {len(active_models)}"

    def verify_icons_display_on_each_business_model(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['MCDELIVERY_ICON'])
        print("Mcdelivery text is displayed with icon")
        self.actions.is_element_displayed(*locators['DINE_IN_ICON'])
        print("Dine-In text is displayed with icon")
        self.actions.is_element_displayed(*locators['ON_THE_GO_ICON'])
        print("On the Go text is displayed with icon")
        self.actions.is_element_displayed(*locators['TAKE_AWAY_ICON'])
        print("Take Away text is displayed with icon")

    def verify_switching_from_one_model_to_another(self):
        time.sleep(2)
        self.actions.is_element_displayed(*locators['DINE_IN_OPTION'])
        self.actions.click_button(*locators['DINE_IN_OPTION'])
        time.sleep(2)
        self.actions.is_element_displayed(*locators['MCDELIVERY_OPTION'])
        self.actions.click_button(*locators['MCDELIVERY_OPTION'])

    def show_toast(self):
        try:
            toast = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locators['TOAST_MESSAGE'])
            )
            web_toast_message = toast.get_attribute("text").strip()
            expected_message = "Sorry, we do not serve this location yet"

            if web_toast_message == expected_message:
                print("Toast message matches.")
            else:
                print(f"Toast message not matched: '{web_toast_message}'")

        except Exception as e:
            print(f"Toast message not found: {e}")

    def verify_error_message_for_undeliverable_address(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['UNDELIVERABLE_AREA_MESSAGE'])
        self.actions.is_element_displayed(*locators['NO_STORES_NEAR_BY'])
        print("No stores nearby is displayed")
    
    def verify_address_selected_and_restaurant_updated_accordingly(self):
        time.sleep(5)
        self.actions.is_element_displayed(*locators['HOME_PAGE_ADDRESS'])
        self.actions.is_element_displayed(*locators['STORE_AVAILABLE'])
        print("Mantri mall store is displayed")
        self.actions.is_element_displayed(*locators['OPEN'])
        print("Open is displayed with timimg")
    
    def verify_recently_used_address_is_auto_selected_after_login(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['HOME_PAGE_ADDRESS'])


    