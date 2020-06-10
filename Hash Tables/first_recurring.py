#Given an array, return the first recurring character
#Undefined if none

#eg. IN => [2,4,1,3,4,1,2] | OUT => 4
#    IN => [1,3,4,5,6,7]   | OUT => undefined

#Time/Space O(n)
def first_recurring(arr):
    seen = {}

    if len(arr) > 1:
        for character in arr:
            character = str(character)
            if character in seen:
                return character
            else:
                seen[character] = True 

    return None 

retArray = [2,4,1,3,4,1,2]
nonArray = [1,3,4,5,6,7]

print(first_recurring(retArray))
print(first_recurring(nonArray))
