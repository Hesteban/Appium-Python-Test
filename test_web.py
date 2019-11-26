from appium import webdriver
# Android environment
import unittest
import os
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

class AppiumTest(unittest.TestCase):



    desired_caps = {}

    @classmethod
    def setUpClass(cls):
        print("\n setup class")
        # desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['platformVersion'] = '8.1'
        cls.desired_caps['automationName'] = 'uiautomator2'
        cls.desired_caps['deviceName'] = 'Android device'
        cls.desired_caps['browserName'] = 'Chrome'
        #tambien me funciono con el nombre que devuelve adb devices


    @classmethod
    def setUp(cls):
        print("\n setup ")
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        cls.driver.implicitly_wait(10)


    '''@classmethod
    def tearDown(cls):
        cls.driver.quit()'''




    _username= "m_login_email"
    _password= "m_login_password"
    _submit= "//button[@id='u_0_5']"
    _err_modal ="//div[@data-sigil='m_login_notice']/span"

    def test_01_login_NOK_facebook(self):
        self.driver.get('http://www.facebook.com')
        self.driver.find_element_by_id(self._username).send_keys("hesteban")
        self.driver.find_element_by_id(self._password).send_keys("*qewq12")
        self.driver.find_element_by_xpath(self._submit).click()

        err_modal = self.driver.find_element_by_xpath(self._err_modal)
        self.assertTrue(err_modal.is_displayed() and 'incorrecta' in err_modal.text)




