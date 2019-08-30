#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@description 
@author wangsl agis216@126.com
@version v1.0.0
"""


class User(object):
    __user_name = ""
    __age = 10
    __address = ""

    def __init__(self, user_name, age, address):
        self.__user_name = user_name
        self.__age == age
        self.__address = address

    pass

    def show_info(self):
        print("user name is {}".format(self.__user_name))
        print("age  is {}".format(self.__age))
        print("address  is {}".format(self.__address))
        pass
