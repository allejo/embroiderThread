# Helper Functions

# Function requests user input. 
# maxNum is the max/last number displayed on the list; numbers not on the list will not exist and may cause error
def user_input_int(maxNum):
    while True:
        user_input = input('Enter a number.')

    ## Can delete once done - only for debugging purposes
        print('Printing from utilities.py --> user_input_int(). User input: ' + str(user_input) )

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            print("Try again, enter a number.")

# Function requests user input. 
# maxNum is the max/last number displayed on the list; numbers not on the list will not exist and may cause error
# valid_options --> represents only the valid letter(s).
def user_input_option(valid_options, maxNum):
    while True:
        user_input = input('Enter your selection.')

    ## Can delete once done - only for debugging purposes
        print('Printing from utilities.py  --> user_input_option. User input: '+ str(user_input))

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            if user_input.upper() in valid_options:
                return user_input.upper()
            
            print("Try again, enter a valid selection.")


def user_input_options(valid_options):
    while True:
        user_input = input('Enter your selection.')

        try:
            user_input = int(user_input)
        except ValueError:
            user_input = user_input.upper()
            pass

        if user_input in valid_options:
            return user_input

        print("Try again, enter a valid selection.")
