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
        cls.desired_caps['deviceName'] = 'Nexux_5_2'
        cls.desired_caps['app'] = cls.apk_path

    @classmethod
    def setUp(self):
        print("\n setup ")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    '''def test_01_locate_elements_basic(self):
        print("\n test")
        #acc_button = self.driver.find_element_by_name('Accessibility')
        acc_button = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']")
        #print(acc_button)
        acc_button.click()
        pref_button = self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']")
        pref_button.click()
        self.driver.find_element_by_id('android:id/checkbox').click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[2]").click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("123dqw!!!")
        self.driver.find_element_by_id('android:id/button1').click()
    

    def test_02_locate_elements_uiautomator(self):
        print("\n test 2")
        #acc_button = self.driver.find_element_by_name('Accessibility')
        acc_button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")')
        #print(acc_button)
        acc_button.click()
    
    def test_03_touch_actions_tap_long_press(self):
        print("\n test 2")
        action= TouchAction(self.driver)
        views_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']")
        views_elem.click()
        exp_list_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Expandable Lists']")
        #exp_list_elem.click()
        action.tap(exp_list_elem).perform()
        time.sleep(2)
        cus_adp_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='1. Custom Adapter']")
        # exp_list_elem.click()
        action.tap(cus_adp_elem).perform()
        p_names_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='People Names']")
        # exp_list_elem.click()
        action.long_press(p_names_elem, duration=2000).release().perform()

        modal_elem = self.driver.find_element_by_class_name('android.widget.ListView')

        self.assertTrue(modal_elem.is_displayed())

    

    def test_04_touch_actions_swipe(self):
        print("\n test 2")
        action= TouchAction(self.driver)
        views_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']")
        views_elem.click()
        date_widgets_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Date Widgets']")
        #exp_list_elem.click()
        action.tap(date_widgets_elem).perform()
        inline_elem = self.driver.find_element_by_xpath("//android.widget.TextView[@text='2. Inline']")
        inline_elem.click()
        nine_elem = self.driver.find_element_by_xpath("//*[@content-desc='9']")
        nine_elem.click()

        fifteen_elem = self.driver.find_element_by_xpath("//*[@content-desc='15']")
        fortyfive_elem = self.driver.find_element_by_xpath("//*[@content-desc='45']")

        action.long_press(fifteen_elem, duration=2000).move_to(fortyfive_elem).release().perform()

        hour_elem = self.driver.find_element_by_id('android:id/hours')
        min_elem = self.driver.find_element_by_id('android:id/minutes')

        self.assertTupleEqual(('9','45'),(hour_elem.text,min_elem.text))

    '''

    def test_05_locate_elements_uiautomator_UiScrollable(self):
        print("\n test 2")
        # acc_button = self.driver.find_element_by_name('Accessibility')
        views_button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Views")')
        views_button.click()

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("WebView"))')