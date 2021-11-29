"""
Add password check program
"""
MIN_LENGTH = 10


# Start of version1
def version1():
    password = input(f"Enter a valid password with at least {MIN_LENGTH} characters: ")
    while len(password) < MIN_LENGTH:
        print(f"Password does not meet the length requirement {len(password)}/{MIN_LENGTH} characters")
        password = input("Re-enter new password: ")
    print(len(password) * "*")


def main():
    """Get password and print asterisks."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks in place of all characters."""
    print(len(password) * "*")


def get_password(MIN_LENGTH):
    """Get and validate the password to fit the requirements."""
    password = input(f"Enter a valid password with at least {MIN_LENGTH} characters: ")
    while len(password) < MIN_LENGTH:
        print(f"Password does not meet the length requirement {len(password)}/{MIN_LENGTH} characters")
        password = input("Re-enter new password: ")
    return password


if __name__ == '__main__':
    main()
