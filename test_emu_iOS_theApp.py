import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumTest(unittest.TestCase):

    app_IOS = "https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.app.zip"
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
        # 1. Navigate to the webview page
        webView_elem = self.driver.find_element_by_accessibility_id("Webview Demo")
        webView_elem.click()
        time.sleep(1)

        # 2. Attempt to navigate to an incorrect site
        urlInput_elem = self.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextField' and name == 'urlInput'")
        urlInput_elem.send_keys(self.wrong_url)

        gotButton_elem = self.driver.find_element_by_accessibility_id("navigateBtn")
        gotButton_elem.click()

        time.sleep(1)

        #3. Assert that an error message pops up
        '''alert_elem = self.driver.find_element_by_id("Alert")
        assert alert_elem is not None'''
        alert = self.driver.switch_to.alert
        assert "Sorry" in alert.text
        okButton_elem = self.driver.find_element_by_id("OK")
        okButton_elem.click()

        time.sleep(2)

        #4. assert that the webview did not actually go anywhere
        assert urlInput_elem.is_displayed() is True

        #5. attempt to navigate to the correct site
        clearButton_elem = self.driver.find_element_by_id("clearBtn")
        clearButton_elem.click()
        urlInput_elem.send_keys(self.appium_url)
        gotButton_elem.click()
        time.sleep(1)

        #6. assert that the webview went to the right place
        webContext = self.getWebContext(self.driver)
        self.driver.switch_to.context(webContext)
        main_logo = self.wait_until_visible("//a[@class='mainLogo']", self.driver)
        assert main_logo is not None

        self.driver.switch_to.context('NATIVE_APP')
        self.driver.back()
        time.sleep(1)








