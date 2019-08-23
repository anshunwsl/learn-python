#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@description
@author wangsl agis216@126.com
@version v1.0.0
"""

import json

if __name__ == "__main__":
    json__data = open("../data/heat_map_data_01.json", "r")

    json_object = json__data.readlines()

    json_string = "".join(json_object)

    data = json.loads(json_string, "UTF-8")

    points = data["heatData"]

    result_file = open("../data/heat_map_data_01.csv", "w")
    result = "lon,lat,num\r\n"

    for point in points:
        item = point["lng"] + ","+point["lat"] + "," + point["num"] + "\r\n"
        result += item

    print(data["heatData"])

    try:
        result_file.write(result)

    finally:
        result_file.close()
        pass
    print(result)

    # print(json_object["heatData"])
