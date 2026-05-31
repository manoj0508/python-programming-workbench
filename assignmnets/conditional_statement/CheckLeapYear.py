# W A P to check whether a year entered by user is an leap year or not?
# Check with below input:-
# leap year:- 2012, 1968, 2004, 1200, 1600,2400
# Non-lear year:- 1971, 2006, 1700,1800,1900


def main() -> None:
    year = int(input("please enter you year : "))

    isLeapYear = year % 4 == 0 and year / 100 != 0

    if isLeapYear:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


if __name__ == "__main__":
    main()
