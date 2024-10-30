import random
list_stuff = ["age", "name", "is_student", "total", "my_list", "employee_data", "result", "counter", "file_path", "pi"]
number_list = [10,12,2,3,5,13,32,23,9]

#TODO
# Welcome to this test you will have several mini projects to complete
# Remember that you can use your previuos programs, and make a research in google
#!Any AI is not allow it
#This test is indiviual please make your own test
#you can listen to music during the test
def project_1():
#TODO Project 1: List Creation (5 points)
# Task: Create a list of 10 random integers between 1 and 100, name that list as random_integers.
# Requirements: Use a for loop or list comprehension to generate the list.
    random_integers=[random.randint(1,101) for i in range(10)]
    print(random_integers)
    
def project_2():
#TODO Project 2: List Manipulation (7 points)
# Task: Add two more stuff to the following list (at any position), remove the second element from the list, and print the modified list.
# Requirements: Use append(), insert(), and remove() or pop().
    list_stuff = ["age", "name", "is_student", "total", "my_list", "employee_data", "result", "counter", "file_path", "pi"]
    for list in list_stuff:
        list_stuff.pop(1) 
        print(list)

def project_3():
#TODO Project 3: Indexing and Slicing (6 points)
# Using the list_stuff 
# Task: Print the first 5 elements and the last 3 elements of the list.
# Requirements: Use slicing and indexing.
    slicing = list_stuff[0:5]
    slicing2 = list_stuff[7:10]
    print(f'{slicing} {slicing2}')

def project_4():
#TODO Project 4: Looping with Lists (8 points)
# Task: Use a for loop to find the sum of all the even numbers in the list.
# Requirements: Apply an if statement within the loop to check for even numbers.
    sum= 0
    for i in number_list:
        if i%2==0:
            sum += i
    print(sum)
def project_5():
#TODO Project 5: List Comprehension Basics (9 points)
# Use number_list
# Task: Create a new list, and name it square_numbers, that contains the squares of the original list numbers.
# Requirements: Use a list comprehension for this task.0
    list_of_squares= []
    for int in number_list:
        square= int**2
        list_of_squares.append(square) 
    print(list_of_squares)
    
def project_6():
#TODO Project 6: Filtering with List Comprehensions (10 points)
## Use number_list
# Task: Create a list that contains only the numbers greater than 15 from the original list, name that list as filtered_list.
# Requirements: Use a list comprehension with a filtering condition.
    firltered_list = [i for i in number_list if i <= 15]
    print(firltered_list)
 
def project_7():   
#TODO Project 7: List inside a list (10 points)
# Task: append a list (you will create that list) in the position #4 in the list_stuff
# Print the final list 


#TODO Project 8: loops with Lists (15 points)
# Task: Write a loop that keeps removing elements from the list until the number_list contains only numbers less than 30.
# Requirements: Use while, pop(), remove(), del, sort().

#TODO Project 9: Custom Function (15 points)
# Create a copy of the values from the original number_list, and name it number_list_2
# Use the list number_list_2
# Task: Write a function that takes a list and prints a new list with the odd numbers doubled and even numbers unchanged.
# Requirements: Use list comprehension inside the function, and print().

#TODO Project 10: List Sorting and Methods (8 points)
# Task: Sort the number_list_2 in descending order and print the index of the highest and lowest values in the list.
# Requirements: Use sort(), index(), Hint: look for max() and min () functions.

project_1()