def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    

def fibo_memo(n):
    global cnt
    cnt += 1
    if n !=0 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]


cnt = 0
n = 7
print(fibo(n), cnt)

cnt = 0
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n), cnt)