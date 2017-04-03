import doctest

def mutation(input_array):
    """
    >>> mutation(["hello", "hey"])
    False
    >>> mutation(["hello", "Hello"])
    True
    >>> mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])
    True
    >>> mutation(["Mary", "Army"])
    True
    >>> mutation(["Mary", "Aarmy"])
    True
    >>> mutation(["Alien", "line"])
    True
    >>> mutation(["floor", "for"])
    True
    >>> mutation(["hello", "neo"])
    False
    >>> mutation(["voodoo", "no"])
    False
    """

    haystack, needles = input_array

    if len(needles) == 0: #base case
        return True

    else: #check next first, then recurse
        if needles[0].lower() in haystack.lower():
            return mutation([haystack, needles[1:]])
        else:
            return False


doctest.testmod()
