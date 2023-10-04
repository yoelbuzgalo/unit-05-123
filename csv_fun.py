import csv
import re

def opener(filename):
    try:
        with open(filename):
            return True
    except FileNotFoundError:
        print("Could not open file: ", filename)
        return False

def names_and_addresses(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for record in csv_reader:
            print("Name:", record[0], "Address:", record[1])

def zip_check(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for record in csv_reader:
            if re.findall(', [789]\d{4}', record[1]):
                print(record[0])
                
                

def average(filename, column):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        sum = 0
        counter = 0
        for record in csv_reader:
            counter += 1
            sum += float(record[column])
        return sum/counter

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
    # print(first_only("data/full_grades_010.csv"))
    # print(average("data/full_grades_010.csv", 26))
    zip_check("data/full_grades_010.csv")

if __name__ == "__main__":
    main()