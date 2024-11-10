import random
import string

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    # Create a pool of characters based on user selections
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Ensure the pool is not empty
    if not char_pool:
        raise ValueError("At least one character type should be selected")

    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# User input for password parameters
try:
    length = int(input("Enter password length (minimum 6): "))
    if length < 4:
        raise ValueError("Password length should be at least 4")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and print the password
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print(f"Generated Password: {password}")

except ValueError as e:
    print(f"Error: {e}")
