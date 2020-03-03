import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


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
        #cls.desired_caps['noReset'] = True
        #cls.desired_caps['fullReset'] = False


        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        cls.driver.implicitly_wait(10)

    def setUp(self):
        print("\n setup ")

    def tearDown(self):
        print("\n Teardown ")
        print("\n Returning to home page ")

        while not self.is_elem_visible('Choose An Awesome View', self.driver, MobileBy.ACCESSIBILITY_ID ):
            self.driver.back()


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

    def is_elem_visible(self, locator, driver, locator_strategy=By.XPATH):
        try:
            elem = self.driver.find_element(locator_strategy,locator)
            print("\n Elem {} located by {} is visible".format(locator, locator_strategy))
            return True
        except Exception as e:
            print("Exception: {}".format(e))
            return False

    def wait_until_visible(self, locator, driver, locator_strategy=By.XPATH):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((locator_strategy, locator)))
            print("\n Elem {} located by {} is visible".format(locator, locator_strategy))
            return element
        except Exception as e:
            print("Exception: {}".format(e))
            return None


    def test_01_Normal_Login(self):
        login_elem = self.driver.find_element_by_accessibility_id("Login Screen")
        login_elem.click()
        time.sleep(1)

        login_title = self.wait_until_visible('//XCUIElementTypeStaticText[@name="Login"]', self.driver)
        assert login_title is not None


        username_elem = self.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextField' and name == 'username'")
        username_elem.send_keys('alice')

        pass_elem = self.driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeSecureTextField' and name == 'password'")
        pass_elem.send_keys('mypassword')


        gotButton_elem = self.driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="loginBtn"])[2]')
        gotButton_elem.click()

        logged_elem = self.wait_until_visible('You are logged in as alice', self.driver, MobileBy.ACCESSIBILITY_ID)
        assert logged_elem is not None


    def test_02_logout(self):
        login_elem = self.driver.find_element_by_accessibility_id("Login Screen")
        login_elem.click()
        time.sleep(1)

        Logout_elem = self.driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="Logout"])[2]')
        Logout_elem.click()

        login_title = self.wait_until_visible('//XCUIElementTypeStaticText[@name="Login"]', self.driver)
        assert login_title is not None


    def test_03_Login_deeplink(self):

        self.driver.get("theapp://login/alice/mypassword")

        logged_elem = self.wait_until_visible('You are logged in as alice', self.driver, MobileBy.ACCESSIBILITY_ID)
        assert logged_elem is not None





