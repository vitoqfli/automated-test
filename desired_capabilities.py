# -*- coding:utf-8 -*-
# Author : vitoqfli
# Data : 2019/12/4 23:10

def get_desired_capabilities():
    desired_caps = {
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
