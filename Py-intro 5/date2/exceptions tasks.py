""" # Exercise 1
- Write a program that prompts the user for a number. The number should 
divide the number 1. Handle the ZeroDivisionError exception and print an 
error message.
- The program will keep prompting the user to enter a number until a 
non-zero number is entered.
Hint:
- use a while loop
- research on the keyword: *break* """

print()
print('---Task1---')
print()
while True:
    try:
        number = int(input("Enter number plz: "))
        result = (1 / number)
    except ZeroDivisionError:
        print("Error Cannot use ZERO")
    else:
        print("Result: ", result)
        break


print()
print('---Task2---')
print()


""" ## Exercise 2
- Write a program that prompts the user to enter two numbers and performs 
division.
- Handle the ValueError exception if the user inputs a non-numeric value.
Note: The program will keep prompting the user to enter two numbers 
until a non-zero numeric value is entered as the second number.
 """

while True:
    try:
        number1 = int(input("Enter number plz: "))
        number2 = int(input("Enter number plz: "))
    except ValueError:
        print("Error Use Numbers plz")
    else:
        print(number1 / number2)
        break


print()
print('---Task3---')
print()

""" ## Exercise 3:
- Write a program that prompts the user to enter a list of integers 
and computes the average.
- Handle the ValueError exception if the user inputs a non-numeric value.
Note: The program assumes that the user enters a comma-separated list 
of integers. If the user enters a list with a different separator, the 
program will not be able to parse the input and may raise other exceptions. """

while True:
    try:
        numbers = (input("Enter number list separated by , "))
        num_list = numbers.split(",")
        int_list = []
        for i in num_list:
            int_list.append(int(i))
        average = sum(int_list)/len(int_list)
        print(average) 
        break
    except SyntaxError:
        print("nah")
    except ValueError:
        print("ValueError")



print()
print('---Task4---')
print()

""" ## Exercise 4:
Create a Python function that receives three parameters: a date 
(datetime object), number of days (integers), timezone (string).
The function should add the number of days to the date, 
considering the timezone passed as an argument. If the timezone 
is not valid, the function should raise an exception.
(edited) """

from datetime import datetime
""" 
while True:
    try:
        date = (input("Enter date format YYYY,MM,DD"))
        date_format = datetime.strptime(date,%Y,%m,%d)
        print(date_format) """