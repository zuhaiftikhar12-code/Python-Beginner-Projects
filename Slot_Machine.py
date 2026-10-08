import random
import time as t
def spin_row():
    symbols=['🍒','🍋','🍉','🔔','⭐']
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet * 3
        elif row[0]=='🍋':
            return bet * 4
        elif row[0]=='🍉':
            return bet * 4
        elif row[0]=='🔔':
            return bet * 10
        elif row[0]=='⭐':
            return bet * 20
    return 0
def main():
    balance=100
    print("************************")
    print("Welcome to python slots ")
    print("symbols: 🍒🍋🍉🔔⭐")
    print("************************")
    while balance>0:
        print(f"Current Balance: {balance}")
        bet=input("Enter the bet amount: ")
        if not bet.isdigit():
            print("Enter a valid number")
            continue
        bet=int(bet)
        if bet>balance:
            print("insufficient bet amount")
            continue
        if bet<=0:
            print("bet must be greater then 0")
            continue
        
        balance-=bet
        
        row=spin_row()
        print("Spinning.....")
        t.sleep(1)
        print()
        print_row(row)
        payout=int(get_payout(row,bet))
        if payout>0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost that turn")
        
        balance+=payout
        play_again=input("Do you want to play again(Y/N): ").upper()
        if play_again != "Y":
            break
    print("*****************************************")
    print(f"   Game over! your final balance : {balance}")
    print("*****************************************")
if __name__=="__main__":
    main()