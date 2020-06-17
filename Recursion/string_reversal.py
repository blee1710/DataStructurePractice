# String reversal using recursion 

def reverseRecursive(str):
    if str == "":
        return "" 
    else: 
        return reverseRecursive(str[1:]) + str[0]


print(reverseRecursive('Hello'))