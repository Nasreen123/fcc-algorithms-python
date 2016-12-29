"""
Create a function that takes two or more arrays and returns the symmetric difference
of the arrays.
link: https://www.freecodecamp.com/challenges/symmetric-difference
"""

def get_diff(args):
    #variable to store answers as we iterate
    final_result = []
    all_lists = []
    #for each arg, make sure no duplicates
    for arg in args:
        set_arg = list(set(arg))
        all_lists.append(set_arg)

    #for each item in arg, check occurance in the items in all the other args
    #if it doesnt occur, or it occurs three times, include it
    for this_list in all_lists:
        #print 'arg = ', arg
        other_lists_contents = [item for each_list in all_lists for item in each_list if each_list != this_list]
        #print 'other_lists_contents ', other_lists_contents
        for item in this_list:
            #print 'item = ', item
            if item not in other_lists_contents:
                final_result.append(item)
                #print 'this item is unique ''
            elif other_lists_contents.count(item) == 2:
                final_result.append(item)
                #print 'this item is in all'
    #remove duplicates
    return list(set(final_result))


tests = [
[[1, 2, 3], [5, 2, 1, 4]],
[[1, 2, 5], [2, 3, 5], [3, 4, 5]],
[[1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]],
[[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]],
[[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]
]
answers = [
[3, 4, 5],
[1, 4, 5],
[1, 4, 5],
[2, 3, 4, 6, 7],
[1, 2, 4, 5, 6, 7, 8, 9]
]

for i in range(len(tests)):
    result = get_diff(tests[i])
    print 'test = ', tests[i]
    print 'result = ', result
    print 'answer = ', answers[i]
    if result == answers[i]:
        print 'PASSED'
    else:
        print 'FAILED'
    print '\n'
