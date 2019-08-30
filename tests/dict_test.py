#! /usr/local/bin/env python3
# -*-coding:UTF-8 -*-
"""
@description   
@author anshunwsl agis216@126.com
@version 1.0.0
"""
import collections

import copy


def print_info(info):
    """
    ddd
    """
    pass


Scale = collections.namedtuple("Scale", "name age address")

info_data = []
#

info_data.append(Scale("wangshanglang", 20, "shanzhen"))
info_data.append(Scale("yubao", 100, "china"))

#

for (name, age, address) in info_data:
    print(name, age, address)

set_data = set()

new_data = [1, 1, 1, 1, 3, 4, 2]

single_data = set(new_data)
#
print(single_data)


def show_user(name_, age_, address_):
    try:
        info = "name is {0} \n age is {1}\n address is {2}".format(name_, age_, address_)
        print(info)
    except Exception as dd:
        print(dd.args)
    finally:
        print("fish!")
    pass


print("-" * 50)
for item in info_data:
    show_user(*item)

print("-" * 50)

for item in info_data:
    show_user(item.name, item.age, item.address)

print("-" * 50)

new_scale = Scale("1", 1, "1")

print(new_scale)


class User(object):
    def __init__(self):
        pass

    def show_user(self, age):
        print(age)
        pass


user_info = [1, 2, [12, 11], 4, 4.34, 6]

user_info_1 = user_info[:]

user_info_2 = copy.deepcopy(user_info)

user_info_1[2][1] = 100
user_info_2[2][1] = 200

print(user_info)
print(user_info_1)
print(user_info_2)
