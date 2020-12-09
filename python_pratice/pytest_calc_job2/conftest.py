# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
from typing import List

import pytest
import yaml
import os
from python_code.calc import Calculator

# 获取当前文件的路径，然后进行路径拼接得到绝对路径，相对路径少用，容易出错
yaml_file_path = os.path.dirname(__file__) + "/calc_datas/calc.yaml"

with open(yaml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_ids = datas_add['myid']
    datas_sub = datas['sub']
    sub_datas = datas_sub['datas']
    sub_ids = datas_sub['myid']
    datas_mul = datas['mul']
    mul_datas = datas_mul['datas']
    mul_ids = datas_mul['myid']
    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_ids = datas_div['myid']


# 定义一个获取实例的fixture方法
@pytest.fixture()
def get_calc():
    calc = Calculator()
    return calc


@pytest.fixture(params=add_datas, ids=add_ids)
def get_add_datas(request):
    print("开始加法计算")
    datas = request.param
    # print(f"request.param里面的数据是：{datas}")
    yield datas
    print("计算结束")


@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_sub_datas(request):
    print("开始减法计算")
    datas = request.param
    # print(f"request.param里面的数据是：{datas}")
    yield datas
    print("计算结束")


@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_mul_datas(request):
    print("开始乘法计算")
    datas = request.param
    # print(f"request.param里面的数据是：{datas}")
    yield datas
    print("计算结束")


@pytest.fixture(params=div_datas, ids=div_ids)
def get_div_datas(request):
    print("开始除法计算")
    datas = request.param
    # print(f"request.param里面的数据是：{datas}")
    yield datas
    print("计算结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    # print("items")
    # print(items)
    # 实现用例反转执行,即自定义用例执行顺序
    # items.reverse()

    # 在钩子函数里修改测试用例参数编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # item.nodeid 拿到的是测试用例的名称
        # 自动给测试用例加上标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
