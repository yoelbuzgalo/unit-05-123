def terminate():
    '''
    This function will return True upon user input of 'y' otherwise False.
    '''
    exit_input = input("Are you sure you want to quit? (y/n): ")
    if exit_input.lower() == 'y':
        return True
    return False

def student_lab_average(grades):
    '''
    This function calculates a student's lab average grades based on the data passed
    '''
    total = 0 # Starts with 0
    lab_grades = 8 # Defaulted to 8 lab grades, so no matter how many data is passed but must be all 8 grades for average. (Note typo in instruction as there is only 8 labs in .csv file) 
    for grade in grades:
        if grade == '':
            continue # Skips on empty strings of an expected lab grade (if it doesnt exist)
        total += float(grade) # Add to total for every grade received
    return (total/lab_grades) # Calculates the average based on default 10 classes, so even if it was missing 1 or more classes, it would count them as 0

def main():
    '''
    Main entry of this program
    '''
    while True:
        user_input = input("Enter a filename or 'quit' to quit: ")
        if user_input == 'quit':
            if terminate(): # Calls the terminate function to double check if the user is sure, upon True itll break the loop
                break # Terminates the loop
            continue # Goes back to initial loop
        elif user_input == '':
            continue # Goes back to initial loop
        else:
            try:
                with open(user_input) as file:

                    header = next(file).strip().split(",") # Gets the header of the file, and strips all the whitespace + splits with comma
                    print("Lab Averages from:", user_input)
                    print("-----------------------------------------------------------")
                    print("Student","Lab Average",sep="                                         ")
                    print("-----------------------------------------------------------")

                    # Initialize variables for calculating after iterating every line of grades
                    class_sum = 0
                    class_min = 100
                    class_max = 0
                    student_counter = 0

                    for line in file:
                        line = line.strip().split(",") # Strips and splits every line after the header

                        # Get data associated
                        student_lastname = line[0] # Gets the student's last name
                        student_firstname = line[1] # Gets the student's first name
                        student_grades = line[2:10] # Gets the student's lab grades
                        student_average = student_lab_average(student_grades) # Gets the student's average grade

                        # Adds data to for class average, minimum and max
                        # Updates the class maximum if student average is higher than latest class maximum (starts with 0 by default)
                        if student_average > class_max:
                            class_max = student_average
                        
                        # Updates the class minimum if student average is lower than latest class minimum (starts with 100 by default)
                        if student_average < class_min:
                            class_min = student_average

                        class_sum += student_average
                        student_counter += 1

                        # Print formatter
                        spaces_count_needed = 48 - (len(student_firstname) + len(student_lastname))
                        spaces = (" " * spaces_count_needed)

                        # Prints the result for every average grade calculated
                        print(student_firstname, student_lastname, spaces, student_average)
                    print("-----------------------------------------------------------")
                    print("Class Average", (class_sum/student_counter), sep="                                      ")
                    print("Class Minimum", class_min, sep="                                      ")
                    print("Class Maximum", class_max, sep="                                      ")
            except FileNotFoundError:
                print("No such file:", user_input)
    print("Goodbye!")
    return

if __name__ == "__main__":
    main()