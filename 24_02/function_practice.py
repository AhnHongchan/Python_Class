def greet(name, age):
    print(f'안녕하세요, {name}님 {age}살이시군요.')

# greet('Alice', 25) # 안녕하세요, Alice님 25살이시군요.
    
# greet('bella') 
# TypeError: greet() missing 1 required positional argument: 'age'
    
# greet(30)
# TypeError: greet() missing 1 required positional argument: 'age'
# 30을 적어도 age가 missing이 되었다는 이유는 위치인자기 때문
# 첫 번째 자리는 name의 자리

# greet(30, 'bella') 안녕하세요, 30님 bella살이시군요.
# greet(30, 'bella', 'aaa')
# TypeError: greet() takes 2 positional arguments but 3 were given


numbers = input().split()

print(numbers)

result = list(map(int, numbers))

print(result)

result = list(map(int, input().split()))

print(result)