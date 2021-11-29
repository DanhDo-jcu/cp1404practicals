"""
Add password check program
"""
password_length = 10
password = input("Enter a valid password: ")
while len(password) < password_length:
    print(f"Password does not meet the length requirement {len(password)}/10 characters")
    password = input("Re-enter new password: ")
print(len(password) * "*")
