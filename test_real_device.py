from appium import webdriver
# Android environment
import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

class AppiumTest(unittest.TestCase):

    apks_dir_path = 'C:\\ANDROID'
    apk_filename = "ApiDemos-debug.apk"
    apk_path = os.path.join(apks_dir_path, apk_filename)
    print(apk_path)
    desired_caps = {}

    @classmethod
    def setUpClass(cls):
        print("\n setup class")
        # desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '8.1'
        cls.desired_caps['automationName'] = 'uiautomator2'
        cls.desired_caps['deviceName'] = 'Android device'
        #tambien me funciono con el nombre que devuelve adb devices

        cls.desired_caps['app'] = cls.apk_path

    @classmethod
    def setUp(self):
        print("\n setup ")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def test_01_scroll_based_on_size(self):
        dimension = self.driver.get_window_size()
        print(dimension)
        x = dimension['width'] /2
        start = dimension['height'] * 0.60
        end = dimension['height'] * 0.10

        views_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']")
        views_elem.click()
        self.driver.swipe(x,start,x,end,2000)
        time.sleep(5)