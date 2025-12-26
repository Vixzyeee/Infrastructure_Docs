print("=== SIMPLE LOGIN DECISION ===")

username_input = input("Enter username: ")
password_input = input("Enter password: ")

correct_username = "admin"
correct_password = "12345"

if username_input == correct_username and password_input == correct_password:
    print("Login successful")
elif username_input != correct_username and password_input == correct_password:
    print("Username is incorrect")
elif username_input == correct_username and password_input != correct_password:
    print("Password is incorrect")
else:
    print("Both username and password are incorrect")
