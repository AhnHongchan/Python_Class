import numpy as np
n = int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        lst[i][j] = cnt
        cnt += 1

print(np.array(lst))

sum = 0


for x in range(n):
    sum += lst[x][x]
    sum += lst[n-1-x][x]

if n % 2 == 1:
        sum -= lst[int((n-1)/2)][int((n-1)/2)]

print(sum)
