def main() -> None:
    accounts = (121,232,343,501,62,456,34,234,583,1000,221);

    account_balance = {
        121  : 5000.00,
        232  : 12000.00,
        343  : 800.00,
        501  : 25000.00,
        62   : 3500.00,
        456  : 9000.00,
        34   : 1500.00,
        234  : 7000.00,
        583  : 4200.00,
        1000 : 50000.00,
        221  : 6800.00
    }

    operation = True
    while operation:
        accountNo = int(input("Enter account no : "))
        if accountNo in accounts:
            amount = int(input("please enter withdraw amount : "))
            balance =account_balance.get(accountNo)

            if 0 < amount <= balance:
                    print("Cash Withdraw successfully !")
                    balance -=amount;
                    account_balance[accountNo] = balance
                    print("Account Balance : ", balance)
            else:
                    print("Invalid/Insufficient fund, current Balance : ", balance)

        else:
            print("Invalid account no or account does not exist")
        choice = str(input("Do you want to continue? (y/n) : "))
        operation = choice.lower()=='y'

    print("user operation ended, Thank you !!!")


if __name__ == "__main__":
    main()