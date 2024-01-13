import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        length = int(input("Enter the desired length of the password (default is 12): ") or 12)
        password_generator = PasswordGenerator(length)
        password = password_generator.generate_password()

        print(f'Generated Password: {password}')

        ask_again = input("Do you want to generate another password? (yes/no): ").lower()
        if ask_again != 'yes':
            print("Exiting the Password Generator. Goodbye!")
            break

if __name__ == '__main__':
    main()
