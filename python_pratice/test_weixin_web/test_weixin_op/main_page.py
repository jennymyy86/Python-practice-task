# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_weixin_web.test_weixin_op.add_member_page import AddMemberPage
from test_weixin_web.test_weixin_op.basepage import BasePage
from test_weixin_web.test_weixin_op.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact_page(self):
        # 点击通讯录
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item .index_service_cnt_item_title").click()
        return AddMemberPage()
