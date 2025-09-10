from conftest import setup_platform
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.view_cart_page import ViewCartPage
import os
import time
import subprocess

locators = {
        "ORDER_CONFIRMATION": (By.XPATH, "//h3[contains(text(), 'Delivering happiness at your doorstep')]"),
        "ORDER_HISTORY_PAGE": (By.XPATH, "//h1[contains(text(), ' Order History ')]"),
        "TRACK_ORDER": (By.XPATH, "//div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'CASH')]]/following::div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'Order Status')] and h2[contains(text(), 'In Kitchen')]] /following::button[contains(text(), 'Track')][1]"),
        "PAY_ONLINE_BUTTON": (By.XPATH, "//button[contains(text(), 'Pay Online')]"),
        "ORDER_IN_KITCHEN": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Payment Mode'] and h2[normalize-space(text())='NET_BANKING']] /following::div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Order Status'] and h2[normalize-space(text())='In Kitchen']][1])[1]"),
        "ORDER_CANCELLED": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Payment Mode'] and h2[normalize-space(text())='CASH']] /following::div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Order Status'] and h2[normalize-space(text())='Cancelled']])[1]"),
        "ORDER_ACCEPTED": (By.XPATH, "//h2[contains(text(), ' Accepted ')]"),
        "ORDER_PLACED": (By.XPATH, "//h2[contains(text(), ' Placed ')]"),
        "ORDER_COMPLETED": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Payment Mode'] and h2[normalize-space(text())='NET_BANKING']] /following::div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Order Status'] and h2[normalize-space(text())='Completed']])[1]"),
        "ORDER_DELIVERED": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Payment Mode'] and h2[normalize-space(text())='NET_BANKING']] /following::div[contains(@class, 'bottomGrid__paymentTexts') and h2[normalize-space(text())='Order Status'] and h2[normalize-space(text())='Delivered']])[1]"),
        "COMPLETED_TRACK_ORDER": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'NET_BANKING')]]/following::div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'Order Status')] and h2[contains(text(), 'Completed')]] /following::button[contains(text(), 'Track')])[1]"),
        "ORDER_SERVED_TEXT": (By.XPATH, "//span[contains(text(), ' Order Served! ')]"),
        "CANCELLED_TRACK_ORDER": (By.XPATH, "//div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'CASH')]]/following::div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'Order Status')] and h2[contains(text(), 'Cancelled')]] /following::button[contains(text(), 'Track')][1]"),
        "ORDER_CANCELLED_TEXT": (By.XPATH, "//span[contains(text(), ' Order cancelled ')]"),
        "BACK_FROM_POST_PAYMENT": (By.XPATH, "//img[@alt = 'ic-arrow-back-black']"),
        "MCDELIVERY_BM": (By.XPATH, "(//div[contains(text(), ' McDelivery ')])[1]"),
        "DINE_IN_BM": (By.XPATH, "(//div[contains(text(), ' Dine in ')])[1]"),
        "ON_THE_GO_BM": (By.XPATH, "(//div[contains(text(), ' On The Go ')])[1]"),
        "TAKEOUT_BM": (By.XPATH, "(//div[contains(text(), ' Takeout ')])[1]"),
        "HELP_BUTTON": (By.XPATH, "(//button[contains(text(), 'Help')])[1]"),
        "MCDELIVERY_HELP_BUTTON": (By.XPATH, "(//div[contains(@class, 'paymentHistoryCard')][.//div[contains(@class, 'paymentHistoryCard__popular-tag') and contains(text(), 'McDelivery')]]  //button[contains(@class, 'app-btn') and contains(text(), 'Help')])[1]"),
        "TIME_EXCEED_POP_UP_MSG": (By.XPATH, "//h2[contains(text(), 'Order Active Hours Ended')]"),
        "POP_UP_OK_BUTTON": (By.XPATH, "//span[contains(text(), 'OK')]"),
        "CANCELLED_HELP_BUTTON": (By.XPATH, "(//div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'CASH')]]/following::div[contains(@class, 'bottomGrid__paymentTexts')][h2[contains(text(), 'Order Status')] and h2[contains(text(), 'Cancelled')]] /following::button[contains(@class, 'app-btn') and contains(text(), 'Help')])[1]"),
        "GET_HELP_TEXT": (By.XPATH, "//div[contains(text(), 'Get Help')]"),
        "FEEDBACK_FIRST_TEXT_FIELD": (By.XPATH, "//ion-select[@aria-label = 'What is your concern?']"),
        "OTHER_OPTION": (By.XPATH, "//ion-select-option[contains(text(), 'Other')]"),
        "PROMO_NOT_APPLIED_OPTION": (By.XPATH, "//ion-select-option[contains(text(), 'Promo Not Applied')]"),
        "FEEDBACK_SECOND_TEXT_FIELD": (By.XPATH, "//textarea[@placeholder = 'Share some details']"),
        "SUBMIT_BUTTON": (By.XPATH, "//button[contains(text(), ' Submit ')]"),
        "COMPLAINT_RAISED_POP_UP": (By.XPATH, "//h2[contains(text(), 'Complaint Raised:')]"),
        "ORDER_DETAILS": (By.XPATH, "//span[contains(text(), ' Your order Details ')]"),
        "MENU_DETAILS": (By.XPATH, "//div[@class = 'menu__title-container']"),
        "INVOICE": (By.XPATH, "//span[contains(text(), ' Invoice ')]"),
        "ORDER_ID_TEXT": (By.XPATH, " (//h2[contains(text(), 'Order ID:')])[1]"),
        "ORDER_ID": (By.XPATH, "//span[contains(text(), 'DAD-TA-22-07-2025-79884447 ')]"),
        "STORE_NAME": (By.XPATH, "(//h2[contains(text(), ' Dadar Star Mall ')])[1]"),
        "HOME_TEXT_ON_DELIVERY_ADDRESS": (By.XPATH, "//strong[contains(text(), ' Home ')]"),
        "DELIVERY_ADDRESS": (By.XPATH, "//p[contains(text(), ' Shree Prasanna Cooperative Housing Society')]"),
        "PLACED_STATUS_BAR": (By.XPATH, " //span[contains(text(), 'Placed')]"),
        "ACCEPTED_STATUS_BAR": (By.XPATH, "//span[contains(text(), ' Accepted ')]"),
        "IN_KITCHEN_STATUS_BAR": (By.XPATH, "//span[contains(text(), ' In Kitchen ')]"),
        "OUT_FOR_DELIVERY_STATUS_BAR": (By.XPATH, "//span[contains(text(), ' Out for delivery ')]"),
        "MCDELIVERED_STATUS_BAR": (By.XPATH, "//span[contains(text(), ' McDelivered ')]"),

    
    }


