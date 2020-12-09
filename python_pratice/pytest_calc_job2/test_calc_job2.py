# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
补全计算器（加减乘除）的测试用例
使用数据的数据驱动，完成加减乘除用例的自动生成
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合allure 生成测试结果报告
'''
import allure
import pytest


class TestCalcJob2:

    # 装饰器指定执行用例的顺序
    @pytest.mark.run(order=1)
    @allure.story("测试加法")
    # 定义加法测试用例
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            with allure.step("计算两个数相加"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    # 定义减法测试用例
    @pytest.mark.run(order=2)
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            with allure.step("计算两个数相减"):
                result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    # 定义乘法测试用例
    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            with allure.step("计算两个数相乘"):
                result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]

    # 定义除法测试用例
    @pytest.mark.run(order=4)
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("计算两个数相除"):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_div_datas[2]
