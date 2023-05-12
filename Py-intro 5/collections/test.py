'''
l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']


def remove_numbers(l33t):
    list = [word for word in l33t if word.isalpha() == True]
    return list

print(remove_numbers(l33t))'''


'''def sq(my_list):
    result = []
    for x in my_list:
        if x > 0:
            # result = result + [item]
            result.append(x*x)
    return result

my_list = [1, 2, 3, 4, 5]
print(sq(my_list))'''

def square(my_list):
    list = [n for n in my_list if n > 0 == True]
    return list*n
my_list = [1, 2, 3, 4, 5]
print(square(my_list))