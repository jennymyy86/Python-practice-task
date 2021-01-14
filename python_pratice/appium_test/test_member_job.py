# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_member(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("Jack")
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/eq7").send_keys("15012344321")
        self.driver.find_element_by_id("com.tencent.wework:id/gur").click()
        failetext = self.driver.find_element_by_xpath("//*[contains(@text,'手机已存在于通讯录')]").text
        assert failetext == "手机已存在于通讯录，无法添加"
