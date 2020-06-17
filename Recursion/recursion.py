# Simple recursive function example


counter = 0 

def recursive():
    global counter
    print(counter)

    # base case
    if counter > 3:
        return 'Done'

    # method to get closer to base case
    counter = counter + 1

    # recursive case
    return recursive()


print(recursive())


