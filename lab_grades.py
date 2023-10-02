def terminate():
    '''
    This function will return True upon user input of 'y' otherwise False.
    '''
    exit_input = input("Are you sure you want to quit? (y/n)")
    if exit_input.lower() == 'y':
        return True
    return False

def student_lab_average(grades):
    '''
    This function calculates a student's lab average grades based on the data passed
    '''
    total = 0 # Starts with 0
    lab_grades = 10 # Defaulted to 10 lab grades, so no matter how many data is passed but must be all 10 grades for average. 
    for grade in grades:
        total += grade # Add to total for every grade received
    return (total/lab_grades) # Calculates the average based on default 10 classes, so even if it was missing 1 or more classes, it would count them as 0
