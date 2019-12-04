# -*- coding:utf-8 -*-
# Author : vitoqfli
# Data : 2019/12/4 23:10

def get_desired_capabilities():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "udid": "b166ef99",
        "app": "/Users/xxxx/Desktop/appium自动化测试/AndroidTest-8.0.apk",
        "automationName": "Appium",
        "deviceName": "Galaxy A9",
        "newCommandTimeout": 60,
        "appWaitActivity": "com.ut.roidpt.engine.app.core.BootActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "autoGrantPermissions": True,
        "noReset": True
    }

    {
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "OPPO R11s Plus",
        "appPackage": "com.tencent.tmgp.jxqy",
        "udid": "369ec4aa",
        "appActivity": ".MainActivity"
    }
    return desired_caps

def get_uri():
    return 'http://localhost:4723/wd/hub'
