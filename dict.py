person = {
    'name': 'Alice', 
    'age': 25
}
# 들여쓰기를 하면 키 밸류를 보기 좀 더 편해짐
# person.clear()
# print(person) #{}

# print(person['name']) # Alice
# print(person.get('name')) # Alice
# print(person.get('country')) # None
# print(person.get('country', '키가 없습니다.')) # 키가 없습니다.

# person.keys()
# print(person.keys()) 
# # dict_keys(['name', 'age'])
# # key의 모임, 반복 가능(리스트처럼 감싸져 있음, 나열 가능)
# for k in person.keys():
#     print(k)

# for key, value in person.items():
#     print(key, value)

# name Alice
# age 25
    
# print(person.pop('age'))
# print(person)
# 25
# {'name': 'Alice'}

# print(person.setdefault('country', 'KOREA'))
# print(person)

# KOREA
# {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

other_person = {'name' : 'Jane', 'gender': 'Female'}
person.update(other_person)
print(person)
# {'name': 'Jane', 'age': 25, 'country': 'KOREA', 'gender': 'Female'}
person.update(age=50)
print(person)
# {'name': 'Jane', 'age': 50, 'country': 'KOREA', 'gender': 'Female'}
person.update(country = 'KOREA')
print(person)