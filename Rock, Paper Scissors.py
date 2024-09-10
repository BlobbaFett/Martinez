import random

word_list = ['rock', 'paper', 'scissors']

while True:
    print('rock, paper, scissors chosse one to start playing: to stop the game just write (exit)')
    user_guess = input()
    selected_word = random.choice(word_list)
    
    if user_guess == 'exit':
        print(f'You exit the game good luck next time :)')
        break
    
    if user_guess not in word_list:
        print(f'invalid word')
        continue
    elif user_guess == selected_word:
        print(f'Its a tie')
    elif (user_guess == 'rock' and selected_word == 'scissors') or (user_guess == 'scissors' and selected_word == 'paper') or (user_guess == 'scissors' and selected_word == 'paper'):
        print(f'you win')
        continue
    else:
        print(f'you lose')