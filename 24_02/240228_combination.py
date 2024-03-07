'''
N = 3
path = []

def func(lev, start):
    if lev == N:
        print(path, end= ' ')
        return
    
    for i in range(start, 7):
        path.append(i)
        func(lev+1, i)
        path.pop()

func(0, 1)

[1, 1, 1] [1, 1, 2] [1, 1, 3] [1, 1, 4] [1, 1, 5] [1, 1, 6] 
[1, 2, 2] [1, 2, 3] [1, 2, 4] [1, 2, 5] [1, 2, 6] [1, 3, 3] 
[1, 3, 4] [1, 3, 5] [1, 3, 6] [1, 4, 4] [1, 4, 5] [1, 4, 6]
[1, 5, 5] [1, 5, 6] [1, 6, 6] [2, 2, 2] [2, 2, 3] [2, 2, 4] 
[2, 2, 5] [2, 2, 6] [2, 3, 3] [2, 3, 4] [2, 3, 5] [2, 3, 6] 
[2, 4, 4] [2, 4, 5] [2, 4, 6] [2, 5, 5] [2, 5, 6] [2, 6, 6] 
[3, 3, 3] [3, 3, 4] [3, 3, 5] [3, 3, 6] [3, 4, 4] [3, 4, 5] 
[3, 4, 6] [3, 5, 5] [3, 5, 6] [3, 6, 6] [4, 4, 4] [4, 4, 5] 
[4, 4, 6] [4, 5, 5] [4, 5, 6] [4, 6, 6] [5, 5, 5] [5, 5, 6] 
[5, 6, 6] [6, 6, 6]
'''
'''
coin_list = [500, 100, 50, 10]
tar = 1730

cnt = 0
for coin in coin_list:
    possible_cnt = tar // coin

    cnt += possible_cnt
    tar -= coin * possible_cnt

print(cnt)
'''
'''
person = [10, 15, 30, 50]
n = len(person)
sum_v = 0
left_person = n-1

for turn in range(n):
    time = person[turn]
    sum_v += left_person * time
    left_person -= 1
print(sum_v)
'''

'''
n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]

things.sort(key = lambda x:(x[1]/x[0]), reverse = True)
# 큰 것부터 앞으로 나오게 하기 위해

sum = 0
for kg, price in things:
    per_price = price / kg
    if target < kg:
        sum += target * per_price
        break
    
    sum += price
    target -= kg

print(int(sum))
'''