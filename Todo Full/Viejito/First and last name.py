#This program that asks for the user's first and last names
print('What is your name?')
first_name = input()
print('What is your last name?')
last_name = input()

first_name_len = len(first_name)
last_name_len = len(last_name)
full_name_len = first_name_len + last_name_len
    
print(f'Hello {last_name} {first_name} your name has {full_name_len} letters and your initials are {first_name[0]}{last_name[0]}.')

first_name_backwards = first_name[::-1]
doubled_name = ""
for i in first_name:
    doubled_name += i * 2

print(f'{doubled_name}, your name spelled backwards is {first_name_backwards}')