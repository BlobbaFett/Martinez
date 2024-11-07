#This program prints Hello! 10 times
for Hello in range(10):
    print('Hello!')
#This program crate a variable named i
for i in range(15):
    i=i+1
    print ('Hello! i is set to' + str(i))
#This program sums all the number up to 1 million
sum = 0
for million in range(1000000):
    sum += million
print(sum)
#This program asks the user to input 2 integers, and print the square of every other number between those two numbers
num1 = int(input('enter a number: '))
num2 = int(input('enter a number: '))
for num3 in range(num1, num2,2):
    print(num3 **2)
#This program tell the user if it is a prime number or even number
num = int(input('enter a number: '))
if num == 2:
    print('prime number')
elif num %2==0:
    print('even') 
else:
    print('prime')
