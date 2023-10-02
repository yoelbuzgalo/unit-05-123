def numbers():
    total = 0
    while True:
        file_name_input = input("Enter a file name: ")
        if file_name_input != '':
            try:
                with open(file_name_input) as file:
                    sum = 0
                    for line in file:
                        line = line.strip()
                        try:
                            line = int(line)
                        except:
                            print("Error trying to cast", line, "... skipping")
                            continue
                        sum += line
                    print("sum of numbers:", sum)
                    total += sum
            except FileNotFoundError:
                print("File could not be found or open")
            except ValueError:
                print("File format mismatch for this loop program")
        else:
            break
    print("Total =", total)

def division():
    numerator_input = input("Enter a numerator value: ")
    denominator_input = input("Enter a denominator value: ")
    attempts = 3
    while numerator_input != "" and denominator_input != "":
        try:
            value = float(numerator_input)/float(denominator_input)
        except ValueError as ve:
            attempts -= 1
            if attempts <= 0:
                raise ve
            print("There was an error with casting either of the values to float value")
            break
        except ZeroDivisionError as zde:
            attempts -= 1
            if attempts <= 0:
                raise zde
            print("Your denominator cannot be 0")
            break
        print("Result:", value)
        numerator_input = input("Enter a numerator value: ")
        denominator_input = input("Enter a denominator value: ")

def password():
    user_password = input("Enter password: ")
    if len(user_password) >= 10 and len(user_password) <= 20:
        user_password_2 = input("Please confirm your password again: ")
        if user_password == user_password_2:
            return user_password
        else:
            raise ValueError("Your confirmed passwords don't match")
    else:
        raise ValueError("Password needs to be between 10 and 20 characters long")

def main():
    division()

if __name__ == "__main__":
    main()