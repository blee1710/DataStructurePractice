# Bubble sort implementation

numbers = [3,53,65,1,321,54,76,43,2,4,66]

#O(n^2) Time / O(1) Space
def bubbleSort(array):
    length = len(array)
    for x in range(0,length):
        for j in range(0,length-1):
            if array[j] > array[j+1]:
                # swap 
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


bubbleSort(numbers)

print(numbers)