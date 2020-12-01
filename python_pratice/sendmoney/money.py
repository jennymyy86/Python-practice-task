# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
saved_money = 1000


# 发工资
def send_money():
    # print("发工资了太开心了")
    global saved_money
    saved_money = 2000


# 展示工资
def select_money():
    if saved_money == 1000:
        print(f"存款金额为：{saved_money},还没有发工资，不开心")
    elif saved_money == 2000:
        print(f"存款金额为：{saved_money},发工资了太开心了")


if __name__ == '__main__':
    send_money()
    select_money()
