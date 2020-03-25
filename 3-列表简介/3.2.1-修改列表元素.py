motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 1、修改：利用索引赋值
# motorcycles[0] = 'ducati'
# print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']

# 2、list.append(a) 添加
# motorcycles.append('ducai')
# print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducai']

# 3、list.insert(index,a) 插入
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'honda', 'yamaha', 'suzuki']

# 4、del list[index] 删除元素
# del motorcycles[0]
# print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']

# 5、list.pop()删除元素，并接着使用它的值
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha']
# suzuki

# 6、弹出列表中任何位置的元素
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title())
# print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# The first motorcycle I owned was a Honda
# ['yamaha', 'suzuki']

# 7、list.remove() 根据值删除元素，并可以继续使用值
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive for me.')

# ['honda', 'yamaha', 'suzuki']
# ['honda', 'suzuki']

# A Yamaha is too expensive for me.
