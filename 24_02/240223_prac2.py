'''
7070^1004 = 6258
6258^1004 = 7070
'''

KEY = 1004
def encode_decode(num):
    return num ^ KEY

print(encode_decode(1000))
print(encode_decode(4))