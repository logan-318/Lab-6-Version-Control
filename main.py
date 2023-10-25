# Logan Black

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


# FIXME: finish decode function
def decode():
    pass


def main():

    while True:
        # Prompt the user to encode or decode a password
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")

        option = input("Please enter an option: ")
        if option == "1":
            encoded_password = encode()

        # FIXME
        elif option == "2":
            decode()

        elif option == "3":
            break
        else:
            print("Invalid option!\n")


if __name__ == "__main__":
    main()
