def add_numbers(x, y):
    add = x + y
    return print("Sum of", x, "and", y, "is:", add)

x = input("Please input a number: ")
y = input("Please input another number: ")

try:
    add_numbers(int(x), int(y))
except ValueError:
    print("Please insert a number for both values next time!")
