'''
반복문을 이용하여 아래와 같잍 출력한다.
    - Loop 1: 0b1 출력 (2진수와 10진수로 출력)
    - Loop 2: 0b10 출력 (2진수와 10진수로 출력)
    - Loop 3: 0b100 출력 (2진수와 10진수로 출력)
    - Loop 4: 0b1000 출력 (2진수와 10진수로 출력)
    - Loop 5: 0b10000 출력 (2진수와 10진수로 출력)
'''

t = 1
for i in range(5):
    print(bin(t), t)
    t = t << 1