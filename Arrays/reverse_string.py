# Create a function which reverses a string
# eg. IN => 'Hi i'm Brandon' | OUT => 'nodnarB m'i iH'


#Time: O(n) 
#Space: O(n)
def reverse(str):
    reverselist = []
    for i in range(len(str)-1, -1,-1): 
        reverselist.append(str[i])
    return ''.join(reverselist)
    #return str[::-1]

#Running test case
input = "Hi i'm Brandon"

print(reverse(input))

