from actions.webpage_actions import WebAppActions
from actions.android_actions import AndroidActions
from conftest import readConstants


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.actions = WebAppActions(driver)
        self.actions = AndroidActions(driver)
        

    def open_mcd_website(self):
        url = readConstants("APP_URL")
        self.actions.launch_browser_url(url)
        self.driver.maximize_window() 
        print("Opened McD Website")

    def launch_application(self):
        self.actions.launch_app()
        print("Opened McD App")
  

    def quit_driver(self):
        self.actions.quit_Driver()
        print("Closed McD App")

    

    