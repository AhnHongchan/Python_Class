# my_set = {'a', 'b', 'c', 1, 2, 3}

# print(my_set)
# case
# {'c', 1, 2, 3, 'a', 'b'}
# {1, 2, 3, 'b', 'c', 'a'}
# 순서가 존재하지 않아 매 출력마다 순서가 달라짐

# my_set.add(4)
# print(my_set)
# {1, 2, 3, 4, 'b', 'a', 'c'}
# {1, 2, 3, 4, 'c', 'a', 'b'}

# my_set.add(4)
# print(my_set)

# 중복이 되지 않는다.
# {1, 2, 3, 'c', 'b', 'a', 4}
# {1, 2, 3, 'b', 4, 'c', 'a'}

# my_set.clear()
# print(my_set) # set()

# my_set.remove(2)
# print(my_set)
# {1, 3, 'a', 4, 'c', 'b'}

# my_set.remove(10)
# print(my_set) # KeyError: 10

# element = my_set.pop()
# print(element)
# c, 1, 1, 1, 1 - 왜 우리가 생각하는 랜덤의 확률이 아닌가

# my_set.update([1,4,5])
# print(my_set)


# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 9}

# print(set1.difference(set2)) # {0, 2, 4}
# print(set1.intersection(set2)) # {1, 3}
# print(set1.issubset(set2)) # False
# print(set1.issuperset(set2)) # False
# print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}

# print(hash(1)) # 1
# print(hash('a'))
# -3133287799518204883
# -4076714354704769889
# 3809319173521601395

