'''
arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def print_name():
    print('{', end = '')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')

def run(lev):
    if lev == 3:
        print_name()
        return
    
    for i in range(2):
        path.append(arr[i])
        run(lev+1)
        path.pop()

run(0)

{MIN CO TIM }
{MIN CO }
{MIN TIM }
{MIN }
{CO TIM }
{CO }
{TIM }
{}
'''

'''
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1       # 오른쪽으로 한 칸씩 민다.

for tar in range(1<<n):
    print('{', end='')
    get_sub(tar)
    print('}')

{}
{A}
{B}
{AB}
{C}
{AC}
{BC}
{ABC}
'''

'''
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        # 1비트 1인지 확인
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(1<<n):
    if get_count(tar) >= 2:
        result += 1
print(result)
'''
'''
조합
arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3
def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()

run(lev = 0, start = 0)
'''