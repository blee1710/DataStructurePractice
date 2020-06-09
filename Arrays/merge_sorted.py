#Merge two sorted arrays
#eg. IN => ([0,4,5],[1,3,6]) | OUT => [0,1,3,4,5,6]


#Time/Space O(a + b)
def mergeSorted(arr1, arr2):
    #returns the sole array if one is empty, or none
    if len(arr1)==0 or len(arr2)==0:
        return arr1 + arr2
    
    sortedList = []
    i = 0
    j = 0

    #linear time traversal until end of one array
    while i<len(arr1) and j<len(arr2):

        if arr1[i] <= arr2[j]:
            sortedList.append(arr1[i])
            i+=1
        
        elif arr2[j] < arr1[i]:
            sortedList.append(arr2[j])
            j+=1

    #adds remainder of list to sorted
    return sortedList+arr1[i:]+arr2[j:]

#Running test case
print(mergeSorted([0,4,5],[1,3,6]))
