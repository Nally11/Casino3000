def even(my_list):
    result = []
    for x in my_list:
        if x > 0:
            # result = result + [item]
            result.append(x*x)
    return result

my_list = [1, 2, 3, 4, 5]
print(even(my_list))