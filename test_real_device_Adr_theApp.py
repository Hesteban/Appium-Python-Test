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
        webView_elem = self.driver.find_element_by_accessibility_id("Webview Demo")
        webView_elem.click()
        urlInput_elem = self.wait_until_visible("//android.widget.EditText[@content-desc='urlInput']", self.driver)
        assert urlInput_elem is not None

        urlInput_elem.send_keys(self.wrong_url)
        gotButton_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Go']")
        gotButton_elem.click()

        time.sleep(1)

        #alert_elem = self.driver.find_element_by_id("android:id/alertTitle")
        #assert alert_elem is not None
        alert = self.driver.switch_to.alert
        assert "Sorry" in alert.text

        okButton_elem = self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']")
        okButton_elem.click()

        time.sleep(2)

        clearButton_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Clear']")
        clearButton_elem.click()
        urlInput_elem.send_keys(self.appium_url)
        gotButton_elem.click()
        time.sleep(1)

        webContext = self.getWebContext(self.driver)
        self.driver.switch_to.context(webContext)
        main_logo = self.wait_until_visible("//a[@class='mainLogo']", self.driver)
        assert main_logo is not None

        self.driver.switch_to.context('NATIVE_APP')
        self.driver.back()
        time.sleep(1)
