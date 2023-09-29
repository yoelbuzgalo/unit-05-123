import math

def py_tester():
    '''
    This function prompts user to enter pi in decimal digits and gives back a score result of correct digits!
    '''
    user_input = input("Enter pi in decimal digits, up to the first 100: ")
    pi_value = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    score = 0
    for index in range(len(user_input)):
        if user_input[index] == ".":
            continue
        elif user_input[index] == pi_value[index]:
            score += 1
        else:
            print("Incorrect! At index", index, ",it is supposed to be", pi_value[index])
    return score

def display_score(score):
    '''
    This function prints a display score for the player based on the passed score result
    '''
    if score <= 4:
        print("Score", score,": PI Neophyte")
    elif score <= 9:
        print("Score", score, ": PI Novice")
    elif score <= 24:
        print("Score", score, ": PI Journeyman")
    elif score <= 49:
        print("Score", score, ": PI Enthusiast")
    elif score <= 96:
        print("Score", score, ": PI Connoisseur")
    elif score <= 100:
        print("Score", score, ": PI PI Expert")
    elif score > 100:
        print("Score", score, ": PI Imposter")


def main():
    '''
    Main entry of this program
    '''
    display_score(py_tester()) # Calls py_tester and prints the score by calling display_score function

if __name__ == "__main__":
    main()