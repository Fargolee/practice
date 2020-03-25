cars = ['bwm', 'audi', 'toyota', 'subaru']
# 1.永久性排序，按字母顺序
# cars.sort()
# print(cars)

# # ['audi', 'bwm', 'subaru', 'toyota']

# # 2.按字母反顺序排列
# cars.sort(reverse=True)
# print(cars)

# ['toyota', 'subaru', 'bwm', 'audi']


# print('Here is the original list:')
# # 1、按原始顺序打印列表
# print(cars)
# print('\nHere is the sorted list:')
# # 2、按字母顺序显示列表
# print(sorted(cars))
# # 3、核实，并不会永久性排列
# print('\nHere is the original list again:')
# print(cars)

# Here is the original list:
# ['bwm', 'audi', 'toyota', 'subaru']

# Here is the sorted list:
# ['audi', 'bwm', 'subaru', 'toyota']

# Here is the original list again:
# ['bwm', 'audi', 'toyota', 'subaru']


# 4.reverse()反转列表元素的排列顺序，永久性，可再次调用来恢复原来
cars.reverse()
print(cars)

cars.reverse()
print(cars)

# ['subaru', 'toyota', 'audi', 'bwm']
# ['bwm', 'audi', 'toyota', 'subaru']
