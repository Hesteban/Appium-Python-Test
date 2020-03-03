from appium import webdriver
# Android environment
import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumTest(unittest.TestCase):
    adr_app ="https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.apk"
    desired_caps = {}
    wrong_url = "https://cloudgrey.io"
    appium_url = "https://appiumpro.com"

    @classmethod
    def setUpClass(cls):
        print("\n setup class")
        # desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '7.0'
        cls.desired_caps['automationName'] = 'uiautomator2'
        cls.desired_caps['deviceName'] = 'ZY223GGZ9H'
        # tambien me funciono con el nombre que devuelve adb devices

        #cls.desired_caps['app'] = '/Users/hesteban/Appium Course/TheApp-v1.10.0.apk'
        cls.desired_caps['app'] = cls.adr_app
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
            if 'cloudgrey' in context:
                return context

    def wait_until_visible(self, locator, driver, locator_strategy=By.XPATH):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((locator_strategy, locator)))
            return element
        except Exception as e:
            print("Exception: {}".format(e))
            return None

    def test_01_(self):
        screen_orientation = self.driver.orientation
        print(screen_orientation)
        if screen_orientation != 'LANDSCAPE':
            self.driver.orientation = "LANDSCAPE"
        time.sleep(5)
        dimension = self.driver.get_window_size()
        print(dimension)

        screenshot_path = os.path.dirname(os.path.realpath(__file__))
        self.driver.save_screenshot(os.path.join(screenshot_path, 'screenshot_1.png'))
