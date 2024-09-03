import random

my_num = random.randint(1, 10)
print('For exit the program write: "exit"')
while True:
    number = input('Guess a number between 1 and 10: ')
    
    if number == 'exit':
        print('You exit the game good luck next time :)')
        break
    number = int(number)
        
    if number < 1 or number > 10:
        print('WARNING, You are picking an invalid number')
    elif number == my_num:
        print('you are right')
        break
    elif number < my_num:
        print('you are guessing to low')
    else:
        print('you guess to high')