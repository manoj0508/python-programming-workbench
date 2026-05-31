# W A P which takes three numbers from the user and prints below output:-
#     1. num1 is greater than num2 and num3 if num1 is greater than num2 and num3
#     2. num2 is greater than num1 and num3 if num2 is greater than num1 and num3
#     3. num3 is greater than num1 and num2 if num3 is greater than num1 and num2

# Note:- 1. Do this problem using if - elif - else
#       2. Do this using ternary operator

def main1() -> None :
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    num3 = int(input("enter third number : "))

    if num1 > num2 > num3 :
        print("num1 is greater than num2 and num3")
    elif num2 > num1 > num3 :
        print("num2 is greater than num1 and num3")
    else :
        print("num3 is greater than num1 and num2")



def main2()-> None :
    num1 = int(input("enter first number : "))
    num2 = int(input("enter second number : "))
    num3 = int(input("enter third number : "))

    result = "num1 is greater than num2 and num3" if num1 > num2 > num3 \
        else "num2 is greater than num1 and num3" if num2 > num3 > num1 \
        else "num3 is greater than num1 and num2"

    print(result)

if __name__== "__main__":
    main1()
    main2()