import numpy as np
import pandas as pa
import os


# pip


def get_user(user_name, age):
    #
    print(user_name)
    print("age is %s" % age)

    pass


if __name__ == '__main__':
    print("hello the world..")

    #
    get_user("wangshanglang", 100)
    new_data = np.array([1, 2, 3, 4])
    #
    file_header = ["name", "age", "address"]

    # csv_data = np.loadtxt(os.getcwd() + "/data/test_csv.csv")
    # csv_data = pa.read_csv(os.getcwd() + "/data/test_csv.csv")
    csv_data = pa.read_csv("./data/test_csv.csv")
    print(new_data)
    print(csv_data)
    print(pa._version.get_versions())
