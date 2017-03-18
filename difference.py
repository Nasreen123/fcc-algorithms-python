""" Compare two arrays and return a new array with any items only found in one
of the two given arrays, but not both. In other words, return the symmetric
difference of the two arrays

Link to Free Code Camp challenge:
https://www.freecodecamp.com/challenges/diff-two-arrays"""

def diffArray(arr1,arr2):
    """
    >>> diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])
    [4]
    >>> diffArray(['diorite', 'andesite', 'grass', 'dirt', 'pink wool', 'dead shrub'], ['diorite', 'andesite', 'grass', 'dirt', 'dead shrub'])
    ['pink wool']
    >>> diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4])
    ['piglet', 4]
    >>> diffArray([1, 'calf', 3, 'piglet'], [7, 'filly'])
    [1, 'calf', 3, 'piglet', 7, 'filly']

    """

    new1 = [item for item in arr1 if item not in arr2]
    new2 = [item for item in arr2 if item not in arr1]

    newArr = new1 + new2

    return newArr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
