# ！/usr/bin/env/ python
# -*- coding: utf-8 -*-

import yaml


def get_datas():
    with open('data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


print(get_datas())
