def numbers():
    while True:
        file_name_input = input("Enter a file name: ")
        if file_name_input != '':
            with open(file_name_input) as file:
                sum = 0
                for line in file:
                    line = line.strip()
                    line = int(line)
                    sum += line
                print("sum of numbers:", sum)
        else:
            break

def main():
    numbers()

if __name__ == "__main__":
    main()