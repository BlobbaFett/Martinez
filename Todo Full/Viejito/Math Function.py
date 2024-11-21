def factorial(n):
    result = 1
    for i in range (2,n+1):
        result *= i
        print(result)
factorial(6)

def reminder(a,b):
    print(a-((a//b)*b))
    
reminder(3,2)