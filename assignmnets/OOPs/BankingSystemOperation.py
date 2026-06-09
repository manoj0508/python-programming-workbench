import random

class BankUser:

    def __init__(self, name, account_no, initialAmount):
        self.name = name
        self.account_no = account_no
        self.balance = initialAmount

    def show_details(self):
        print("User name {}, Account no {} and Balance {}".format(self.name, self.account_no, self.balance))


class BankOperation:
    def __init__(self, account_data):
        self.account_data = account_data

    def open_account(self, bank_user):
        self.account_data[bank_user.account_no] = bank_user

    def withdraw(self, account_no, amount):
        bank_user = self.account_data[account_no]
        new_balance = bank_user.balance - amount
        bank_user.balance = new_balance
        print("Successfully withdraw {} and updated new balance {}".format(amount, new_balance))

    def deposit(self, account_no, amount):
        bank_user = self.account_data[account_no]
        new_balance = bank_user.balance + amount
        bank_user.balance = new_balance
        print("Successfully deposited {} and updated new balance {}".format(amount, new_balance))

    def view_balance(self, account_no):
        bank_user = self.account_data[account_no]
        print("Name {}, account no {} and current balance is {}".format(bank_user.name, bank_user.account_no,
                                                                        bank_user.balance))

def get_account():
    return int(input("Enter your account no : "))


def main() -> None:

    bank = BankOperation({})

    while True:
        print("""
          1. Create new account
          2. Withdraw amount
          3. Deposit amount
          4. View balance
          5. Exit """)
        choice = int(input("Please select from above options: "))

        if choice == 1:
            name = input("Enter your name : ")
            amount = int(input("Enter initial amount "))
            new_account_no = random.randint(111111,999999)
            newUser = BankUser(name, new_account_no, amount)
            newUser.show_details()
            bank.open_account(newUser)
        elif choice == 2:
            account = get_account()
            amount = int(input("Enter amount to withdraw "))
            bank.withdraw(account, amount)
        elif choice == 3:
            account = get_account()
            amount = int(input("Enter amount to deposit "))
            bank.deposit(account, amount)
        elif choice == 4:
            account = get_account()
            bank.view_balance(account)
        elif choice == 5:
            print("Thank for using bank app, Good by !!!")
            break
        else:
            print("Pleas select a valid option")


if __name__ == "__main__":
    main()
