import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    # Base character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters like !@#$%^&*()

    # Combine character sets based on user preference
    characters = letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password = generate_password(length=16, use_digits=True, use_symbols=True)
print("Generated Password:", password)
