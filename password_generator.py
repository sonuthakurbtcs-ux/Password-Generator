import random
import string

def generate_password():
    print("===== PASSWORD GENERATOR =====")

    # Ask user for password length
    try:
        length = int(input("Enter password length (example: 12): "))
        if length < 4:
            print("Password length must be at least 4 characters!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lower + upper + digits + symbols

    # Guarantee strong password (at least one of each type)
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to remove pattern
    random.shuffle(password)

    # Final password
    final_password = "".join(password)

    print(f"\nGenerated Password: {final_password}")
    print("\n✔ Strong password generated successfully!")


if __name__ == "__main__":
    generate_password()
