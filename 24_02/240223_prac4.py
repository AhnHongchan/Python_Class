N, M = map(int, input().split())

x = bin(M)
cnt = 0

for i in range(len(x)-3, -1, -1):
    if M & (1<< i):
        cnt += 1

if cnt == N:
    print('ON')
else:
    print('OFF')

''' 
for i in range(5):
    print(bin(t), t)
    t = t << 1

M = 31
N = 5
def Test():
    tar = M
    for i in range(N):
        if tar &  0x1 == 0:
        return False
        tar = tar >> 1
    return True
print(Test())
'''


