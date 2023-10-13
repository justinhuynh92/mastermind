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

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    #find colors that are in the correct position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        # print individual element from the list
        print("You ran out of tries, the code was:", *code)

# run the game file
if __name__ == "__main__":
    game()
