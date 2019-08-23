#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    print("hello the world..")

    # file_data = open("../data/temp.txt", 'w')
    # file_data.write("hello the worlf")
    # file_data.close()

    file_data = open("../data/temp.txt", "r")

    info_text_view = file_data.readlines()

    for info_text in info_text_view:
        print(info_text)

    # print(info_text_view)
