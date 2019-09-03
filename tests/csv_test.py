#! /usr/local/bin/env python3
# -*-coding:UTF-8 -*-
"""
@description   
@author anshunwsl agis216@126.com
@version 1.0.0
"""

import pandas as pa

import traceback

data = pa.read_csv("../data/heat_map_data_01.csv", nrows=10, usecols=["lon", "lat"])

print(data)

print("ddd")
traceback.print_exc()
