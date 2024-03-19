# 연습문제 2
# {1,2,3,4,5,6,7,8,9,10}의 부분집합 중 원소의 합이 10인 부분집합을 모두 출력하시오.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = []
def dfs(start, sum_v):
    if sum_v == 10:
        print(*path)
        return
    elif sum_v > 10:
        return
    for i in range(start, len(arr)):
        if arr[i] not in path:
            path.append(arr[i])
            sum_v += arr[i]
            dfs(i+1, sum_v)
        else:
            continue
        a = path.pop()
        sum_v -= a

dfs(0, 0)