import random

options=("rock","paper","scissors")
is_running=True

while is_running:
    player=None
    computer=random.choice(options)
    
    player=input("Enter a choice (rock,paper,scissors): ")
    while player not in options:
        player=input("Enter a choice (rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("Its a Tie! ")
    elif player=="rock" and computer=="scissors":
        print("You Win 🎉🎉🎉")
    elif player=="paper" and computer=="rock":
        print("You Win 🎉🎉🎉")
    elif player=="scissors" and computer=="paper":
        print("You Win 🎉🎉🎉")
    else:
        print("You Lose 😞😒")
        
    play_again=input("play again (y/n): ").lower()
    if play_again=="n":
        is_running=False
            
print("Thanks for playing❤️")