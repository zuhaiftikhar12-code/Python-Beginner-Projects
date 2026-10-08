import random

lowest_no=1
highest_no=100

answer=random.randint(lowest_no,highest_no)

guesses=0
is_running=True

print("----- Number Guessing Game -----")

print(f" Select a number between  {lowest_no} and {highest_no}")

while is_running:
    
    guess=input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if(guess<lowest_no or guess>highest_no):
            print("The number is out of range")
            print(f"Please select a number between  {lowest_no} and {highest_no}")
        elif guess>answer:
            print("Too High! Try again")
        elif guess<answer:
            print("Too Low! Try again")
        else:
            print(f"Correct!😍🎉👌 The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running=False
    else:
        print("invalud guess")
        print(f"Please select a number between  {lowest_no} and {highest_no}")
        
    