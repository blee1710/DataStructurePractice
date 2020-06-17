# Selection sort implementation

numbers = [3,53,65,1,321,54,76,43,2,4,66]

# Time: O(n^2) || Space: O(1)
def selectionSort(array):
    length = len(array)
    for x in range(length):
        minimum = x
        temp = array[x]
        for j in range(x+1, length):
            if array[j] < array[minimum]:
                minimum = j 
        
        array[x] = array[minimum]
        array[minimum] = temp 

selectionSort(numbers)
print(numbers)