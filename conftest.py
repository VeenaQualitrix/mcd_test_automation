
import http
from http.client import RemoteDisconnected
import platform
import socket
import subprocess
# import time
import allure
from bs4 import BeautifulSoup
import psutil
import pytest
from appium import webdriver as appiumDriver
from selenium import webdriver
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType
from selenium import webdriver
from requests.auth import HTTPDigestAuth
import re
import urllib3
import wget
import logging
# from src.app.application import Application
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium import webdriver as browserDriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
from pathlib import Path
import time
import zipfile
import signal

import json
import stat

import requests
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504, 401],
)


def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="fire_tv", help="platform to run test (Fire_TV, Roku_TV, Apple_TV,IPad)"
    )
    parser.addoption("--consecutive_failure_abort", default="True", action="store")
    parser.addoption("--consecutive_failure_count", default="5", action="store")
    parser.addoption("--qaserver", default="qa8", action="store")
    parser.addoption("--appFileName", action="store")
    parser.addoption("--app_package_name", action="store")
    parser.addoption("--roku_ip", action="store")
    parser.addoption("--rokuUser", action="store")
    parser.addoption("--rokuPass", action="store")
    parser.addoption("--screenShotToggle", default=True, action="store")
    parser.addoption("--roku_webdriver_host", default="localhost", action="store")
    parser.addoption("--webDriverAgentUrl", action="store")
    
   

