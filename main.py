# Piper
def decode(password=''):
    new_password = ""
    try:
        for digit in password:
	    # Logan - fixed issue where new_digit would be < 0
            new_digit = int(digit) - 3
            if new_digit < 0:
                new_digit += 10
            new_password += str(new_digit)
        print(f'The encoded password is {password}, and the original password is {new_password}\n')
    except ValueError:
        print("Invalid password!")


# Logan B
def encode():
    new_password = ""
    try:
        # Make sure user inputs an 8-digit integer
        password = str(int(input("Please enter your password to encode: ")))
        if len(password) != 8:
            raise ValueError

        for digit in password:
            # Add each digit by 3
            # If new digit value >= 10, subtract 10
            new_digit = int(digit) + 3
            if new_digit >= 10:
                new_digit -= 10
            new_password += str(new_digit)

        print("Your password has been encoded and stored!\n")
        return new_password

    except ValueError:
        print("Invalid password!\n")


def main():

    while True:
        # Prompt the user to encode or decode a password
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")

        option = input("Please enter an option: ")
        if option == "1":
            encoded_password = encode()
        elif option == "2":
            try:
                decode(encoded_password)
            except UnboundLocalError:
                print("Please encode a password first!\n")
        elif option == "3":
            break
        else:
            print("Invalid option!\n")


if __name__ == "__main__":
    main()
