import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to Password Generator")
    print("_____________________________")

    while True:
        try:
            length = int(input("To generate your password\nEnter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Please enter a positive integer for password length.")
        except ValueError:
            print("Please enter a positive integer for password length.")

    password = generate_password(length)
    print(f"\nThe Password of length ({length}) is generated:")
    print(password)


if __name__ == "__main__":
    main()
