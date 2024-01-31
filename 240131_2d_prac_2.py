import numpy as np
n = int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        lst[i][j] = cnt
        cnt += 1

print(np.array(lst))

sum_abs = 0

for x in range(n):
    for y in range(n):
        if x-1 >= 0 and y-1 >= 0 and x+1 <= 4 and y+1 <= 4:
            sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x][y+1]-lst[x][y]) + abs(lst[x+1][y]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))
        elif x-1 < 0:
            if y-1 < 0:
                sum_abs += (abs(lst[x][y+1]-lst[x][y]) + abs(lst[x+1][y]-lst[x][y]))
            elif y+1 > 4:
                sum_abs += (abs(lst[x+1][y]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))
            else:
                sum_abs += (abs(lst[x][y+1]-lst[x][y]) + abs(lst[x+1][y]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))
        elif y-1 < 0:
            if x-1 < 0:
                pass
            elif x+1 > 4:
                sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x][y+1]-lst[x][y]))
            else:
                sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x][y+1]-lst[x][y]) + abs(lst[x+1][y]-lst[x][y]))
        elif x+1 > 4:
            if y-1 < 0:
                pass
            elif y + 1 > 4:
                sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))
            else:
                sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x][y+1]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))
        elif y+1 > 4:
            if x-1 < 0:
                pass
            elif x+1 > 4:
                pass
            else:
                sum_abs += (abs(lst[x-1][y]-lst[x][y]) + abs(lst[x+1][y]-lst[x][y]) + abs(lst[x][y-1]-lst[x][y]))

print(sum_abs)

