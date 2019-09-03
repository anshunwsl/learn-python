#! /usr/local/bin/env python3
# -*-coding:UTF-8 -*-
"""
@description   
@author anshunwsl agis216@126.com
@version 1.0.0
"""

import pickle

my_data = {
    "name": "Python",
    "type": "Language",
    "version": "2.7.5"
}

my_file = open("../data/cache_data.dat", "wb")

pickle.dump(my_data, my_file)

my_file.close()
print("write data success!")

# re load data..


new_file = open("../data/cache_data.dat", "rb")
new_data = pickle.load(new_file)

new_file.close()

print(str(new_data))
