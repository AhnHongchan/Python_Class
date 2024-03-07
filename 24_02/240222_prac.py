'''
내 코드
N = int(input())
lst = [[0] * 7 for _ in range(2)]

for i in range(4):
    lst[0][i] = N + i
    lst[1][6-i] = N - i

print(lst)
'''

N = int(input())

lst = [[0] * 7 for _ in range(2)]

t1 = N
for i in range(4):
    lst[0][i] = t1
    t1 += 1

t2 = N
for i in range(6, 2, -1):
    lst[1][i] = t2
    t2 -= 1

print(lst[0])
print(lst[1])