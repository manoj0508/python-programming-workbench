# W. A P. to implement calculator but the operation to be done and two numbers will be taken as input from user:-
# Operation console should show below:-
#     Please select any one operation from below:-
#         * To add enter 1
#         * to subtract enter 2
#         * To multiply enter 3
#         * To divide enter 4
#         * To divide and find quotient enter 5
#         * To divide and find remainder enter 6
#         * To divide and find num1 to the power of num2 enter 7
#         * To Come out of the program enter 8


def main() -> None:
    print("""Please select any one operation from below:-
             * To add enter 1
             * to subtract enter 2
             * To multiply enter 3
             * To divide enter 4
             * To divide and find quotient enter 5
             * To divide and find remainder enter 6
             * To divide and find num1 to the power of num2 enter 7
             * To Come out of the program enter 8""")
    choice = int(input("please select "))

    num1 = int(input("enter first no : "))
    num2 = int(input("enter second no : "))

    if choice == 1:
        result = num1 + num2
        print("addition : ", result)
    elif choice == 2:
        result = num1 - num2
        print("substraction : ", result)
    elif choice == 3:
        result = num1 * num2
        print("multiplication : ", result)
    elif choice == 4:
        result = num1 / num2
        print("division : ", result)
    elif choice == 5:
        result = num1 / num2
        print("result : ", result)
    elif choice == 6:
        result = num1 % num2
        print("divisions remainder : ", result)
    elif choice == 7:
        result = num1 / num2
        power = num1 ** num2
        print("division result : ", result)
        print("num1 to the power num2 : ", power)
    else:
        exit(1);


if __name__ == "__main__":
    main()
