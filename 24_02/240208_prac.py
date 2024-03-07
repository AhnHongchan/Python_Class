'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V):   # 정점 번호 i, 시작 i/ 마지막 V
    visited = [0]*(V+1)     # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1      # 시작점 방문
    print(i)        # 정점에서 할 일
    while True:     # 탐색
        for w in adjl[i]:       # 현재 방문한 정점에 인접하고 방문 안한 정점 w가 있으면
            if visited[w] == 0:
                st.append(i)        # push(i), i를 지나서
                i = w               # w에 방문
                visited[i] = 1      # 방문해서 할 일
                print(i)
                break       # for w 브레이크
        else:       # i에 남은 인접 정점이 없으면
            if st:      # 스택이 비어있지 않으면 (지나온 정점이 남아있으면)
                i = st.pop()
            else:       # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
                break       # 탐색 마무리 / while true 브레이크


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접 리스트
adjl = [[] for _ in range(V+1)]      # adjl[i] 행에 i에 인접한 정점 번호저장
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)         # 방향이 없는 경우
# print(adjl)
dfs(1, V)
