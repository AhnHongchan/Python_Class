T = int(input())
case = list(map(int, input().split()))

n = len(case)

sum = 0

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            sum += case[j]

    if sum == 0:
        print(True)
    else:
        pass
            # print(case[j], end =",")
    # print()
# print()