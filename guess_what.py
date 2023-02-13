import random

def is_quit(s):
    '''
    Check if the program should be terminated.
    'q' terminates.
    '''
    if s.lower() == 'q':
        quit()

def init_scoreboard():
    '''
    Initialize a scoreboard: a dictionary with lvls of 
    difficulties (keys) and empty lists of attempts it took 
    to complete a game (items).
    '''
    return {1: [], 2: [], 3: []}

def log_game(scoreboard, lvl, attempts):
    '''
    Log how many attempts it took a user to complete
    a game on a given lvl of difficulty into a scoreboard.
    '''
    return scoreboard[lvl].append(attempts)

def scoreboard_get_rows(scoreboard):
    '''
    Get rows from a scoreboard provided.
    Return lists (rows).
    '''
    rows = []
    for i in range(max(map(len, scoreboard.values()))):
        rows.append([]) # create an empy row
        for lvl in [1, 2, 3]:
            if len(scoreboard[lvl]) <= i:
                rows[i].append(0)
                continue
            rows[i].append(scoreboard[lvl][i])
    return rows

def scoreboard_display_header():
    '''
    Display header of the scoreboard.
    '''
    print('|{:^5s}|{:^5s}|{:^5s}|'.format('Lvl 1', 'Lvl 2', 'Lvl 3'))

def display_rows(scoreboard):
    '''
    Display rows from a scoreboard provided.
    '''
    for row in scoreboard_get_rows(scoreboard):
        print('|{:^5d}|{:^5d}|{:^5d}|'.format(row[0], row[1], row[2]))

def check_guess(value, guess):
    '''
    Check if the guess (int) is overshooting, underhooting,
    or is equal to the value (int) provided. Returns 'over', 'under', 'equal'.
    '''
    if guess == value:
        return 'equal'
    elif guess < value:
        return 'under'
    else:
        return 'over'

def display_check_guess(state):
    '''
    Display a message whether the guess is overshooting, underhooting, or is equal to
    the number picked. Function accepts 'over', 'under', 'equal' as arguments.
    If 'equal' is given, function returns True.
    '''
    messages = {'equal': 'You guessed it right!', 'under': 'Your guess is less than the number picked.', 'over': 'Your guess is more than the number picked.'}
    print(messages[state])
    return state == 'equal'
    
def display_get_guess(lower_n, upper_n):
    '''
    Prompt for a number (int) in range from
    a lower number to an upper number. Return the guessed number.
    '''
    while True:
        print('\nThink of any integer value in the range from {} to {}.'.format(lower_n, upper_n))
        guess = input(': ')
        is_quit(guess)
        if guess.isdigit():
            guess = int(guess)
            if lower_n <= guess <= upper_n:
                return guess
            else:
                print('Your guess is outside the range.')
                continue
        else:
            print('Your guess should be an integer!')
            continue

def get_bounds(lvl):
    '''
    Get bounds of the corresponding lvl. Return two values:
    lower and upper bounds.
    '''
    bounds = {1: (1, 20), 2: (1, 50), 3: (1, 100)}
    return bounds[lvl]

def display_get_lvl():
    '''
    Display available difficulties of the game. Prompt for the difficulty number.
    Return the lvl (int) a user chose.
    '''
    print('What level of difficulty would you like to choose?')
    print('1 Easy: a value in a range of 1-20 will be picked.')
    print('2 Medium: a value in a range of 1-50 will be picked.')
    print('3 Hard: a value in a range of 1-100 will be picked.')
    while True:
        lvl = input('\nEnter the difficlty number.\n: ')
        is_quit(lvl)
        if lvl.isdigit() and int(lvl) in [1, 2, 3]:
            return int(lvl)
        else:
            print('Uknown difficulty number!')
            continue
    
def generate_num(lower_n, uppper_n):
    '''
    Generate a random number between a lower num and an upper num provided.
    '''
    return random.randint(lower_n, uppper_n)