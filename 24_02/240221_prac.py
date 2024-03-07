'''
2 5 3 6 4
'''
# 최대힙
def enq(n):
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 > 자식
    p = c//2        # 부모번호 계산
    while p >= 1 and h[p] < h[c]:     # 부모가 있는데, 더 작으면
        h[p], h[c] = h[c], h[p]     # 교환
        c = p
        p = c // 2

# 힙 삭제
def deq():
    global last
    tmp = h[1]      # 루트의 키값 보관
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p * 2
    while c <= last:    # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]:       # 오른쪽 자식이 있고 더 크면
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp            

N = 10              # 필요한 노드 수
h = [0] * (N+1)     # 최대 힙
last = 0            # 힙의 마지막 노드 번호

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)
print(h)
while(last>0):
    print(deq())
