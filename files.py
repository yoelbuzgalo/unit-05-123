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

def main():
    longest_words("data/alice.txt")

if __name__ == "__main__":
    main()