import random

# set colors and 10 tries
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

# define function that's going to generate the code for us
def generate_code():
    code = []

    # insert 4 random colors into list
    for _ in range(CODE_LENGTH):
        # select random element from colors
        color = random.choice(COLORS)
        code.append(color)

    return code

# function that allows user to guess the code
def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        # check if input is equal to 4
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        # check if color is in the list
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess

# check how many guessing colors are correct
def check_code(guess, real_code):
    color_counts = {}
    # keep track of colors that are in and not in the correct position
    correct_pos = 0
    incorrect_pos = 0
