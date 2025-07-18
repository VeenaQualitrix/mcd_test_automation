from actions.webpage_actions import WebAppActions
from conftest import readConstants


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = WebAppActions(driver)

    def open_mcd_website(self):
        url = readConstants("APP_URL")
        self.actions.launch_browser_url(url)
        self.driver.maximize_window() 
        print("Opened McD Website")

    def launch_application(self, appURL):
        self.actions.launch_browser_url(appURL)
        print("Opened McD Website")