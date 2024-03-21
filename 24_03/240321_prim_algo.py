'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 우선순위큐를 활용
from heapq import heappush, heappop

def prim(start):
    pq = []
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # 기존 BFS는 노드 번호만 관리
    # PRIM 가중치가 낮으면 먼저 나와야 한다.
    # 관리해야할 데이터: 가중치 노드 번호 2가지
    # 동시에 두 가지 데이터 다루기
    # 1. class로 만들기: 3가지 이상의 변수를 관리해야할 시
    # 2. 튜플로 관리
    # 이차원 배열 + 가중치 + 높이
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # 방문했다면 continue
        if MST[now]:
            continue
        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없다면 pass
            if graph[now][to] == 0:
                continue
            # 이미 방문했다면
            if MST[to]:
                continue
            
            heappush(pq, (graph[now][to], to))

    print(f'최소 비용:{sum_weight}')


V, E = map(int, input().split())
# 인접 행렬로 저장
# [실습] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w

# [기존] 3 -> 4로 갈 수 있다.
# graph[3][4] = 1

# [가중치 그래프] 3->4로 가는 데 31이라는 비용이 든다.
# graph[3][4] = 34