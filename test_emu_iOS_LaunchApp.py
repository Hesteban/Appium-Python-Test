import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumTest(unittest.TestCase):

    app_IOS = "https://github.com/cloudgrey-io/the-app/releases/download/v1.10.0/TheApp-v1.10.0.app.zip"
    desired_caps = {}
    wrong_url = "https://cloudgrey.io"
    appium_url = "https://appiumpro.com"

    @classmethod
    def setUpClass(cls):
        print("\n setup class")
        # desired_caps = {}
        cls.desired_caps['platformName'] = 'iOS'
        cls.desired_caps['platformVersion'] = '12.2'
        cls.desired_caps['deviceName'] = 'iPhone X'
        cls.desired_caps['automationName'] = 'XCUITest'
        cls.desired_caps['app'] = cls.app_IOS
        cls.desired_caps['noReset'] = True
        cls.desired_caps['fullReset'] = False


        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        cls.driver.implicitly_wait(10)

    def setUp(self):
        print("\n setup ")

    @classmethod
    def tearDownClass(cls):
        print("\n tearDown ")
        cls.driver.quit()

    def getWebContext(self, driver):
        contexts = driver.contexts
        print(contexts)
        for context in contexts:
            print(context)
            if 'NATIVE_APP' not in context:
                web_context = context
                break
        else:
            print("Web context not found")
            web_context = None

        return web_context


    def wait_until_visible(self, locator, driver, locator_strategy=By.XPATH):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((locator_strategy, locator)))
            return element
        except Exception as e:
            print("Exception: {}".format(e))
            return None

    def test_01_(self):

        webView_elem = self.driver.find_element_by_accessibility_id("Webview Demo")
        webView_elem.click()
        time.sleep(1)

        # Launching new app
        self.driver.execute_script('mobile: launchApp', {'bundleId': 'com.apple.Preferences'})

        # Terminating new app
        self.driver.execute_script('mobile: terminateApp', {'bundleId': 'com.apple.Preferences'})

        time.sleep(5)









