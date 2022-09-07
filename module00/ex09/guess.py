import random

MIN = 0
MAX = 99


def quit_game() -> None:
    print('Goodbye!')
    exit(0)


def win_game(guess_amount: int, guess: int) -> None:
    if guess == 42:
        print('The answer to the ultimate question of life, the universe and everything is 42.')
    if guess_amount == 1:
        print('Congratulations! You got it on your first try!')
    else:
        print(f'Congratulations, you\'ve got it!\nYou won in {guess_amount} attempts!')
    quit_game()


def print_intro() -> None:
    print('This is an interactive guessing game')
    print('You have to enter a number between 1 and 99 to find out the secret number.')
    print('Type \'exit\' to end the game.')
    print('Good luck!\n')


def game():
    super_secret_nb = random.randint(MIN, MAX)
    guesses_amount = 0
    print_intro()
    while True:
        try:
            guesses_amount += 1
            guess = input(f'What\'s your guess between {MIN} and {MAX}?\n>> ')
            if guess.lower() == 'exit':
                quit_game()
            guess = int(guess)
            if guess < super_secret_nb:
                print('Too low!')
            elif guess > super_secret_nb:
                print('Too high!')
            else:
                win_game(guesses_amount, guess)
        except ValueError:
            pass


if __name__ == '__main__':
    game()
