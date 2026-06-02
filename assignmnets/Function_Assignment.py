def get_account_no() -> int:
    return int(input("Enter account no : "))


def get_amount() -> int:
    return int(input("Please enter amount : "))


def update_transaction(account_no, amount, account_transaction) -> None:
    all_trans = account_transaction.get(account_no)
    all_trans.append(amount)


def banking_menu() -> None:
    customer_accounts = {}
    account_transaction = {}

    while True:
        print("""
              1. Create a new account
              2. Check account balance
              3. Deposit money	
              4. Withdraw money		
              5. Transfer funds		
              6. View transaction history
              7. Exit the application """)

        choice = int(input("Please select your choice :"))

        if choice == 1:
            account_no = get_account_no()
            name = input("Enter person name : ")
            initial_amount = get_amount()
            customer_accounts[account_no] = initial_amount
            account_transaction[account_no] = [initial_amount]
            print("Account created successfully")

        elif choice == 2:
            account_no = get_account_no()
            print("Current balance : ", customer_accounts.get(account_no))

        elif choice == 3:
            account_no = get_account_no()
            amount = get_amount()
            if customer_accounts.get(account_no) is not None:
                customer_accounts[account_no] = customer_accounts.get(account_no) + amount
                update_transaction(account_no, amount, account_transaction)
                print("updated balance : ", customer_accounts.get(account_no))
            else:
                print("Invalid account no")

        elif choice == 4:
            account_no = get_account_no()
            amount = get_amount()
            customer_accounts[account_no] = customer_accounts.get(account_no) - amount
            update_transaction(account_no, amount, account_transaction)
            print("Withdrawal successfully, balance amount : ", customer_accounts.get(account_no))

        elif choice == 5:
            account_no1 = get_account_no()
            account_no2 = int(input("please enter account no to transfer fund: "))
            amount = get_amount()
            if customer_accounts.get(account_no1) is not None and customer_accounts.get(account_no2) is not None:
                customer_accounts[account_no1] = customer_accounts.get(account_no1) - amount
                customer_accounts[account_no2] = customer_accounts.get(account_no2) + amount
                update_transaction(account_no, amount, account_transaction)
                print("updated balance for account {} is {}".format(account_no2, customer_accounts.get(account_no2)))
            else:
                print("account numbers are invalid")

        elif choice == 6:
            account_no = get_account_no()
            transactions = account_transaction[account_no]
            print("All Transactions details : ", transactions)

        elif choice == 7:
            print("exit")
            break

        else:
            print("Please select valid choice !")


if __name__ == '__main__':
    banking_menu()
