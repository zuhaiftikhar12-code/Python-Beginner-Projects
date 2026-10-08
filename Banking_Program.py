def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount=float(input("Enter the amount to deposit: "))
    if amount>=0:
        return amount
    else:
        print("This is not a valid amount")
        return 0
def withdraw(balance):
        amount=float(input("Enter the amount to withdraw: "))
        if amount>balance:
            print("Insufficient amount")
            return 0
        elif amount<0:
            print("Amount must be greater then 0")
            return 0
        else:
            print("withdraw done")
            return amount

def main():
    is_running=True
    balance=0
    while is_running:
        print("**********************")
        print("    Banking Program   ")
        print("**********************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**********************")
        choice=input("Enter your choice(1-4): ")
        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance+=deposit()
            print("Deposit done!")
        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4':
            is_running=False
        else:
            print("**********************")
            print("   invalid choice     ")
            print("**********************")
    print("*****************************")
    print("Thank You! Have a nice day 👋")
    print("*****************************")
if __name__=='__main__':
    main()