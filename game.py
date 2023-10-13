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