@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
        Fixture for setting up the testing environment.
    """
    return request.config.getoption("--platform")




def launchChromeheadless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (recommended for headless mode)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in Docker containers
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-insecure-localhost")
    #chrome_options.add_argument("--headless=old")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    browserDriver = webdriver.Chrome(service=service, options=chrome_options)
    return browserDriver



@pytest.fixture(scope="class", autouse=False)
def get_admin_server(request):
    server_value = request.config.getoption("--qaserver")
    admin_server_url = readConstants("admin_app_url")
    print('admin_server_url===', admin_server_url.format(server_value))
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browserDriver = launchChromeBrowser()
    browserDriver = launchChromeheadless()
    print("launch portal")
    browserDriver.get(admin_server_url.format(server_value))
    browserDriver.save_screenshot("headless_mode_test.png")
    yield browserDriver
    # browserDriver.close


def load_capabilities(config_name):
    print('config_name want to fetch ', config_name)
    project_root = os.getcwd()
    # os.path.dirname(os.path.dirname(__file__))
    print('project_root', project_root)
    config_path = os.path.join(project_root, 'util', 'platformconfig.json')
    print('config_path', config_path)
    with open(config_path, 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        # print('reading full config file ', config)
    return config.get(config_name, {})


def readConstants(constant_key):
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'util', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)
        # print('reading full config file ', config)
    return costant_value.get(constant_key)


def readPreReqJson(prereqFileName, constant_key):
    project_root = os.getcwd()
    data_file_path = os.path.join(project_root, 'util', prereqFileName + ".json")
    with open(data_file_path, 'r', encoding='utf-8') as constant_file:
        costant_value = json.load(constant_file)
    return costant_value.get(constant_key)


def start_appium_service_with_retry(port=4723, retries=3, delay=5):
    appium_service = AppiumService()
    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1} to start Appium service on port {port}...")
            appium_service.start(args=[f"--port={port}", "--log-level=debug"])
            if appium_service.is_running:
                print(f"Appium service started successfully on port {port}!")
                return appium_service
        except Exception as e:
            print(f"Error starting Appium service: {e}")
            time.sleep(delay)

    # If all retries fail, kill the process on the port and try one last time
    print(f"All {retries} retries failed. Checking and killing the process on port {port}.")
    kill_process_on_port(port)
    time.sleep(delay)  # Wait briefly before retrying
    try:
        appium_service.start(args=[f"--port={port}", "--log-level=debug"])
        if appium_service.is_running:
            print(f"Appium service started successfully on port {port} after killing the PID!")
            return appium_service
    except Exception as e:
        print(f"Failed to start Appium service even after killing the process: {e}")
        raise Exception("Unable to start Appium service.")


def kill_process_on_port(port):
    try:
        # Use lsof to find the PID and kill it
        result = os.popen(f"lsof -ti:{port}").read().strip()
        if result:
            print(f"Killing process with PID: {result} on port {port}.")
            os.system(f"kill -9 {result}")
        else:
            print(f"No process found running on port {port}.")
    except Exception as e:
        print(f"Error killing process on port {port}: {e}")

@pytest.fixture(scope="class", autouse=False)
def setup_platform(env, request):
    driver = None
    """
        Fixture for setting up the testing environment.
    """
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'util', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)
       
    with open(constants_path, "w") as constant_file:
        json.dump(costant_value, constant_file, indent=4)              
    currentPlatform = env
    appToLaunch = request.config.getoption("--appFileName")
   
    print('currentApp', currentPlatform)
    if currentPlatform == 'android':
        print("Inside android")
        appium_service = AppiumService()
        appium_service.start(args=['--allow-insecure=adb_shell', '--allow-cors'])
        if not appium_service.is_running:
            raise Exception("Appium server did not start!")

        capabilities = load_capabilities(currentPlatform)
        appPath = os.path.abspath(os.getcwd())
       
        capabilities["appium:app"] = os.path.join(appPath, 'builds', appToLaunch)
        print('capabilities to load', capabilities)
        
        options = UiAutomator2Options().load_capabilities(capabilities)
        print("loadingoptions ====", options)

        # capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        try:
            print("am i relunching app?=============================")
            driver = appiumDriver.Remote("http://127.0.0.1:4723", options=options)
            print(" firetv driver started=====")
            print(" firetv driver started=  driver type ====", type(driver))
            driver.terminate_app(readConstants("current_app_package"))
            time.sleep(2)
            driver.close
            # Launch (activate) the app again
            driver.activate_app(readConstants("current_app_package"))
            
            driver.implicitly_wait(10)
        except Exception as e:
            print("firetv appluanch error ===", e)
    
        except Exception as e:
            print("firetv appluanch error ===", e)

    if currentPlatform == 'web':
        driver = launchChromeheadless()
        print("launch chrome browser ", type(driver))

    if currentPlatform == 'ios':
        print("launch apple tv")
        appium_service = start_appium_service_with_retry()
        appium_service.start()
        webDriverAgentUrl = request.config.getoption("--webDriverAgentUrl")
        if not appium_service.is_running:
            raise Exception("Appium server did not start!")
        appToLaunch = request.config.getoption("--appFileName")
        bundleId = request.config.getoption("app_package_name")
        capabilities = load_capabilities(currentPlatform)
        appPath = os.path.abspath(os.getcwd())
        capabilities["webDriverAgentUrl"] = webDriverAgentUrl
        print('capabilities to load for iOS', capabilities)

        print(os.path.abspath(os.getcwd()))

        options = XCUITestOptions().load_capabilities(capabilities)
        print("loadingoptions ====", options)
        try:
            print("am i relunching app?=============================")
            for attempt in range(3):
                try:
                    driver = appiumDriver.Remote("http://127.0.0.1:4723", options=options)
                    if driver is not None:
                        break
                except Exception as e:
                    print(f"Attempt {attempt + 1} to create driver failed: {e}")
                    time.sleep(5)
            print("iOS driver started=====")
            print("iOS driver started=  driver type ====", type(driver))
            driver.implicitly_wait(30)
            bundleId= 'com.il.mcd'
            try:
                driver.execute_script('mobile: terminateApp', {'bundleId': bundleId})

            except Exception as e:
                print(f"Failed to terminate app {bundleId}: {e}")
            driver.execute_script('mobile: activateApp', {'bundleId': bundleId})
        except Exception as e:
            print("iOS appluanch error ===", e)
        
    if driver:
        print('yeidling driver instance condition')
        yield driver
        print('after yielding driver')
        if isinstance(driver, appiumDriver.Remote):
            print('Inside tear down')
            # driver.quit()
            if currentPlatform == 'ios':
                appium_service.stop()
        if isinstance(driver, browserDriver.chrome.webdriver.WebDriver):
            print('Inside tear down for web ')
            driver.quit()
            # appium_service.stop()
    else:
        print('yielding nothing')
        yield None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    print("came for failed test case",report)
    if report.when == "call":
        print("came for failed test case")
        driver = None
        app_driver = item.funcargs.get('setup_platform', None)
        # print("app_driver instance in tear down ====" , type(app_driver))
        browser_driver = item.funcargs.get('get_admin_server', None)
        if app_driver:
            driver = app_driver
        elif browser_driver:
            driver = browser_driver

        if driver:  
            print("coming to take screenshot for failure")
            if isinstance(driver, webdriver):
                screenshot = driver.get_screenshot_as_png()
                print("secnario is failed so trying to kill app and relaunch ", readConstants("current_app_package"))
                # driver.terminate_app(readConstants("current_app_package"))
                try:
                    # Attempt to terminate using Appium
                    driver_status = driver.terminate_app(readConstants("current_app_package"))
                    print(f"status of the driver is: ======================= {driver_status}")
                except Exception as e:
                    print(f"Appium terminate_app failed: {e}. Trying force stop.")
                    # Fallback to ADB force stop
                    os.system(f"adb shell am force-stop {readConstants('current_app_package')}")
                time.sleep(2)
                print("app killed====lets relaunch")
                driver.activate_app(readConstants("current_app_package"))
                print("app killed====lets relaunch")
                allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.JPG)
                time.sleep(5)
            if isinstance(driver, str):
                print("its roku report")    

        # Make sure the setup_platform fixture is called

        
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                print("reach as scenrio is failed")
                if driver:  
                    if isinstance(driver, webdriver):
                        print("secnario is failed so trying to kill app and relaunch " ,readConstants("current_app_package"))
                        driver.terminate_app(readConstants("current_app_package"))
                        time.sleep(2)
                        print("app killed====lets relaunch")
                        driver.activate_app(readConstants("current_app_package"))
                        print("app killed====lets relaunch")
                        allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)
                        time.sleep(5)
                    
        except Exception as e:
            print('Fail to take screen-shot:', e)


consecutive_failure_abort = "False"
consecutive_failure_count = 5
consecutive_failures = 0


def pytest_configure(config):
    global consecutive_failure_abort, consecutive_failure_count
    consecutive_failure_abort = config.getoption("--consecutive_failure_abort")
    print("Consecutive failure value", consecutive_failure_abort, type(consecutive_failure_abort))
    if config.getoption("--consecutive_failure_count"):
        consecutive_failure_count = int(config.getoption("--consecutive_failure_count"))

    app_file = config.getoption("--appFileName")
    app_package_name = config.getoption("--app_package_name")
    current_platform = config.getoption("--platform")
    webDriverAgentUrl = config.getoption("--webDriverAgentUrl")
    # if not app_file and current_platform == "android":
    #     raise pytest.UsageError("--appFileName is required")

    if not app_package_name and current_platform == "android":
        raise pytest.UsageError("--app_package_name is required")

    # if not webDriverAgentUrl and current_platform == "ios":
        # raise pytest.UsageError("--webDriverAgentUrl is required")

    #isScreenshoreRequired = config.getoption("--screenShotToggle")

    # project_root = os.getcwd()
    # constants_path = os.path.join(project_root, 'utils', 'constants.json')
    # with open(constants_path) as constant_file:
    #     costant_value = json.load(constant_file)
    # costant_value["current_app_package"] = app_package_name
    # print("reading from cons for screenshot ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])
    # print("reading run tim e setup screenshot ===", isScreenshoreRequired)
    # costant_value["NEED_SCREENSHOTS_FOR_PASS"] = isScreenshoreRequired
    # print("reading from cons for screenshot after update ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])

    # print("final value for screenshot ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])

    # with open(constants_path, "w") as constant_file:
    #     json.dump(costant_value, constant_file, indent=4)


def pytest_runtest_logreport(report):
    global consecutive_failures, consecutive_failure_abort, consecutive_failure_count

    if consecutive_failure_abort == 'True':

        if report.when == 'call' and report.failed:
            consecutive_failures += 1

        elif report.when == 'call' and report.passed:
            consecutive_failures = 0
                

        if consecutive_failures >= consecutive_failure_count:
            # print("Aborting test suite due to consecutive failures!")
            pytest.exit(f" \n Aborting test suite due to {consecutive_failure_count} consecutive failures")


def updateConstantFile(contantKey, ConstantValue):
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'util', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)
    costant_value[contantKey] = ConstantValue
    with open(constants_path, "w") as constant_file:
        json.dump(costant_value, constant_file, indent=4) 
    

@pytest.fixture(scope="session", autouse=False)
def mobile_driver():

    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "18.5",
        "deviceName": "Sunil's iPhone",
        "automationName": "XCUITest",
        "appPackage": "com.il.mcd",
        "appActivity": "com.mcdonalds.mobileapp/.MainActivity",
        "noReset": False,
        "fullReset": False
    }
    appium_service = AppiumService()
    appium_service.start(args=['--allow-insecure=adb_shell', '--allow-cors'])
    if not appium_service.is_running:
        raise Exception("Appium server did not start!") 