""" TASK: Take a list of two numbers, and return the sum of
those two numbers and all the numbers between them.
The lowest number will not always come first.

Link to Free Code Camp challenge: 
https://www.freecodecamp.com/challenges/sum-all-numbers-in-a-range"""

def sum_all(list):
    list = sorted(list)
    a, b = list[0], list[1]

    sum = a
    for number in range(b-a):
        a += 1
        sum += a

    return sum


print sum_all([4,1])
print sum_all([1,4])
print sum_all([5,10])
print sum_all([10,5])
