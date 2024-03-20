# 인접 행렬 DFS: 재귀
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

visited = [0] * 5

def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다.

    # 다음 재귀 호출 전
    visited[now] = 1
    print(now, end=' ')

    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인
    for to in range(5):
        if graph[now][to] == 0:
            continue
        
        # 이미 방문했다면 pass
        if visited[to]:
            continue
    # 돌아왔을 때 작업