dismensions = (200, 50)
# 不可变的列表叫元组，元组内的值不能修改
# dismensions[0] = 250
# print(dismensions[0])
# print(dismensions[1])

print('Original dimensions:')
for dismension in dismensions:
    print(dismension)
dismensions = (400, 100)
print('\nModified dimensions:')
for dismension in dismensions:
    print(dismension)
#     Original dimensions:
# 200
# 50

# Modified dimensions:
# 400
# 100
