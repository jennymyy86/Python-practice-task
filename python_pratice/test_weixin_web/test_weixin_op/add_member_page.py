# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_weixin_web.test_weixin_op.basepage import BasePage
from test_weixin_web.test_weixin_op.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 前面加_表示这个变量私有化，只有这个类能用到，其他类用不到
    _ele_name = (By.ID, "username")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_mail = (By.ID, "memberAdd_mail")

    def add_member(self, name, id, mail):
        # “*”表示可以解析元祖
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    # PO设计模式，如果需要测试失败的，需要重新定义一个函数
    def add_member_fail(self, name, id, mail):
        # “*”表示可以解析元祖
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)
