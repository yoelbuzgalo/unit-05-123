def terminate():
    exit_input = input("Are you sure you want to quit? (y/n)")
    if exit_input.lower() == 'y':
        return True
    return False