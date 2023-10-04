import csv

def opener(filename):
    try:
        with open(filename):
            return True
    except FileNotFoundError:
        print("Could not open file: ", filename)
        return False

def names_and_addresses(filename):
    with open(filename) as file:
        header = next(file).strip().split(",")
        for line in file:
            values = line.strip().split(",")
            print("Name:", values[0], "Address:", values[1])

def first_only(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        # skip the header row
        next(csv_reader)
        for record in csv_reader:
            print("Name:", record[0], "Address:", record[1])


def main():
    # file_input = input("Enter filename to open: ")
    # print("File is able to be opened: ", opener("data/"+file_input))
    # names_and_addresses("data/full_grades_010.csv")
    print(first_only("data/full_grades_010.csv"))

if __name__ == "__main__":
    main()