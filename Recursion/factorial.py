# Factorial functions

def recursiveFactorial(num):
    # base case
    if num == 1:
        return 1 
    
    # getting closer to base + recursive case
    else:
        return (num * recursiveFactorial(num-1))

def recursiveIterative(num):
    total = 1
    for x in range(2,num+1):
        total = total * x 
    
    print(total)
    


print(recursiveFactorial(10))

recursiveIterative(10)