import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase  # default: lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    # If no options selected
    if not characters:
        print("Error: Please select at least one character type.")
        return None

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# Main program
def main():
    print("=== Password Generator ===")

    while True:
        length = int(input("Enter password length: "))

        use_uppercase = input("Include uppercase? (yes/no): ").lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)

        if password:
            print("Generated Password:", password)

        again = input("Generate another password? (yes/no): ").lower()
        if again != "yes":
            break


# Run the program
if __name__ == "__main__":
    main()