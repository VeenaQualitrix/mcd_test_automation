from actions.webpage_actions import WebAppActions
from conftest import readConstants
from selenium import webdriver
from appium import webdriver as appiumdriver
from actions.android_actions import AndroidActions
from actions.ios_actions import iOSActions



class BasePage:

    def __init__(self, driver):
        self.driver = driver 
        if isinstance(driver, webdriver.Remote):
            self.driver = driver
            print("Web browser instance")
            self.actions = WebAppActions(driver)
        elif isinstance(driver, appiumdriver.Remote):
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            if platform_name == 'android':
                print("Inside Android")
                self.actions = AndroidActions(driver)
            elif platform_name == 'ios':
                print("Inside iOS")
                self.actions = iOSActions(driver)
        else:
            print("Both chrome and webdriver instance is not called")


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

    # def launch_application(self, appURL):
    #     if appURL:
    #         self.actions.launch_browser_url(appURL)
    #         print("Opened McD Website")
    #     else:
    #         self.actions.launch_app()
    #         print("Opened McD App")  
            