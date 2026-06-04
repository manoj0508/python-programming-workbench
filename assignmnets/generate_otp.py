import random
import string


def generate_otp() -> None:
    otp_type = input("please provide otp type Numeric/Alphanumeric : ").strip().lower()
    otp_l = int(input("Please provide OTP length 4/6/8/12 : ").strip())

    valid_lengths = [4, 6, 8, 12]
    valid_types = ["numeric", "alphanumeric"]

    OTP_again = 'y'

    while OTP_again == 'y':
        if otp_type not in valid_types:
            print("Invalid OTP type. Choose Numeric or Alphanumeric.")
        elif otp_type == "numeric":
            if otp_l not in valid_lengths:
                print("Invalid OTP length. Choose from 4, 6, 8, 12.")
            else:
                num = random.randint(10 ** (otp_l - 1), 10 ** otp_l - 1)
                print(num)
        else:
            if otp_l not in valid_lengths:
                print("Invalid OTP length. Choose from 4, 6, 8, 12.")
            else:
                characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
                num = ''.join(random.choices(characters, k=otp_l))
                print(num)

        OTP_again = input("do you want to generate another OTP y/n : ").strip().lower()


if __name__ == "__main__":
    generate_otp()
