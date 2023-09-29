import math

def py_tester():
    '''
    This function prompts user to enter pi in decimal digits and gives back a score result of correct digits!
    '''
    user_input = input("Enter pi in decimal digits, up to the first 100: ")
    pi_value = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    score = 0
    for index in range(len(user_input)):
        if user_input[index] == pi_value[index]:
            score += 1
            continue
        else:
            print("Incorrect! At index", index, ",it is supposed to be", pi_value[index])
    return score

def main():
    '''
    Main entry of this program
    '''
    print(py_tester())

if __name__ == "__main__":
    main()