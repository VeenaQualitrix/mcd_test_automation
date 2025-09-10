from appium import webdriver as appium_webdriver
from selenium.webdriver.remote.webdriver import WebDriver as selenium_webdriver
from conftest import readConstants
from actions.webpage_actions import WebAppActions
from actions.android_actions import AndroidActions
from actions.ios_actions import iOSActions


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = None

        # Case 1: Appium Remote driver
        if isinstance(driver, appium_webdriver.Remote):
            print("Application Launched via Appium")
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()

            if platform_name == 'android':
                print("Inside Android")
                self.actions = AndroidActions(driver)
            elif platform_name == 'ios':
                print("Inside iOS")
                self.actions = iOSActions(driver)

        # Case 2: Selenium WebDriver (Chrome/Firefox/Edge etc.)
        elif isinstance(driver, selenium_webdriver):
            print("Launching for WebBrowser")
            self.actions = WebAppActions(driver)

        # Case 3: Unknown driver
        if not self.actions:
            raise Exception(f" Unsupported driver type: {type(driver)}. Actions not initialized.")


    def launch_application(self, appURL =None):
        if appURL:
            self.actions.launch_browser_url(appURL)
            print("Opened McD Website")
        else:
            self.actions.launch_app()
            print("Opened McD App")   

    def open_mcd_website(self):
        url = readConstants("APP_URL")
        self.actions.launch_browser_url(url)
        self.driver.maximize_window() 
        print("Opened McD Website")

    def quit_driver(self):
        self.actions.quit_Driver()
        print("Closed McD App")