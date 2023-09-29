def print_lines(file_name):
    '''
    This function opens a file based on the path/name passed
    '''
    my_file = open(file_name)
    for line in my_file:
        print(line.strip()) # Prints every line in the file

def main():
    print_lines("data/alice.txt")

if __name__ == "__main__":
    main()