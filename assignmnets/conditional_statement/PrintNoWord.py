# W. A P. which takes one number from 0 to 9 from the user and prints it in the word. And if the word is not from 0 to 9 then
# it should print that number is outside of the range and program should exit.
# For exapmple:-
# input = 1
# output = one

def main() -> None:
    number = int(input("Please enter single digit no : "))
    if number == 1:
        print("one")
    elif number == 2:
        print("two")
    elif number == 3:
        print("three")
    elif number == 4:
        print("four")
    elif number == 5:
        print("five")
    elif number == 6:
        print("six")
    elif number == 7:
        print("seven")
    elif number == 8:
        print("eight")
    elif number == 9:
        print("nine")
    elif number == 0:
        print("zero")
    else:
        print("number is outside of the range")


if __name__ == "__main__":
    main()
