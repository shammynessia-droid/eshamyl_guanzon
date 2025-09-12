correct_password = "eshamylgwapa"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("You are logged in.")
        break
    else:
        print("Wrong password. Please try again.")