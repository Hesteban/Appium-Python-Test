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

    apks_dir_path = 'C:\\ANDROID'
    apk_filename = "TheApp-v1.10.0.apk"
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
        cls.desired_caps['deviceName'] = 'Nexus_5_2'
        cls.desired_caps['app'] = cls.apk_path

    @classmethod
    def setUp(self):
        print("\n setup ")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDown(self):
        print("\n tearDown ")
        self.driver.quit()

    # def test_01_first_ex(self):
    #     print("\n test")
    #     message = "Hola Automation!!!"
    #     echo_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Echo Box']")
    #     #print(acc_button)
    #     echo_elem.click()
    #     self.driver.find_element_by_accessibility_id("messageInput").send_keys(message)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Save']").click()
    #
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Hola Automation!!!']"))
    #     )
    #     assert element is not None
    #
    #     response_elem_list=self.driver.find_elements_by_accessibility_id("Hola Automation!!!")
    #     print(len(response_elem_list))
    #     if len(response_elem_list)>0:
    #         assert True
    #     else:
    #         assert False

    def test_WebView_and_switch_context(self):
        '''
        1-Navigate to a webview
        2-Change context to webview
        3-Validate an element on the webview context using Selenium strategy
        4-Change context to Native
        5-Press native back button
        '''
        print("\n test")
        self.driver.find_element_by_accessibility_id("Webview Demo").click()
        # self.driver.find_element_by_accessibility_id("urlInput").send_keys("https://appiumpro.com")
        urlInput= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@content-desc='urlInput']"))
        )
        if urlInput is not None:
            urlInput.send_keys("https://appiumpro.com")
        self.driver.find_element_by_accessibility_id("navigateBtn").click()
        time.sleep(5)
        context_list = self.driver.contexts
        for context in context_list:
            print(context)
        webview_context = self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_io.cloudgrey.the_app')
        main_logo= self.driver.find_element_by_xpath("//a[@class='mainLogo']")
        assert main_logo is not None
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.back()
        time.sleep(5)


