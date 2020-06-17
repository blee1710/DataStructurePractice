# Implementation of mergesort
# Divide and conquer ~ O(n log n) 


def mergesort(array):
    if len(array) == 1:
        return array 
    
    # split array into left and right 
    split = int(len(array)/2)
    left = array[:split]
    right = array[split:]

    return merge(
        mergesort(left),
        mergesort(right)
    )

def merge(left, right):
    array = []
    leftCount = 0 
    rightCount = 0 
    
    # iterate over each half, comparing the two
    while leftCount < len(left) and rightCount < len(right):
        if left[leftCount] < right[rightCount]:
            array.append(left[leftCount])
            leftCount += 1
        elif right[rightCount] < left[leftCount]:
            array.append(right[rightCount])
            rightCount += 1
        else: 
            array.append(left[leftCount])
            leftCount += 1

    # add leftover array 
    array += left[leftCount:]
    array += right[rightCount:]

    return array


numbers = [3,53,65,1,321,54,76,43,2,4,66]

print(mergesort(numbers))
