import numpy as np

if __name__ == "__main__":
    ndarray_data = np.array([[1, 2], [3, 4]])

    print(ndarray_data)

    dt = np.dtype(np.int32)
    print(dt)
    # print(ndarray_data.shape)
    # print(ndarray_data.size)
    # print(ndarray_data.dtype)

    new_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(new_array.shape)
    new_array.shape = (5, 2)
    print(new_array)

    print("call reshape method result is ::")
    new_array.reshape((5, 2))
    print(new_array)

    # dt1 = np.dtype([('name', "S20"), ("age", np.int8), ("marks", "f4")])
    #
    # new_array = np.array([["wangsl", 100, 20], ["yubao", 200, 100]], dtype=dt1)
    #
    # print(new_array)
    # student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    # a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    # print(a)

    x_data = np.empty([3, 3], dtype=int)
    print(x_data)
