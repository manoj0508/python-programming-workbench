# W A P which takes two numbers from the user and prints below output:-
#     1. num1 is greater than num2 if num1 is greater than num2
#     2. num1 is smaller than num2 if num1 is smaller than num2
#     3. num1 is equal to num2 if num1 and num2 are equal

# Note:- 1. Do this problem using if - else
#       2. Do this using ternary operator

def main1() -> None:
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))

    if num1 > num2:
        print("num1 is greater than num2")
    elif num2 > num1:
        print("num1 is smaller than num2")
    else:
        print("num1 and num2 are equal")


def main2() -> None:
    print("ternary operator ")
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))

    result = "num1 is greater than num2" if num1 > num2 else "num1 is smaller than num2" \
        if num1 < num2 else "num1 and num2 are equal"
    print(result)


if __name__ == "__main__":
    main1()
    main2()
