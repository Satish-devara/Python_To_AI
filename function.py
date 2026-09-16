def combine(a, b):
    print(a+b)


combine(5,6)


numbers = [1, 2, 3, 4, 5]

squares = [n*n for n in numbers]

even = [n for n in numbers if n%2 == 0]

dicti = {
    n: n*n
    for n in numbers
}

print(numbers)
print(squares)
print(even)
print(dicti)
