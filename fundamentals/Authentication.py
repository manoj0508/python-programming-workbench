
def main ()-> None:
 username = "admin"
 password = "pass"

 uname = str(input("Enter user name = "))
 sec = str(input("Enter pass :"))

 if uname == username and sec == password:
    print("user name is correct")
    print("use login sucessfully")
 else:
     print("user cred is invalid")


if __name__ == "__main__":
    main()