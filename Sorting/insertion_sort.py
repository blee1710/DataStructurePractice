"""
Insertion sort implementation

Useful for when the list is known to be 
nearly/mostly sorted

"""

numbers = [3,53,65,1,321,54,76,43,2,4,66]


# O(n) best case, O(n^2) generally
def insertionSort(array):
    length = len(array)

    for x in range(length):
        value = array[x]

        j = x-1 
        while j >= 0 and value < array[j] : 
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = value


insertionSort(numbers)

print(numbers)