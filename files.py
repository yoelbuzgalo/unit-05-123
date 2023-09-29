def print_lines(file_name):
    '''
    This function opens a file based on the path/name passed
    '''
    my_file = open(file_name)
    for line in my_file:
        print(line.strip()) # Prints every line in the file

def word_search(file_name):
    file = open(file_name)
    user_input = input("Enter a word that you want to search: ")
    user_input = user_input.lower()
    for line in file:
        line = line.strip()
        line = line.lower()
        if line == user_input:
            return print("Word found")
    return print("Word not found")

def longest_word(string):
    words = string.split()
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    if longest != '':
        print(longest)

def longest_words(file_name):
    file = open(file_name)
    for line in file:
        line = line.strip()
        longest_word(line)
    file.close()

def print_names(file_name):
    file = open(file_name)
    next(file)
    for line in file:
        line = line.strip()
        line = line.split(",")
        print(line[1], line[0])
    file.close()

def average_grade(file_name, column):
    sum = 0
    count = 0
    with open(file_name) as file:
        header = next(file).split(',') # skip header
        for line in file:
            line = line.strip()
            values = line.split(",")
            sum += float(values[column])
            count += 1
    print(header[column], sum/count)

        

def main():
    average_grade("data/grades_010.csv", 4)

if __name__ == "__main__":
    main()