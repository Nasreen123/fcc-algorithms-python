import doctest, math

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

    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])

    else:
        return False


doctest.testmod()
