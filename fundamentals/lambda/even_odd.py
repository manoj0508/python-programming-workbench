
check_even_odd = lambda x : "even" if x%2==0 else "odd"
check_positive_negative = lambda x: "Positive" if x >0 else "Negative"

check_even = lambda x : x%2 ==0

find_max = lambda num1, num2 : num1 if num1> num2 else num2
find_min = lambda num1, num2 : num1 if num1 < num2 else num2
find_squre = lambda x: x**2

def main() -> None:
    num = int(input("enter number : "))
    even_odd = check_even_odd(num)
    print("number is : ",even_odd)

    number_sign_value = check_positive_negative(num)
    print("enter number is : ",number_sign_value)

    num2 = int(input("enter 2nd number "))

    print("max number :", find_max(num, num2))

    print("min number :", find_min(num, num2))

    num = [2,4,3,8,10]

    print(list(map(find_squre, num)))

    for val in map(lambda x: x**2, num):
        print(val, end = "| ")
    print()
    print(list(filter(check_even,map(find_squre, num))))






if __name__=="__main__":
    main()
