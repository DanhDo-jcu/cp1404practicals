"""
Add password check program
"""


def main():
    """Start of main"""
    password_length = 10
    password = get_password(password_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks in place of characters"""
    print(len(password) * "*")


def get_password(password_length):
    """Get and validate the password to fit the requirements"""
    password = input("Enter a valid password: ")
    while len(password) < password_length:
        print(f"Password does not meet the length requirement {len(password)}/10 characters")
        password = input("Re-enter new password: ")
    return password


if __name__ == '__main__':
    main()
