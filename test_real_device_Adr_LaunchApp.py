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
    adr_app ="https://github.com/cloudgrey-io/the-app/releases/download/v1.10.0/TheApp-v1.10.0.apk"
    desired_caps = {}
    wrong_url = "https://cloudgrey.io"
    appium_url = "https://appiumpro.com"
    number_to_call =  '609540652'

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
        webView_elem = self.driver.find_element_by_accessibility_id("Webview Demo")
        webView_elem.click()
        urlInput_elem = self.wait_until_visible("//android.widget.EditText[@content-desc='urlInput']", self.driver)
        assert urlInput_elem is not None

        # Launh App using start activity
        self.driver.start_activity("com.android.dialer", "DialtactsActivity")

        # Make a call
        dialer = self.driver.find_element_by_accessibility_id("teclado")
        dialer.click()

        digits = self.driver.find_element_by_id("com.android.dialer:id/digits")
        digits.send_keys(self.number_to_call)

        ring = self.driver.find_element_by_accessibility_id("marcar")
        ring.click()

        #destiny = self.driver.find_element_by_id('com.android.dialer:id/name')
        destiny = self.wait_until_visible('com.android.dialer:id/name', self.driver, By.ID)
        destiny_value = destiny.get_attribute("text")
        print("\n Number to call: {}".format(destiny_value))
        assert self.number_to_call == destiny_value.replace(" ", "")

        # End call
        hungup = self.driver.find_element_by_accessibility_id("Finalizar llamada")
        hungup.click()

        time.sleep(5)
