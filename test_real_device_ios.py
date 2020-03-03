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
        cls.desired_caps['platformName'] = 'iOS'
        cls.desired_caps['platformVersion'] = '12.4.1'
        cls.desired_caps['automationName'] = 'XCUITest'
        cls.desired_caps['deviceName'] = 'Iphone7'
        cls.desired_caps['udid'] = 'be7bb8ddffd25704d77ad1726dc1f47f4f4ab10c'
        cls.desired_caps['xcodeOrgId'] = '2W7Q5LPE7R'
        cls.desired_caps['xcodeSigningId'] = 'iPhone Developer'
        cls.desired_caps['app'] = '/Users/hesteban/Library/Developer/Xcode/DerivedData' \
                                  '/UICatalog-eghigligsmibasfjjueksgojnplx/Build/Products/Debug-iphoneos/UICatalog.app'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def setUp(self):
        print("\n setup ")


    @classmethod
    def tearDownClass(cls):
        print("\n tearDown ")
        cls.driver.quit()

    @unittest.skip
    def test_01_test01(self):
        self.driver.find_element_by_accessibility_id("Alert Views").click()
        text_extry_button = self.driver.find_element_by_ios_predicate('type == "XCUIElementTypeStaticText" AND value =="Text Entry"')
        text_extry_button.click()
        '''tex_extry_box = self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="A Short Title Is Best"]/'
                                                          'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/'
                                                          'XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther')'''
        tex_extry_box = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeAlert[`name == "A Short Title Is Best"`]/'
                                                          'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/'
                                                          'XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/'
                                                          'XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther')
        tex_extry_box.send_keys("Hello")
        self.driver.find_element_by_accessibility_id("OK").click()

        self.driver.back()

        dimension = self.driver.get_window_size()
        print(dimension)
        x = dimension['width'] / 2
        start = dimension['height'] * 0.60
        end = dimension['height'] * 0.10

        self.driver.swipe(x, start, x, end, 2000)
        self.driver.find_element_by_id('Steppers').click()

        increment_button = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeButton[`name =="Increment"`][1]')
        increment_button.click()
        increment_button.click()

        counter_value = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeStaticText[1]').get_attribute('value')
        print('Counter value: {}'.format(counter_value))
        assert(counter_value == '2')


    def test_02_PickerWheel(self):
        self.driver.find_element_by_accessibility_id("Picker View").click()
        central_picker = self.driver.find_element_by_ios_predicate('type =="XCUIElementTypePickerWheel" '
                                                                   'and name == "Green color component value"')

        central_picker.send_keys("220")
        assert(central_picker.get_attribute("value") == "220")
