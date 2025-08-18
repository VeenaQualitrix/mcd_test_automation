from actions.webpage_actions import WebAppActions
from conftest import readConstants
from appium import webdriver
from actions.android_actions import AndroidActions
from actions.ios_actions import iOSActions



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        if isinstance(driver, webdriver.Remote):
            print("Application Launched")
            self.driver = driver
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            if platform_name == 'android':
                print("Inside Android")
                self.actions = AndroidActions(driver)
            elif platform_name == 'ios':
                print("Inside iOS")
                self.actions = iOSActions(driver)
            else:
                print("for WebBrowser")
                self.actions = WebAppActions(driver)


    '''
    def launch_application(self, appURL):
        if appURL:
            self.actions.launch_browser_url(appURL)
            print("Opened McD Website")
        else:
            self.actions.launch_app()
            print("Opened McD App")  
            '''

    def launch_application(self):
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