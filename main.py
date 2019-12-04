# -*- coding:utf-8 -*-
# Author : vitoqfli
# Data : 2019/12/4 23:11

from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import  expected_conditions as EC

import unittest

import time

from time import sleep

import desired_capabilities


class AndroidTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        desired_cap = desired_capabilities.get_desired_capabilities()

        uri = desired_capabilities.get_uri()

        self.driver = webdriver.Remote(uri,desired_cap)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def leftSwipe(self):
        window_size = self.driver.get_window_size()
        self.driver.swipe(start_x=window_size["width"] * 0.8,
                          start_y=window_size["height"] * 0.5,
                          end_x=window_size["width"] * 0.1,
                          end_y=window_size["height"] * 0.5 )

    def wait_for_element(self,xpath=None, id=None, index=None, timeOut=20):
        startTime = time.time()
        nowTime = time.time()
        while nowTime - startTime < timeOut:
            try:
                if xpath is not None:
                    el = self.driver.find_element_by_xpath(xpath)
                    return el
            except:
                pass

            try:
                if id is not None:
                    if index is not None:
                        return self.driver.find_element_by_id(id)[index]
                    else:
                        return self.driver.find_element_by_id(id)
            except:
                pass

            sleep(1)

            nowTime = time.time()

        raise Exception("Element xpath[%s] id[%s] index[%s] is not found" % (xpath, id, index))


    def test_a_utFrame(self):

        print(self.driver.current_activity)
        self.wait_for_element(id="com.ut.androidtest:id/downloadBtn").click()

        time.sleep(8)
        circulation = 2

        while circulation > 0:
            time.sleep(1)
            self.leftSwipe()
            self.leftSwipe()


            self.wait_for_element(xpath="//*[@text='欢迎使用']").click()
            time.sleep(1)

            loginBtn = self.wait_for_element(xpath="//*[@text='登    录']")
            loginBtn.click()
            time.sleep(1)

            self.wait_for_element(xpath="//*[@text='XX申请']").click()
            time.sleep(1)

            item = self.wait_for_element(xpath="//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]")
            item.click()
            time.sleep(1)


            backBtn = self.wait_for_element(id="com.ut.androidtest:id/imageTextBt_imageBt")
            backBtn.click()
            time.sleep(.5)

            #系统返回键
            self.driver.press_keycode(keycode=4)
            time.sleep(1)

            self.wait_for_element(xpath="//*[@text='日志查询']").click()
            time.sleep(1.5)

            self.wait_for_element(xpath="//*[@text='录像日志']").click()
            self.wait_for_element(xpath="//*[@text='领用日志']").click()
            self.wait_for_element(xpath="//*[@text='归还日志']").click()
            self.wait_for_element(xpath="//*[@text='报警日志']").click()
            time.sleep(.5)

            self.wait_for_element(xpath="//*[@text='消息']").click()
            self.wait_for_element(xpath="//*[@text='首页']").click()
            self.wait_for_element(xpath="//*[@text='我']").click()
            time.sleep(1)

            updateBtn = self.wait_for_element(xpath="//*[@text='版本更新']")
            updateBtn.click()
            time.sleep(10)

            self.assertIsNotNone(self.wait_for_element(xpath="//*[@text='Hello world']"), "版本更新失败")

            circulation -= 1




if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(AndroidTest("test_a_utFrame"))
    unittest.TextTestRunner(verbosity=2).run(suite)