import numpy as np
# arr = [[j for j in range(11)] for i in range(10)]
# # print(array)
# arr[3][2] = 100
# np_arr = np.array(arr)
# print(np_arr)

arr = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(np.array(arr))