def user_operation(amount,balance) -> None:
    if amount > 0:
        if amount <= balance:
            print("successfully withdraw : ",amount)
            balance -= amount
            print("Balance remaining : ",balance)
        else:
            print("Withdraw amount exceeds balance")
            print("Balance : ",balance)
    else:
        print("Please enter valid amount")


def main ()-> None:
  userBalance = 7000
  operation = True

  while operation:
    amount = int(input("Enter withdraw amount : "))
    user_operation(amount,userBalance)
    choice = input("do you want to continue (y/n) ? ")
    operation = choice.lower() == "y"

  print("User operation ends")



if __name__ == "__main__":
    main()