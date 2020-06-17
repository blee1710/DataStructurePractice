"""
Given number (num), return index  value of Fibonacci sequence
where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

The pattern of the sequence is that each value is the
sum of the previous two values

EG. IN => 8 || OUT => 21
"""

# O(2^n)
# adds readability, but call stack memory is higher (no tail call optimisation)
def fibonacciRecursive(num):
    if num < 2:
        return num
    return fibonacciRecursive(num-1) + fibonacciRecursive(num-2)

# O(n)
def fibonacciIter(num):
    sequence = [0,1]
    for x in range(2,num+1):
        sequence.append(sequence[x-2] + sequence[x-1])
    return sequence[num]

print(fibonacciRecursive(8))
print(fibonacciIter(8))