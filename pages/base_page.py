from actions.webpage_actions import WebAppActions
from conftest import readConstants
from appium import webdriver
from actions.android_actions import AndroidActions
from actions.ios_actions import iOSActions



class BasePage:

    def __init__(self, driver):
        if driver is None:
            raise ValueError("Driver cannot be None")
        self.driver = driver

        try:
            capabilities = driver.capabilities
            print("DEBUG: Capabilities =", capabilities)
            platform_name = capabilities.get('platformName', '').lower()
        except AttributeError:
            platform_name = ''
        
        if platform_name == 'android':
            print("Inside Android")
            self.actions = AndroidActions(driver)
        elif platform_name == 'ios':
            print("Inside iOS")
            self.actions = iOSActions(driver)
        else:
            print("Inside Web/Default")
            self.actions = WebAppActions(driver)

    def launch_application(self):
        """Launch the mobile application."""
        self.actions.launch_app()
        print("Opened McD App")


    def open_mcd_website(self):
        """Open the McD website in a browser."""
        url = readConstants("APP_URL")
        self.actions.launch_browser_url(url)
        self.driver.maximize_window()
        print("Opened McD Website")


    def quit_driver(self):
        self.actions.quit_Driver()
        print("Closed McD App")