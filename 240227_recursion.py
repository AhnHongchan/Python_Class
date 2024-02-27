'''
def BBQ(x):
    x += 10
    print(x)

def KFC(x):
    print(x)
    x += 3
    BBQ(x+2)
    print(x)

x = 3
KFC(x+1)
print(x)

4
19
7
3
'''

'''
def KFC(x):
    KFC(x+1)

KFC(0)
print('끝')

RecursionError: maximum recursion depth exceeded
'''

'''
def KFC(x):
    if x == 2:
        return
    print(x)
    KFC(x+1)
    print(x)

KFC(0)
print('끝')

0
1
1
0
끝
'''
'''
def recur(x):
    if x == 6:
        return
    print(x, end= ' ')
    recur(x+1)
    print(x, end=' ')

recur(0)
print('끝')

0 1 2 3 4 5 5 4 3 2 1 0 끝
'''
'''
def KFC(x):
    if x == 2:
        return
    KFC(x + 1)
    print(x, end= ' ')

KFC(0)

1 0
'''
'''
def KFC(x):
    if x == 2:
        return
    KFC(x+1)
    KFC(x+1)
    print(x)

KFC(0)

1
1
0
'''

'''
def tree(x):
    if x == 3:
        return
    tree(x+1)
    tree(x+1)

tree(0)
'''

'''
path = []

def KFC(x):
    if x == 2:
        print(path)
        return
    for i in range(3):
        path.append(i)
        KFC(x+1)
        path.pop()

KFC(0)

[0, 0]
[0, 1]
[0, 2]
[1, 0]
[1, 1]
[1, 2]
[2, 0]
[2, 1]
[2, 2]
'''

'''
path = []
def call(x):
    if x == 3:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        call(x+1)
        path.pop()

call(0)

[1,1,1] ~ [6,6,6]
'''

'''
path = []
used = [False for _ in range(3)]

def KFC(x):
    if x == 2:
        print(path)
        return
    
    for i in range(3):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False
KFC(0)

[0, 1]
[0, 2]
[1, 0]
[1, 2]
[2, 0]
[2, 1]
'''

'''
N, type = map(int, input().split())
path = []
used = [False for _ in range(6)]

def play(x):
    if x == N:
        print(path)
        return
    
    if type == 1:
        for i in range(1, 7):
            path.append(i)
            play(x+1)
            path.pop()
    else:
        for i in range(1, 7):
            if used[i-1] == True:
                continue
            used[i-1] = True
            path.append(i)
            play(x+1)
            path.pop()
            used[i-1] = False

play(0)
'''
'''
실제로는 모두 탐색하지만 출력만 안 하는 경우

path = []

def kfc(x, sum):
    if x == 3:
        if sum <= 10:
            print(f'{path} = {sum}')
        return
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()

kfc(x = 0, sum = 0)

'''

'''
가지치기 한 경우
path = []
def kfc(x, sum):
    if sum > 10:
        return

    if x == 3:
        print(f'{path} = {sum}')
        return
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()

kfc(x = 0, sum = 0)
'''
# 최종답안: 개수 출력
path = []
cnt = 0
def kfc(x, sum):
    global cnt
    if sum > 10:
        return

    if x == 3:
        # print(f'{path} = {sum}')
        cnt += 1
        return
    
    for i in range(1, 7):
        path.append(i)
        kfc(x + 1, sum + i)
        path.pop()

kfc(x = 0, sum = 0)
print(cnt)