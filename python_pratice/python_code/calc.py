# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
# 计算器
class Calculator:

    # 加法
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            print(e)
            return "请输入数字"

    # 减法
    def sub(self, a, b):
        try:
            return a - b
        except Exception as e:
            print(e)
            return "请输入数字"

    # 乘法
    def mul(self, a, b):
        try:
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return a * b
            else:
                return "请输入数字"
        except Exception as e:
            print(e)

    # 除法
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(e)
            return "除数运算中分母不能为0"
        except Exception as value_err:
            print(value_err)
            return "请输入数字"
