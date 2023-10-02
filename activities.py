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
                        line = int(line)
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
def main():
    numbers()

if __name__ == "__main__":
    main()