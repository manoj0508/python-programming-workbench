# W A P which takes one number from the user and checks whether it is an even or odd number?, If it even then prints number is
# even number else prints that number is odd number.

def main() -> None:
    number = int(input("please enter a number : "))
    isEven = number % 2 == 0

    if isEven:
        print(number, "is even number")
    else:
        print(number, "number is odd number")


if __name__ == "__main__":
    main()
