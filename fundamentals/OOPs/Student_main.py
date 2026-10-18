import re

from fundamentals.OOPs.Student import Student


def main()-> None:
    s1 = Student(1, "manoj", 20)
    s1. display()
    print(Student.name)

    replace_data("Spec#1234^&$ABC")
    password_validation()

def replace_data(input_data_value)-> None:
    pattern = "[^A-Za-z0-9]"
    result = re.sub(pattern,'',input_data_value)
    print(result)

def valid_phone_number()-> None:
    input_data = "(123) 456-7896"
    search_pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    if re.search(search_pattern,input_data):
        print("valid")
    else:
        print("invalid")

def password_validation()-> None:
    data = "Manoj@1234"
    pass_rule = r"^[[A-Z]*[a-z]*@[0-9]*]$"
    if re.search(pass_rule,data):
        print("Valid Password")
    else:
        print("invalid Password")


if __name__ == "__main__":
    main()
    valid_phone_number()
