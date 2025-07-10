numbers1 = [7, 7, 3]
numbers2 = [8, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Adition of two lists")
print(list(result))

print()
print()

nums = [1, 2, 3, 4, 5]
def square(n):
    return n*n

mysquare = list(map(square, [1, 2, 3, 4, 5]))
print("Squre of numbers in list")
print(mysquare)