# Need to verify the password and perform below rule checks
#  i) Atleast 8 chars
#  ii) Atleast one UpperCase char [A-Z]
#  iii) Atleast one lowercase char [a-z]
#  iv) Any one given speical char are allowed [%$#@]
#
import re


def one_upper_case_match(input) -> bool:
    pattern = r"^(?=.*[A-Z]).*$"
    if re.search(pattern, input):
        return True
    else:
        return False


def one_lower_case_match(input)->bool:
    pattern = r"^(?=.*[a-z]).*$"
    if re.search(pattern, input):
        return True
    else:
        return False

def one_digit_match(input)->bool:
    pattern = r"^(?=.*[0-9]).*$"
    if re.search(pattern, input):
        return True
    else:
        return False

def one_special_char(input)-> bool:
    pattern = r"^(?=.*[%$#@]).*$"
    if re.search(pattern, input):
        return True
    else:
        return False

def input_word_length(input)-> None:
    pattern = r"^.{8,}$"
    if re.search(pattern, input):
        return True
    else:
        return False


def password_validation_regex() -> None:
    input = "Manoj@QW"
    validation_count=0
    if one_upper_case_match(input):
        print("At least one upper case present")
        validation_count +=1
    if one_lower_case_match(input):
        print("At least one lower case present")
        validation_count +=1
    """
      if one_digit_match(input):
        print("At least one digit present")
        validation_count +=1
    """

    if one_special_char(input):
        print("At least one special char is present")
        validation_count +=1
    if input_word_length(input):
        print("password has 8 chars")
        validation_count +=1

    if validation_count == 4:
        print("password is valid")
    else:
        print("password is invalid")




def main():
    password_validation_regex()


if __name__ == "__main__":
    main()
