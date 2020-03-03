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
    desired_caps = {}
    android_photo_path = '/storage/emulated/0/Download'

    @classmethod
    def setUpClass(cls):
        print("\n setup class")
        # desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '7.0'
        cls.desired_caps['automationName'] = 'uiautomator2'
        cls.desired_caps['deviceName'] = 'ZY223GGZ9H'
        # tambien me funciono con el nombre que devuelve adb devices


        cls.desired_caps['appPackage'] = 'com.google.android.apps.photos'
        cls.desired_caps['appActivity'] = '.home.HomeActivity'

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

        image_name = 'screenshot.jpg'
        image_path = os.path.abspath(image_name)
        print(image_path)
        print(os.path.join(self.android_photo_path,image_name))

        self.driver.push_file(os.path.join(self.android_photo_path,image_name), image_path)
        time.sleep(5)

