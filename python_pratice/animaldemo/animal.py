# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
1、自己写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、将数据配置到yaml文件里
'''

import yaml


# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

class Animal:
    # name: str = None
    # colour: str = None
    # age: int = 0
    # sex: str = "male"

    def __init__(self, name, colour, age, sex):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex

    def crying(self):
        print(f"{self.name}会叫")

    def running(self):
        print(f"{self.name}会跑")


# 创建子类【猫】，继承【动物类】，

class Cat(Animal):
    # 复写父类的__init__方法，继承父类的属性，且 添加一个新的属性，毛发=短毛
    hair: str = "短毛"

    def __init__(self, name, colour, age, sex):
        super().__init__(name, colour, age, sex)

    # 添加一个新的方法， 会捉老鼠，
    def catchingmouse(self):
        print(f"{self.name}会捉老鼠")

    # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def crying(self):
        print(f"{self.name}会喵喵叫")


# 创建子类【狗】，继承【动物类】
class Dog(Animal):
    # 复写父类的__init__方法，继承父类的属性，添加一个新的属性，毛发=长毛
    hair: str = "长毛"

    def __init__(self, name, colour, age, sex):
        super().__init__(name, colour, age, sex)

    # 添加一个新的方法， 会看家
    def lookafterhouse(self):
        print(f"{self.name}会看家")

    # 复写父类的【会叫】的方法，改成【汪汪叫】
    def crying(self):
        print(f"{self.name}会汪汪叫")


# 调用 name== ‘main’：
if __name__ == '__main__':
    # 从yaml文件中读取数据
    with open('data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    #    print(datas)
    # 创建一个猫猫实例
    # p_gf = Cat("Garfield", "yellow", 1, "male")
    name = datas['default']['default_cat']['name']
    colour = datas['default']['default_cat']['colour']
    age = datas['default']['default_cat']['age']
    sex = datas['default']['default_cat']['sex']
    p_gf = Cat(name, colour, age, sex)
    # 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
    print(p_gf.name, p_gf.colour, p_gf.age, p_gf.sex, p_gf.hair)
    # 调用捉老鼠的方法
    p_gf.catchingmouse()
    p_gf.crying()

    # # 创建一个狗狗实例
    # #p_jm = Dog("金毛", "黄白", 3, "公")
    name = datas['default']['default_dog']['name']
    colour = datas['default']['default_dog']['colour']
    age = datas['default']['default_dog']['age']
    sex = datas['default']['default_dog']['sex']
    p_jm = Dog(name, colour, age, sex)
    # 打印【狗狗的姓名，颜色，年龄，性别，毛发】
    print(p_jm.name, p_jm.colour, p_jm.age, p_jm.sex, p_jm.hair)
    # 调用【会看家】的方法
    p_jm.lookafterhouse()
    p_jm.crying()
