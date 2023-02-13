import guess_what

def main():
    scoreboard = guess_what.init_scoreboard()
    while True:
        print('\nHey! This is \'Guess What?\'.')
        print('To quit, enter \'q\'.\n')
        answer = input('1: Play\n2: Display scoreboard\n: ')
        if answer == '1':
            lvl = guess_what.display_get_lvl()
            lower_n, upper_n = guess_what.get_bounds(lvl)
            print('Picking a number between {} and {}.'.format(lower_n, upper_n))
            number = guess_what.generate_num(lower_n, upper_n)
            counter_attempt = 0
            while True:
                counter_attempt += 1
                guess = guess_what.display_get_guess(lower_n, upper_n)
                state = guess_what.check_guess(number, guess)
                if guess_what.display_check_guess(state):
                    guess_what.log_game(scoreboard, lvl, counter_attempt)
                    counter_attempt = 0
                    break
        elif answer == '2':
            guess_what.scoreboard_display_header()
            guess_what.display_rows(scoreboard)
        elif answer == 'q':
            break

if __name__ == '__main__':
    main()
