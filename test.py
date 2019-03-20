from appium import webdriver
# Android environment
import unittest
import os
from appium import webdriver

class AppiumTest(unittest.TestCase):

	apks_dir_path = 'E:\\ANDROID_APKS'
	apk_filename = "ApiDemos-debug.apk"
	apk_path= os.path.join(apks_dir_path, apk_filename)
	print(apk_path)
	desired_caps = {}

	@classmethod
	def setUpClass(cls):
		print("\n setup class")
		# desired_caps = {}
		cls.desired_caps['platformName'] = 'Android'
		cls.desired_caps['platformVersion'] = '9.1'
		cls.desired_caps['automationName'] = 'uiautomator2'
		cls.desired_caps['deviceName'] = 'Pixel_2_OK'
		cls.desired_caps['app'] = cls.apk_path


	@classmethod
	def setUp(self):
		print("\n setup ")
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)



	def test_01(self):
		print("\n test")
		assert False