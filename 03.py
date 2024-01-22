# a = [1, 2, 3, 4]
# b = a
# b[0] = 100

# print(a) [100, 2, 3, 4]
# print(b) [100, 2, 3, 4]

a = 100
b = a

b = 9
print(a) # 100
print(b) # 9

# 할당
original_list = [1, 2, 3]
copy_list = original_list
copy_list[0] = 'hello'
print(original_list)