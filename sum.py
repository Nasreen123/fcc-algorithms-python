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


for item in [[4,1], [1,4], [5,10], [10,5]]:
    print(sum_all(item))



def recursive_sum(list, total=0):
    list = sorted(list)
    print('so far', list, total)
    total = total + list[0]

    if list[0] == list[1]:
        return total

    else:
        list[0] = list[0] + 1
        return recursive_sum(list, total)


for item in [[4,1], [1,4], [5,10], [10,5]]:
    print(recursive_sum(item))
