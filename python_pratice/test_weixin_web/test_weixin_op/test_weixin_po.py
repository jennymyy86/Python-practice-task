# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
import pytest

from test_weixin_web.test_weixin_op.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,mail", [("lisi", "lisi456", "lisi456@qq.com")])
    def test_contactpage_add_member(self, name, id, mail):
        namelist = self.main.goto_contact_page().clic_add_member().add_member(name, id, mail).get_member()
        assert name in namelist

    @pytest.mark.parametrize("name,id,mail", [("wangwu", "wangwu456", "wangwu456@qq.com")])
    def test_mainpage_add_memeber(self, name, id, mail):
        namelist = self.main.goto_add_member_page().add_member(name, id, mail).get_member()
        assert name in namelist
