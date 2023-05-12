'''Write a program that takes a list of numbers and returns a new list containing the squares of each number.
use list comprehension
numbers = [1, 2, 3, 4, 5] ---> [1, 4, 9, 16, 25]'''


def sq(my_list):
    result = []
    for x in my_list:
        if x > 0:
            # result = result + [item]
            result.append(x*x)
    return result

my_list = [1, 2, 3, 4, 5]
print(sq(my_list))

print()
print("-------Compression---------")
print()
my_list = [1, 2, 3, 4, 5]
squares = [*i for i in my_list]
print(my_list)
