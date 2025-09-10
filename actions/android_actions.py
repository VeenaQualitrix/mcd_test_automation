import random
import pytest
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from actions.actions_parent import ActionsParent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.interaction import KEY
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from conftest import readConstants


class AndroidActions(ActionsParent):

    def __init__(self, driver):
        self.driver = driver
        self.ultra_wait = WebDriverWait(self.driver, readConstants("ULTRA_WAIT"))
        self.short_wait = WebDriverWait(self.driver, readConstants("SHORT_WAIT"))
        print("long wait ===", readConstants("LONG_WAIT"))
        self.wait = WebDriverWait(self.driver, readConstants("DEFAULT_WAIT"))
        self.long_wait = WebDriverWait(self.driver, readConstants("LONG_WAIT"))
        self.super_wait = WebDriverWait(self.driver, readConstants("SUPER_WAIT"))
        self.dynamic_number = random.randint(1, 10000)


    def launch_app(self):
        print("Application launch is handled in conftest fixture")


    def relaunch_app(self, appPackage):
        print("Application is already Launched. Relaunching application again")
        self.driver.activate_app(appPackage)

    def fluentWaitNew(self, ele, secs):
        WebDriverWait(self.driver, 60, poll_frequency=secs).until(EC.visibility_of_element_located(ele), 'Error')

    def screenshotAttachment(self, ScreenshotName):
        doIneedScreenshot = readConstants("NEED_SCREENSHOTS_FOR_PASS")
        if str(doIneedScreenshot).lower() == 'true':
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenshotName, attachment_type=AttachmentType.PNG)

    def wait_for_element(self, locator, value, timeout=60):
        """
        Waits for an element to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        print("Waiting for Element", value)
        again = 1
        while again < 3:
            try:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None
            except StaleElementReferenceException:
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutError:
                again = 3
                print("Element not present")
                return self.driver

    def wait_for_elements(self, locator, value, timeout=60):
        """
        Waits for all elements to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        print("Waiting for Element", timeout)
        again = 1
        while again < 3:
            try:
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None
            except StaleElementReferenceException:
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutException:
                again = 3
                print("TimeoutException: Element not present")
                return None
            except Exception:
                print("Exception occured")

    def enter_text(self, locator_type, locator_value, text):
        """
        Enters text into an input field identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        text - Text to enter into the input field.
        """
        print("passing locator_type", locator_type)
        try_count = 1
        while try_count < 5:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((locator_type, locator_value)))
                #self.screenshotAttachment("element_before_clear_{}.jpg".format(self.dynamic_number))
                element.clear()
                #self.screenshotAttachment("element_cleared.jpg_{}.jpg".format(self.dynamic_number))
                element.send_keys(text)
                #self.screenshotAttachment("element_dataset_{}.jpg".format(self.dynamic_number))
                break
            except TimeoutException:
                #self.screenshotAttachment("element_not_found_Timeout_Exception.jpg")
                print("Element Is Not Found To Perform Click Action Due To Timeout, Trying again after 2 seconds")
                try_count = try_count + 1
            except NoSuchElementException:
                #self.screenshotAttachment("element_not_found_NoSuchElementException.jpg")
                print("Element Is Not Found To Perform Click Action Due To NoSuchElementException, Trying again after 2 seconds")
                try_count = try_count + 1
            except ElementClickInterceptedException:
                #self.screenshotAttachment("element_not_clickable.jpg")
                print("Click was itercepted, Trying again after 2 seconds")
            except StaleElementReferenceException:
                print("Stale element, refreshed, trying again")
                try_count += 1

    def click_button(self, locator_type, locator_value):
        """
        Clicks a button identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        """
        print(f"Attempting to click element using locator: {locator_type}, {locator_value}")

        try_count = 1
        max_retries = 2

        while try_count <= max_retries:
            try:
                # Correct use of WebDriverWait with locator tuple
                element = self.long_wait.until(
                    EC.element_to_be_clickable((locator_type, locator_value))
                )
                element.click()
                print(f"Clicked element on attempt #{try_count}")
                return
            except TimeoutException:
                print(f"[{try_count}] TimeoutException: Element not clickable, retrying...")
            except NoSuchElementException:
                print(f"[{try_count}] NoSuchElementException: Element not found, retrying...")
            except ElementClickInterceptedException:
                print(f"[{try_count}] ElementClickInterceptedException: Intercepted, retrying...")
            except StaleElementReferenceException:
                print(f"[{try_count}] StaleElementReferenceException: Stale reference, retrying...")

            try_count += 1
            time.sleep(2)  # Important wait between retries

        raise Exception(f"Failed to click element after {max_retries} attempts: {locator_type}, {locator_value}")

    def close_app(self):
        """
        Closes the application.
        """
        self.driver.close_app()

    def open_app(self):
        """
        Opens the application.
        """
        self.driver.launch_app()

    def quit_Driver(self):
        self.driver.quit()

    def open_url(self, url):
        """
        Opens the specified URL in the web browser.
        Arguments:
        url - The URL to open in the web browser.
        """
        self.driver.get(url)

    def maximize_Window(self):
        """
        Maximizes the window
        """
        self.driver.maximize_window()

    def get_text(self, locator_type, locator_value):
        """
        Retrieves the text of an element identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : string - The text content of the located element.
        """
        try_count = 1
        while try_count < 5:
            try:
                self.long_wait.until(EC.presence_of_element_located((locator_type, locator_value)))
                time.sleep(10)
                element = self.driver.find_element(locator_type, locator_value)
                #self.screenshotAttachment("element_gettingText_{}.jpg".format(self.dynamic_number))
                print("fetching text from app ====", element.text)
                return element.text
                break
            except NoSuchElementException:
                #self.screenshotAttachment("element_not_found.jpg")
                print("Click was itercepted to get_text, Trying again after 2 seconds")
                try_count = try_count + 1
            except StaleElementReferenceException:
                print("Stale element, refreshed, trying again")
                try_count += 1

    def suspend_app(self, seconds):
        """
        Suspends the app for a specified duration.
        Arguments:
        seconds - Duration to suspend the app, in seconds.
        """
        self.driver.background_app(seconds)

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        Performs a swipe gesture from one coordinate to another.
        Arguments:
        start_x - Starting X coordinate.
        start_y - Starting Y coordinate.
        end_x - Ending X coordinate.
        end_y - Ending Y coordinate.
        duration - Duration of the swipe in milliseconds (default is 800).
        """
        #self.screenshotAttachment("element_before_swipe_{}.jpg".format(self.dynamic_number))
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] / 2
        end_x = end_x
        end_y = end_y
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        #self.screenshotAttachment("element_after_swipe.jpg")

    def validate_element_visitbilty_within_time(self, locator_type, locator_value, duration):
        """
        Checks if an element is visible within the specified time frame.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        duration - Maximum time to wait for visibility, in seconds.
        Returns : True if the element is visible within the duration; False otherwise.
        """
        start_time = time.time()  # Record the start time
        try:
            # Wait up to 30 seconds for the element to be visible
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            end_time = time.time()  # Record the end time
            load_time = end_time - start_time
            print("Element loaded in: {:.2f} seconds".format(load_time))  # Format to 2 decimal places
            element = self.driver.find_element(locator_type, locator_value)
            print('is the element is found===', type(element))
            print('is the element is displayed?===', element.is_displayed)
            return element.is_displayed
        except TimeoutException:
            print("Element is not visible within {} seconds".format(duration))
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False

    def get_element_visibility(self, locator_type, locator_value):
        """
        Checks if an element is visible on the page within a 10-second timeout.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the element is visible; False otherwise.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False

    def is_element_displayed(self, locator_type, locator_value):
        """
        Checks if an element is displayed on the page.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the element is displayed; False otherwise.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((locator_type, locator_value)))
            #self.screenshotAttachment("element_displyed_{}.jpg".format(self.dynamic_number))
            return True
        except TimeoutException:
            print("TimeoutException")
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False

    def validate_text(self, locator_type, locator_value, expected_text):
        """
        Validates if the text of an element matches the expected text.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the actual text matches the expected text; False otherwise.
        """
        again = 1
        actual_text = None
        while again < 3:
            try:
                self.wait_for_element(locator_type, locator_value, 30)
                element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((locator_type, locator_value))
                )
                actual_text = element.text
                #self.screenshotAttachment("element_text_{}.jpg".format(self.dynamic_number))
                return actual_text == expected_text
            except NoSuchElementException:
                print("Inside no such element")
                return actual_text
            except StaleElementReferenceException:
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutError:
                again = 3
                print("Element not present")
                return False
            except TimeoutException:
                isVerify = False
                print("Inside timeout exception")
                return isVerify

    def validate_text_contains(self, by, value, expected_text):
        """
        Checks if the text of an element contains the expected text.
        Arguments:
        by - Locator strategy.
        value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the expected text is found within the element's text; False otherwise.
        """
        print("Inside validate text")
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((by, value))
        )
        actual_text = element.get_attribute("text")
        #self.screenshotAttachment("element_actual_text_{}.jpg".format(self.dynamic_number))
        if expected_text.lower() in actual_text.lower():
            return True
        else:
            return False

    def is_checkbox_checked(self, locator_type, locator_value):
        """
        Checks if a checkbox element is selected.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the checkbox is selected; False otherwise.
        """
        try:
            # Locate the checkbox element
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_type, locator_value)))
            #self.screenshotAttachment("checkbox_status_{}.jpg".format(self.dynamic_number))
            checkbosStatus = checkbox.is_selected()
            # Check if the checkbox is selected
            return checkbosStatus
        except (NoSuchElementException, TimeoutException):
            # If the element is not found or there's a timeout, return False
            return False
        
    def tap_on_coordinates(self, x, y):
        finger = PointerInput(kind="touch", name="finger")
        action = ActionBuilder(self.driver, mouse=finger)

        action.pointer_action.move_to_location(x, y)
        action.pointer_action.pointer_down()
        action.pointer_action.pointer_up()
        action.perform()

    def long_press_element(self, element, hold_duration_ms=1000):
        location = element.location
        size = element.size
        center_x = location['x'] + size['width'] // 2
        center_y = location['y'] + size['height'] // 2

        # Define a touch pointer input
        touch_input = PointerInput("touch", "finger")

        # Build actions with touch as the pointer
        actions = ActionBuilder(self.driver, pointer=touch_input)

        actions.pointer_action.move_to_location(x=center_x, y=center_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(hold_duration_ms / 1000)  # pause takes seconds
        actions.pointer_action.pointer_up()


    def swipe_up(self, duration=800):
        """Swipe up from bottom to top (scroll down)."""
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        start_x = width / 2
        start_y = height * 0.8
        end_x = width / 2
        end_y = height * 0.2

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        print(" Swiped up (scroll down)")

    def swipe_down(self, duration=800):
        """Swipe down from top to bottom (scroll up)."""
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        start_x = width / 2
        start_y = height * 0.2
        end_x = width / 2
        end_y = height * 0.8

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        print(" Swiped down (scroll up)")


    


        


    

    
