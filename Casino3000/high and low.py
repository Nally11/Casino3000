import random

def high_or_low():
    number = random.randint(1, 10)
    tokens = 0
    
    print("Welcome to the High or Low game!")
    print("Select a number between 1 and 10.")
    
    while True:
        guess = int(input("Take a guess: "))
        tokens += 1
        
        if guess < number:
            print("Unlucky")
            return
        elif guess > number:
            print("Unlucky")
            return
        else:
            print("Congratulations! You guessed it right!")
            print("It took you", tokens, "attempts.")
            break

high_or_low()
