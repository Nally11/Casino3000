'''Exercise (Vowel Sort):
Write a Python program that sorts a list of strings based on the number of vowels they contain.
The program should take a list of strings as input from the user.
sort the strings by the number of vowels they contain using the sort() method with a custom function
print the sorted list of strings.
'''


def check_vowel(my_strings):
    for word in my_strings:
        word.count('a','e','i','o','u')


print(check_vowel(['hello', 'world',]))


