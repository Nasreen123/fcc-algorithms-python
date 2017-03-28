import doctest

def palindrome(string):
    """
    >>> palindrome("eye")
    True
    >>> palindrome("race car")
    True
    >>> palindrome("not a palindrome")
    False

    """

    string = string.replace(" ", "")

    length = len(string)

    if not length % 2:
        length = length - 1

    for x in range(int(length/2)):
        if string[x] != string[(length-x-1)]:
            return False

    return True


doctest.testmod()
