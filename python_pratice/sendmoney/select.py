# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-


# 展示工资
import save


def select_money():
    if save.saved_money == 1000:
        print(f"存款金额为：{save.saved_money},还没有发工资，不开心")
    elif save.saved_money == 2000:
        print(f"存款金额为：{save.saved_money},发工资了太开心了")
