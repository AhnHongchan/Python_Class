# 이진 검색
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()
print(arr)
# 2. 이진 검색 - 반복문 버전
def binarySearch(low, high, target):
    if low > high:
        return -1
    
    mid = (low+high) // 2
    if target == arr[mid]:
        return mid
    
    if target < arr[mid]:
        return binarySearch(low, mid-1, target)
    else:
        return binarySearch(mid + 1, high, target)


print(f'21 = {binarySearch(0, len(arr)-1, 21)}')
print(f'324 = {binarySearch(0, len(arr)-1, 324)}')
print(f'888 = {binarySearch(0, len(arr)-1, 888)}')