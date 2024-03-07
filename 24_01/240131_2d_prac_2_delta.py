import numpy as np
n = int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        lst[i][j] = cnt
        cnt += 1

print(np.array(lst))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sum_abs = 0

for x in range(n):
    for y in range(n):
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < n and 0 <= ny < n:
                sum_abs += abs(lst[x][y] - lst[nx][ny])


print(sum_abs)