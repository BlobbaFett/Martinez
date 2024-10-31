import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
user_guess = ""

while True:
    user_guess= input('Guess a word between these: python, java, javascript, ruby, html, css: ')
    
    if user_guess == 'exit':
        print('You exit the game good luck next time :)')
        break
    elif user_guess == selected_word:
        print('you are right')
        break
    else:
        print('wrong answer')  
