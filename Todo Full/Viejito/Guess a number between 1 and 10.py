while True:
        number=int(input('Guess a number between 1 and 10:'))
        if number > 10:
            print('WARNING, You are picking an invalid number')
        elif number == 3:
            print('you are right')
            break
        elif number < 3:
            print('you are guessing to low')
        elif number > 3 or number < 10:
            print('you are guessing to high')


