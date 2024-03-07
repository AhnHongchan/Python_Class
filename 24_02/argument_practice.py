def func(pos1, pos2, age = 30, *args, **kwargs):
    print(pos1, pos2, age, args, kwargs)

# func(1, 2, 3, 4, 5)
# 1 2 3 (4, 5) {}
    
# func(1, 2, 3, a = 100, b = 200)
# 1 2 3 () {'a': 100, 'b': 200}