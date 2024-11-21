import os 
import random 
print('Lets play rock paper scissors')
print('1 for rock, 2 for paper, 3 for scissors')

def rock_paper_scissors():
    while True: 
        answer = input(int())
        computer = random.randint = (1, 3)
        if answer == computer:
            print('tie')
        elif (answer == 1 and computer == 3) or (answer == 3 and computer == 2) or (answer == 2 and computer == 1):
            print('you win')
        else:
            print('you lose')
            
rock_paper_scissors()
    