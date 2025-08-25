import random
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from actions.actions_parent import ActionsParent
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from conftest import readConstants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class iOSActions(ActionsParent):
    def __init__(self, driver):
        self.driver = driver
        self.ultra_wait = WebDriverWait(self.driver, readConstants("ULTRA_WAIT"))
        self.short_wait = WebDriverWait(self.driver, readConstants("SHORT_WAIT"))
        print("long wait ===", readConstants("LONG_WAIT"))
        self.wait = WebDriverWait(self.driver, readConstants("DEFAULT_WAIT"))
        self.long_wait = WebDriverWait(self.driver, readConstants("LONG_WAIT"))
        self.super_wait = WebDriverWait(self.driver, readConstants("SUPER_WAIT"))
        self.dynamic_number = random.randint(1, 10000)

    def launch_app(self, application):
        self.driver.activate_app(application)

    def relaunch_app(self, application):
        print("Relaunching Application")
        self.driver.activate_app(application)

    def wait_for_element(self, locator, value, timeout=60):
        """
        Waits for an element to be present on the page.
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
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None
            except StaleElementReferenceException:
                self.driver.refresh()
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
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None
            except StaleElementReferenceException:
                self.driver.refresh()
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutError:
                again = 3
                print("Element not present")
                return self.driver

    def enter_text(self, locator_type, locator_value, text):
        """
        Enters text into an input field identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        text - Text to enter into the input field.
        """
        print("locator_value  to enter_text ===", locator_value)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_type, locator_value)))
        self.screenshotAttachment("original_Text_present{}.jpg".format(self.dynamic_number))
        print("typeing values ===", text)
        element.clear()
        self.screenshotAttachment("original_Text_cleared{}.jpg".format(self.dynamic_number))
        element.send_keys(text)
        self.screenshotAttachment("original_Text{}.jpg".format(self.dynamic_number))
        # self.driver.hide_keyboard()

    def click_button(self, locator_type, locator_value):
        """
        Clicks a button identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        """
        print("passing locator_type", locator_type)
        element_present = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator_type, locator_value)))
        if element_present:
            element = self.driver.find_element(locator_type, locator_value)
            self.screenshotAttachment("clicking_here{}.jpg".format(self.dynamic_number))
            element.click()
            self.screenshotAttachment("button_clicked{}.jpg".format(self.dynamic_number))
        else:
            print("Element is not present to perform click action")

    def close_app(self, application):
        """
        Closes the application.
        """
        self.driver.terminate_app(application)

    def open_app(self, application):
        """
        Opens the application.
        """
        self.driver.activate_app(application)

    def suspend_app(self, seconds):
        """
        Suspends the app for a specified duration.
        Arguments:
        seconds - Duration to suspend the app, in seconds.
        """
        self.driver.background_app(seconds)

    def quit_Driver(self):
        self.driver.quit()

    def open_deep_link(self, deep_link):
        """
        Opens a deep link URL in the mobile app.
        Arguments:
        deep_link - The deep link URL to open.
        """
        self.driver.execute_script("mobile: deepLink", {"url": deep_link})

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
        print("before wait stattement===", locator_type)
        self.long_wait.until(EC.presence_of_element_located((locator_type, locator_value)))
        print("waiting for element to fetch text")
        time.sleep(10)
        element = self.driver.find_element(locator_type, locator_value)
        self.screenshotAttachment("get_text{}.jpg".format(self.dynamic_number))
        text_value = element.get_attribute('value')
        if not text_value:
            text_value = element.get_attribute('name')
        print("fetching text from app ====", text_value)
        return text_value

    def set_screen_orientation(self, orientation):
        """
        Sets the screen orientation of the device.
        Arguments:
        orientation - Desired screen orientation ('LANDSCAPE' or 'PORTRAIT').
        """
        self.driver.orientation = orientation

    def set_text(self, locator_type, locator_value, text):
        """
        Clears and sets text in an input field identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        text - Text to enter into the input field.
        """
        self.screenshotAttachment("set_text_before{}.jpg".format(self.dynamic_number))
        element = self.driver.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)
        self.screenshotAttachment("set_text_after{}.jpg".format(self.dynamic_number))
        self.driver.hide_keyboard()

    def swipe(self, direction="up", duration=800):
        """
        Performs a swipe gesture from one coordinate to another.
        Arguments:
        direction - Swipe directions.
        duration - Duration of the swipe in milliseconds (default is 800).
        """
        self.screenshotAttachment("before_swipe{}.jpg".format(self.dynamic_number))
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] / 2
        if direction == "left":
            end_x = 0
            end_y = start_y
        elif direction == "right":
            end_x = screen_size['width']
            end_y = start_y
        elif direction == "up":
            end_x = start_x
            end_y = 0
        elif direction == "down":
            end_x = start_x
            end_y = screen_size['height']
        elif direction == "up_right":
            start_x = end_x = screen_size['width']
            end_y = 0
        elif direction == "up_left":
            start_x = end_x = 0
            end_y = 0
        else:
            # default direction as up
            end_x = start_x
            end_y = 0
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        self.screenshotAttachment("after_swipe{}.jpg".format(self.dynamic_number))

    def validate_element_visitbilty_within_time(self, locator_type, locator_value, duration):
        """
        Checks if an element is visible within the specified time frame.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        duration - Maximum time to wait for visibility, in seconds.
        Returns : True if the element is visible within the duration; False otherwise.
        """
        self.screenshotAttachment("element_visibilty{}.jpg".format(self.dynamic_number))
        start_time = time.time()  # Record the start time
        print("checking element loading with in given time frame", duration, locator_type, locator_value)
        print("my driver is ==", type(self.driver))
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
            self.screenshotAttachment("waiting_element{}.jpg".format(self.dynamic_number))
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
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            self.screenshotAttachment("element_visibilty{}.jpg".format(self.dynamic_number))
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
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((locator_type, locator_value)))
            self.driver.find_element(locator_type, locator_value)
            self.screenshotAttachment("element_found{}.jpg".format(self.dynamic_number))
            return True
        except TimeoutException:
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
                print(" message expected========", expected_text)
                self.wait_for_element(locator_type, locator_value, 40)
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((locator_type, locator_value))
                )
                print("text  element========", element.is_displayed())
                self.screenshotAttachment("validate_text{}.jpg".format(self.dynamic_number))
                actual_text = element.get_attribute('value')
                print(" message i have read ========", actual_text)
                return actual_text == expected_text
            except NoSuchElementException:
                print("Inside no such element")
                self.screenshotAttachment("error_validate_text{}.jpg".format(self.dynamic_number))
                return actual_text
            except StaleElementReferenceException:
                self.driver.refresh()
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
        again = 1
        actual_text = None
        while again < 3:
            try:
                self.screenshotAttachment("cotain_text{}.jpg".format(self.dynamic_number))
                print(" message expected========", expected_text)
                self.wait_for_element(by, value, 40)
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((by, value))
                )
                self.screenshotAttachment("element_text_validations_{}.jpg".format(self.dynamic_number))
                print("text  element========", element.is_displayed())
                actual_text = element.get_attribute('value')
                self.screenshotAttachment("actual_text{}.jpg".format(self.dynamic_number))
                print(" message i have read ========", actual_text)
                return expected_text in actual_text
            except NoSuchElementException:
                self.screenshotAttachment("text_not_found{}.jpg".format(self.dynamic_number))
                print("Inside no such element")
                return actual_text
            except StaleElementReferenceException:
                self.driver.refresh()
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
            self.screenshotAttachment("check_box{}.jpg".format(self.dynamic_number))
            checkbox = self.driver.find_element(locator_type, locator_value)
            # Check if the checkbox is selected
            self.screenshotAttachment("check_box_status{}.jpg".format(self.dynamic_number))
            return checkbox.is_selected()
        except (NoSuchElementException, TimeoutException):
            # If the element is not found or there's a timeout, return False
            return False

    def screenshotAttachment(self, ScreenshotName):
        doIneedScreenshot = readConstants("NEED_SCREENSHOTS_FOR_PASS")
        print("want to take scrrenshot after sending values ", doIneedScreenshot)
        if str(doIneedScreenshot).lower() == 'true':
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenshotName, attachment_type=AttachmentType.PNG)

    def fluentWaitNew(self, locator, timeout=10, poll_frequency=0.5):
        """
        Waits for an element to be present using a fluent wait approach.
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))
    
    def tap_on_coordinates(self, x, y):
        finger = PointerInput(kind="touch", name="finger")
        action = ActionBuilder(self.driver, mouse=finger)

        action.pointer_action.move_to_location(x, y)
        action.pointer_action.pointer_down()
        action.pointer_action.pointer_up()
        action.perform()

    def hide_keyboard_by_tapping_outside(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        self.tap_on_coordinates(x=width // 2, y=height - 100)

    def clear_text(self, by, locator):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((by, locator)))
        element = self.driver.find_element(by, locator)
        element.clear() 

    def send_keys(self, locator_strategy, locator, text):
        element = self.driver.find_element(locator_strategy, locator)
        element.clear()  # Optional: clear the field before typing
        element.send_keys(text)


    def scroll_down(self):
        window_size = self.driver.get_window_size()
        start_x = window_size["width"] / 2
        start_y = window_size["height"] * 0.8
        end_y = window_size["height"] * 0.2

        self.driver.swipe(start_x, start_y, start_x, end_y, duration=800)

        

    def scroll_to_element_by_name(self, name: str):
        self.driver.execute_script("mobile: scroll", {
            "direction": "down",
            "predicateString": f"name == '{name}'"
        })
        time.sleep(2)

    
