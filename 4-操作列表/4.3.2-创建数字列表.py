# numbers = list(range(1, 6))
# print(numbers)
# [1, 2, 3, 4, 5]

# 1~10 的偶数
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)
# [2, 4, 6, 8, 10]

# 前10个整数的平方
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value**2)
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
