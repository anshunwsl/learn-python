#! /usr/local/bin/env python3
# -*-coding:UTF-8 -*-
"""
@description   
@author anshunwsl agis216@126.com
@version 1.0.0
"""

import threading

import time


class ThreadingTest(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        info = "{0} delay for {1}".format(self.name, self.delay)
        # print(info)
        time.sleep(self.delay)

        print(info)

        pass


test = ThreadingTest("thread1", 2)
test2 = ThreadingTest("thread2", 10)

test.start()
test2.start()
