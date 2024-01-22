my_list = [1,2,3]

# append
# my_list.append(4)
# my_list.append([10, 9, 8])
# print(my_list)
# [1, 2, 3, 4]
# [1, 2, 3, 4, [10, 9, 8]]
# if print(my_list.append([10, 9, 8])):
    # None, 메서드가 원본을 바꾸는 결과를 내는가 여부로

# my_list.extend([4, 5, 6])
# print(my_list)
# [1, 2, 3, 4, 4, 5, 6]

# my_list.insert(3, 'ssafy')
# print(my_list)
# [1, 2, 3, 'ssafy']

# my_list.remove(2)
# print(my_list)
# [1, 3, 'ssafy']

my_list.sort(reverse=True)
print(my_list)