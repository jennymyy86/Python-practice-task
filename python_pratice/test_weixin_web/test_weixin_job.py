# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 获取cookie
# 使用序列化的方法用cookie登录，获取cookie序列化后存入yaml
def test_get_cookie():
    # 调用chromeoptions方法
    opt = webdriver.ChromeOptions()
    # 设置复用浏览器的地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    # 设置隐式等待
    driver.implicitly_wait(3)
    cookies = driver.get_cookies()
    with open("cookiedata.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookies, f)
    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 设置cookie前访问企业微信扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853156199960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'RvqRzwgLF9aoqGa5XBI1U3MoH2re7QAq5dzKU51LR3MpiZSPlSYemdO6v0Tm3Z0l1Sf4E49tiQdt-Y6aw8wrRAMMu622QC4kY5e8HJM5RGAsovmd714WuaR-gIBnYVsHZQ4BOVxXEohXufEFylHv5oRR3ia8QJL34Aq7rXH_tOMaPC4OKX57uO8X9KcapOBhUEFmnDxsON5a6wPQ5vZqZUd9qnSkTrbd5nR0kuaRdsBYYmZsjq5urGfPJjqjpsKrnqI9yjn14f62HfGgEGVUEA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853156199960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325054207532'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '5ufwWvk5wkwBVtSRLDEiGUV5DaIo0xREIqzPKAlnp10sZfpVy4lJj2v6I0H9nxZC'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6816272'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8242869524'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640079185, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608538241,1608539530,1608542980,1608543185'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608551074, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '99t8otm'}, {'domain': '.qq.com', 'expiry': 1608629597, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1235252420.1608519642'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608543185'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '34122556031522342'}, {'domain': '.qq.com', 'expiry': 1608543245, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1671615197, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2008513955.1608519642'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640055538, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1611135200, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    with open("cookiedata.yaml", encoding="utf-8") as f:
        yaml_datas = yaml.safe_load(f)
    for cookie in yaml_datas:
        # 把cookie传给driver
        driver.add_cookie(cookie)
    # 设置cookie后再次访问企业微信
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    # 显示等待，等待元素是可点击状态
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    driver.find_element_by_id("username").send_keys("Jenny")
    driver.find_element_by_id("memberAdd_acctid").send_keys("jenny86")
    driver.find_element_by_id("memberAdd_mail").send_keys("123456789@qq.com")
    driver.find_element_by_css_selector(".js_btn_save").click()
    time.sleep(1)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        # 获取元素属性title的值，存入list内
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    # 断言目标名字是否在列表内
    assert "Jenny" in name_list
    driver.quit()
