#! /usr/local/bin/env python3
# -*-coding:UTF-8 -*-
"""
@description   
@author anshunwsl agis216@126.com
@version 1.0.0
"""

import traceback

import logging

login_config = {
    "level": logging.DEBUG,
    "filename": "../data/log1.txt",
    "filemode": "w",
}

logging.basicConfig(level=logging.DEBUG, filename="../data/log.txt", filemode="w")
# logging.basicConfig(login_config)

my_data = {
    "name": "wsl"
}

#
try:
    print(my_data["age"])
except KeyError as error:

    print(str(error))
    logging.info("error")
    traceback.print_exc()