class OrderTrackingPage(BasePage):

    def verify_order_condirmation_is_displayed(self):
        time.sleep(15)
        self.actions.is_element_displayed(*locators['ORDER_CONFIRMATION'])
        print("Order confirmation message is displayed")

    def verify_order_history_page_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_HISTORY_PAGE'])
        print("Order History page is displayed")

    def click_on_track_order(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['TRACK_ORDER'])
        print("Track order button is displayed")
        self.actions.click_button(*locators['TRACK_ORDER'])
        print("Clicked Track Order button")

    def verify_user_navigated_to_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['PAY_ONLINE_BUTTON'])
        print("Pay online button is displayed")

    def verify_display_of_order_status_on_each_card(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_IN_KITCHEN'])
        print("Order status 'In-Kitchen'is displayed")
        time.sleep(3)
        Cancelled_order = self.driver.find_element(*locators["ORDER_CANCELLED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Cancelled_order)
        self.actions.is_element_displayed(*locators['ORDER_CANCELLED'])
        print("Order status 'Cancelled 'is displayed")
        time.sleep(5)
        Accepted_order = self.driver.find_element(*locators["ORDER_ACCEPTED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Accepted_order)
        self.actions.is_element_displayed(*locators['ORDER_ACCEPTED'])
        print("Order status 'Accepted 'is displayed")
        time.sleep(5)
        Completed_order = self.driver.find_element(*locators["ORDER_COMPLETED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Completed_order)
        self.actions.is_element_displayed(*locators['ORDER_COMPLETED'])
        print("Order status 'Completed'is displayed")
        time.sleep(5)
        Delivered_order = self.driver.find_element(*locators["ORDER_DELIVERED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Delivered_order)
        self.actions.is_element_displayed(*locators['ORDER_DELIVERED'])
        print("Order status 'Delivered'is displayed")
        time.sleep(5)
        Placed_order = self.driver.find_element(*locators["ORDER_PLACED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Placed_order)
        self.actions.is_element_displayed(*locators['ORDER_PLACED'])
        print("Order status 'Placed'is displayed")

    def click_on_completed_order_tracking(self):
        time.sleep(3)
        Completed_order = self.driver.find_element(*locators["ORDER_COMPLETED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Completed_order)
        self.actions.is_element_displayed(*locators['ORDER_COMPLETED'])
        print("Order status 'Completed'is displayed")
        self.actions.click_button(*locators['COMPLETED_TRACK_ORDER'])
        print("Clicked completed status track Order button")
        time.sleep(2)
        self.actions.click_button(*locators['BACK_FROM_POST_PAYMENT'])
        print("Clicked back button from post payment page")

    def click_on_cancelled_order_tracking(self):
        time.sleep(5)
        Cancelled_order = self.driver.find_element(*locators["ORDER_CANCELLED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Cancelled_order)
        self.actions.is_element_displayed(*locators['ORDER_CANCELLED'])
        print("Order status 'Completed'is displayed")
        self.actions.click_button(*locators['CANCELLED_TRACK_ORDER'])
        print("Clicked cancelled status track Order button")

    def verify_completed_order_status_on_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_SERVED_TEXT'])
        print("Order served text is displayed for completed order")

    def verify_cancelled_order_status_on_post_payment_page(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_CANCELLED_TEXT'])
        print("Order cancelled text is displayed for cancelled order")

    def verify_each_order_card_display_BM_name(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['MCDELIVERY_BM'])
        print("Mcdelivery is displayed on order card")
        self.actions.is_element_displayed(*locators['DINE_IN_BM'])
        print("Dine-In is displayed on order card")
        On_the_go_BM_name = self.driver.find_element(*locators["ON_THE_GO_BM"])
        self.driver.execute_script("arguments[0].scrollIntoView();", On_the_go_BM_name)
        self.actions.is_element_displayed(*locators['ON_THE_GO_BM'])
        print("On the go is displayed on order card")
        time.sleep(2)
        takeout_BM_name = self.driver.find_element(*locators["TAKEOUT_BM"])
        self.driver.execute_script("arguments[0].scrollIntoView();", takeout_BM_name)
        self.actions.is_element_displayed(*locators['TAKEOUT_BM'])
        print("Takeout is displayed on order card")

    def scroll_down_the_page_on_order_history_page(self):
        time.sleep(3)
        Scroll_down = self.driver.find_element(*locators["ORDER_PLACED"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Scroll_down)
        self.actions.is_element_displayed(*locators['ORDER_PLACED'])
        print("The page scrolled down")

    def verify_display_of_addition_order_history(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_PLACED'])
        print("The page scrolled down, and the 'Placed' order status is displayed.")

    def scroll_up_the_page_on_order_history_page(self):
        time.sleep(3)
        Scroll_up = self.driver.find_element(*locators["ORDER_IN_KITCHEN"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Scroll_up)
        self.actions.is_element_displayed(*locators['ORDER_IN_KITCHEN'])
        print("The page scrolled up")

    def verify_display_of_previous_order_history(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_IN_KITCHEN'])
        print("The page scrolled up, and the 'In-kitchen' order status is displayed.")

    def verify_help_button_visible_only_for_order_placed_via_Mcdelivery(self):
        time.sleep(3)
        assert self.actions.is_element_displayed(*locators["MCDELIVERY_BM"]), "McDelivery BM not found"
        assert self.actions.is_element_displayed(*locators["MCDELIVERY_HELP_BUTTON"]), \
            "'Help' button is NOT visible for McDelivery, but it should be."
        print(" 'Help' button is visible for McDelivery BM")

    def verify_help_button_not_visible_for_other_BMs(self):
        #  Dine-In
        dine_in_bm = self.driver.find_element(*locators["DINE_IN_BM"])
        self.driver.execute_script("arguments[0].scrollIntoView();", dine_in_bm)
        assert self.actions.is_element_displayed(*locators["DINE_IN_BM"]), "Dine-In BM not found"
        
        help_for_dine_in = self.driver.find_elements(By.XPATH,
            "//div[contains(@class, 'paymentHistoryCard')][.//div[contains(@class, 'paymentHistoryCard__popular-tag') and contains(text(), 'Dine in')]]"
            "//button[contains(@class, 'app-btn') and contains(text(), 'Help')]"
        )
        assert len(help_for_dine_in) == 0, "'Help' button SHOULD NOT be visible for Dine-In BM"
        print(" 'Help' button is not visible for Dine-In BM")

        #  On The Go
        on_the_go_bm = self.driver.find_element(*locators["ON_THE_GO_BM"])
        self.driver.execute_script("arguments[0].scrollIntoView();", on_the_go_bm)
        assert self.actions.is_element_displayed(*locators["ON_THE_GO_BM"]), "On The Go BM not found"

        help_for_on_the_go = self.driver.find_elements(By.XPATH,
            "//div[contains(@class, 'paymentHistoryCard')][.//div[contains(@class, 'paymentHistoryCard__popular-tag') and contains(text(), 'On The Go')]]"
            "//button[contains(@class, 'app-btn') and contains(text(), 'Help')]"
        )
        assert len(help_for_on_the_go) == 0, "'Help' button SHOULD NOT be visible for On The Go BM"
        print(" 'Help' button is not visible for On The Go BM")

        #  Takeout
        takeout_bm = self.driver.find_element(*locators["TAKEOUT_BM"])
        self.driver.execute_script("arguments[0].scrollIntoView();", takeout_bm)
        assert self.actions.is_element_displayed(*locators["TAKEOUT_BM"]), "Takeout BM not found"

        help_for_takeout = self.driver.find_elements(By.XPATH,
            "//div[contains(@class, 'paymentHistoryCard')][.//div[contains(@class, 'paymentHistoryCard__popular-tag') and contains(text(), 'Takeout')]]"
            "//button[contains(@class, 'app-btn') and contains(text(), 'Help')]"
        )
        assert len(help_for_takeout) == 0, "'Help' button SHOULD NOT be visible for Takeout BM"
        print(" 'Help' button is not visible for Takeout BM")

    def select_an_older_order_and_click_on_Help_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CANCELLED_HELP_BUTTON'])
        print("The help button is displayed")
        self.actions.click_button(*locators['CANCELLED_HELP_BUTTON'])
        print("Clicked on Help button")

    def verify_time_exceeded_pop_up_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['TIME_EXCEED_POP_UP_MSG'])
        print("The time exceeded pop up msg is displayed")
        self.actions.click_button(*locators['POP_UP_OK_BUTTON'])
        print("Clicked on Ok button")

    def click_on_back_button_on_post_payment_page(self):
        time.sleep(3)
        self.actions.click_button(*locators['BACK_FROM_POST_PAYMENT'])
        print("Clicked back button on post payment page")

    def select_latest_order_and_click_on_Help_button(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['MCDELIVERY_HELP_BUTTON'])
        print("The help button is displayed")
        self.actions.click_button(*locators['MCDELIVERY_HELP_BUTTON'])
        print("Clicked on Help button")

    def verify_user_able_to_give_a_feedback(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['GET_HELP_TEXT'])
        print("The Get help text is displayed")
        self.actions.is_element_displayed(*locators['FEEDBACK_FIRST_TEXT_FIELD'])
        print("'What is your concern' text is displayed")
        self.actions.click_button(*locators['FEEDBACK_FIRST_TEXT_FIELD'])
        print("Clicked on textfield")
        self.actions.is_element_displayed(*locators['OTHER_OPTION'])
        print("'Other' radio button is displayed")
        self.actions.is_element_displayed(*locators['PROMO_NOT_APPLIED_OPTION'])
        print("'Promo not applied' radio button is displayed")
        self.actions.click_button(*locators['PROMO_NOT_APPLIED_OPTION'])
        print("Clicked on 'Promo not applied' radio button")
        self.actions.click_button(*locators['POP_UP_OK_BUTTON'])
        print("Clicked on Ok button")
        time.sleep(2)
        self.actions.is_element_displayed(*locators['FEEDBACK_SECOND_TEXT_FIELD'])
        print("'Share some details' text is displayed")
        self.actions.enter_text(*locators['FEEDBACK_SECOND_TEXT_FIELD'], "Feedback added")
        print("Entered feedback in text field")
        self.actions.click_button(*locators['SUBMIT_BUTTON'])
        print("Clicked on submit button")

    def verify_complaint_raised_pop_up(self):
        time.sleep(5)
        self.actions.click_button(*locators['MCDELIVERY_HELP_BUTTON'])
        print("Clicked on Help button")
        time.sleep(32)
        self.actions.is_element_displayed(*locators['COMPLAINT_RAISED_POP_UP'])
        print("Complaint raised pop up is displayed")

    def verify_your_order_details_section_is_displayed(self):
        time.sleep(3)
        Your_order_details = self.driver.find_element(*locators["ORDER_DETAILS"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Your_order_details)
        self.actions.is_element_displayed(*locators['ORDER_DETAILS'])
        print("Your Order details text is displayed")

    def verify_menu_details_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['MENU_DETAILS'])
        print("Menu details text is displayed")

    def click_on_invoice_to_download(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['INVOICE'])
        print("Invoice is displayed")
        time.sleep(2)
        self.actions.click_button(*locators['INVOICE'])
        print("Clicked on Invoice to download it")

    def step_verify_invoice_downloaded(context):
        # Define expected filename (adjust to your app behavior)
        expected_filename = "invoice.pdf"  
        time.sleep(5)
        # Use ADB to pull the Downloads directory content list
        result = subprocess.run(["adb", "shell", "ls", "/sdcard/Download"], capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception("Failed to access device downloads folder")

        downloaded_files = result.stdout.splitlines()

        # Debug print
        print("Downloaded files:", downloaded_files)

        # Check if invoice is present
        assert expected_filename in downloaded_files, f"Invoice file '{expected_filename}' not found in Downloads"

    def verify_order_number_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['ORDER_ID_TEXT'])
        print("Order number is displayed")

    def verify_store_name_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['STORE_NAME'])
        print("Store name is displayed")

    def verify_complete_address_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['HOME_TEXT_ON_DELIVERY_ADDRESS'])
        print("Home text on delivery address is displayed")
        self.actions.is_element_displayed(*locators['DELIVERY_ADDRESS'])
        print("Complete delivery address is displayed")

    def verify_status_bar_is_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['PLACED_STATUS_BAR'])
        print("Placed status bar is displayed")
        self.actions.is_element_displayed(*locators['ACCEPTED_STATUS_BAR'])
        print("Accepted status bar is displayed")
        self.actions.is_element_displayed(*locators['IN_KITCHEN_STATUS_BAR'])
        print("In-Kitchen status bar is displayed")
        self.actions.is_element_displayed(*locators['OUT_FOR_DELIVERY_STATUS_BAR'])
        print("Out for delivery status bar is displayed")
        self.actions.is_element_displayed(*locators['MCDELIVERED_STATUS_BAR'])
        print("Mcdelivered status bar is displayed")


