import string

def check_password_strength(password: str, min_length: int = 8, min_classes: int = 4) -> int:
    """Returns a score indicating the strength of the password.
    A higher score means the password is stronger.
    """
    score = 0
    classes_present = 0

    # Check if the password contains at least one character from each required character class
    if any(c.isupper() for c in password):
        score += 1
        classes_present += 1
    if any(c.islower() for c in password):
        score += 1
        classes_present += 1
    if any(c.isdigit() for c in password):
        score += 1
        classes_present += 1
    if any(c in string.punctuation for c in password):
        score += 1
        classes_present += 1

    # Check if the password meets minimum classes requirement
    if classes_present < min_classes:
        return score

    # Check if the password is long enough
    for length_threshold in [12, 16, 20]:
        if len(password) >= length_threshold:
            score += 1

    return score

def check_password(password: str, common_passwords: set, min_length: int = 8, min_classes: int = 4) -> None:
    """Checks the password for various issues and prints a message indicating its strength."""
    # Check if the password is too common
    if password in common_passwords:
        print("Password is too common. Your password strength is 0.")
        return

    # Check the password strength
    score = check_password_strength(password, min_length, min_classes)
    if score == 0:
        print("Password is too weak.")
        print(f"Password must be at least {min_length} characters long and contain at least {min_classes} of the following: uppercase letter, lowercase letter, digit, special character")
    elif score <= 2:
        print("Password is weak or average.")
        print(f"Password must be at least {min_length} characters long and contain at least {min_classes} of the following: uppercase letter, lowercase letter, digit, special character")
    elif score <= 3:
        print("Password is moderately strong.")
    else:
        print("Password is strong.")

if __name__ == "__main__":
    # Read the list of common passwords from the file
    with open("common.txt", "r") as f:
        common_passwords = set(f.read().splitlines())

    while True:
        password = input("Enter password: ")
        check_password(password, common_passwords)
