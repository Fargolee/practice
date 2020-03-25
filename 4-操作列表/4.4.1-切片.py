list = ['a', 'b', 'c', 'd', 'e']

#  前3
# print(list[0:3])
# ['a', 'b', 'c']
# print(list[1:4])
# ['b', 'c', 'd']
# print(list[2:5])
# ['c', 'd', 'e']

# 后3
# print(list[-3:])
# ['c', 'd', 'e']

# print(list[0:-1])
# ['a', 'b', 'c', 'd']

# print(list[:-1])
# ['a', 'b', 'c', 'd']

# 遍历切片
print('Here are the first three on my team:')
for li in list[:3]:
    print(li)

# Here are the first three on my team:
# a
# b
# c
