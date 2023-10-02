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
    while numerator_input != "" and denominator_input != "":
        try:
            value = float(numerator_input)/float(denominator_input)
        except ValueError:
            print("There was an error with casting either of the values to float value")
            break
        except ZeroDivisionError:
            print("Your denominator cannot be 0")
            break
        print("Result:", value)
        numerator_input = input("Enter a numerator value: ")
        denominator_input = input("Enter a denominator value: ")

def main():
    division()

if __name__ == "__main__":
    main()