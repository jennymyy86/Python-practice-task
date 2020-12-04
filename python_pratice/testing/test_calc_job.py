# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：

使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_ids = datas_add['myid']
    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_ids = datas_div['myid']


class TestCalcJob:

    # 定义类级别 setup
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 定义类级别 teardown
    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas,
        ids=add_ids
    )
    # 定义加法测试用例
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
            assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas,
        ids=div_ids
    )
    # 定义除法测试用例
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
            assert result == expect
