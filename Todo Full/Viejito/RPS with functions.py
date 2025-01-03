import random

def format_message(message):
    return f'*********** {message} ************'

def choose():
    while True:
        print(format_message("1 for rock, 2 for paper and 3 for scissors. Choose one to start playing: To stop the game, just write (exit)"))
        user_guess = input()

        if user_guess.lower() == 'exit':
            print(format_message('You exit the game, good luck next time :)'))
            break
        if user_guess not in ['1', '2', '3']:
            print(format_message('Invalid choice, please enter 1, 2, or 3.'))
            continue
        
        user_guess = int(user_guess)
        selected_word = random.randint(1, 3) 

        if user_guess == selected_word:
            print(format_message("It's a tie!"))
        elif (user_guess == 1 and selected_word == 3) or (user_guess == 3 and selected_word == 2) or (user_guess == 2 and selected_word == 1):
            print(format_message('You win!'))
        else:
            print(format_message('You lose!'))
            print(selected_word)

choose()