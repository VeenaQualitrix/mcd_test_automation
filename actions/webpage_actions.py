import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class WebAppActions:

    
    def __init__(self, driver):
        self.driver = driver
        
    
    
    def launch_browser_url(self, url):
        """
        Opens the specified URL in the provided WebDriver instance.
        Arguments:
        url - The URL to open in the web browser.
        """
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.execute_script("return document.readyState") == "complete"
        )

    def enter_text(self, locator_type, locator_value, text):
        """
        Waits for a brief period of time and then enters text into a specified input field.
        """
        element = self.driver.find_element(locator_type, locator_value)
        # print("typing values ===", text)    
        element.clear()
        element.send_keys(text)

    def validate_text(self, locator_type, locator_value, expected_text):
        """
        Validates if the text of an element matches the expected text.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the actual text matches the expected text; False otherwise.
        """
        WebAppActions(self.driver).wait_for_element(locator_type, locator_value, 30)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        actual_text = element.text
        return actual_text == expected_text

    def validate_text_contains(self, by, value, expected_text):
        """
        Checks if the text of an element contains the expected text.
        Arguments:
        by - Locator strategy.
        value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the expected text is found within the element's text; False otherwise.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        actual_text = element.get_attribute("text")
        return expected_text in actual_text

    def click_button(self, locator_type, locator_value):
        """
        Clicks a button identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        """    
        try:
            print("comign to click web element")
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((locator_type, locator_value)))
            element.click()
        except Exception:
            print("Element not found to perform click action")
    
    
    def wait_for_element(self, locator, value, timeout=30):
        """
        Waits for an element to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, value)))
        except NoSuchElementException:
            print("Inside no such element")
            return None
        except Exception:
            print("Element not found")
            return None
    
    def wait_for_elements(self, locator, value, timeout=60):
        """
        Waits for all elements to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((locator, value)))
        except NoSuchElementException:
            print("Inside no such element")
            return None
        except Exception:
            print("Element not found")
            return None
        '''
    def wait_for_element(self, locator, value, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator, value))
        )
        except TimeoutException:
            raise Exception(f"Timeout: Element with locator ({locator}, {value}) not found.")
        except NoSuchElementException:
            raise Exception(f"NoSuchElementException: Element ({locator}, {value}) not found.")
            '''

    def quit_Driver(self):
        self.driver.quit()  
         
    def get_text(self, locator_type, locator_value):
        """
        Retrieves the text of an element identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : string - The text content of the located element.
        """
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((locator_type, locator_value)))
        time.sleep(10)
        element = self.driver.find_element(locator_type, locator_value)
        print("fetching text from app ====", element.text)
        return element.text
    
    def is_element_displayed(self, locator_type, locator_value):
        """
        Checks if an element is displayed on the page.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the element is displayed; False otherwise.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((locator_type, locator_value)))
            element = self.driver.find_element(locator_type, locator_value)
            isElementStatus = element.is_displayed()
            return isElementStatus
        except TimeoutException:
            return False
        
    def is_date_selectable(self, day, month, year):
        """
        Check if the date button for given day/month/year is enabled (not disabled).
        Args:
            day (int or str): Day of the month (e.g., 26)
            month (int or str): Month number (1-12)
            year (int or str): Year (e.g., 2025)
        Returns:
            bool: True if date is selectable (enabled), False if disabled or not found.
        """
        day = str(int(day))
        month = str(int(month))
        year = str(year)

        try:
            date_button = self.driver.find_element(
                By.CSS_SELECTOR,
                f'button.calendar-day[data-day="{day}"][data-month="{month}"][data-year="{year}"]'
            )
            # Check if 'disabled' attribute is present
            is_disabled = date_button.get_attribute("disabled")
            return not bool(is_disabled)  # True if no disabled attribute, else False

        except NoSuchElementException:
            # The date button was not found in the calendar
            return False
