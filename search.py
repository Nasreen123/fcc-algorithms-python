""" Perform a search and replace on the sentence using the arguments provided
and return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with (after).

NOTE: Preserve the case of the original word when you are replacing it. For
example if you mean to replace the word "Book" with the word "dog", it should
be replaced as "Dog"

Free Code Camp link: https://www.freecodecamp.com/challenges/search-and-replace """


def my_replace(str,before,after):

    #Convert to lower incase of different capitalization.
    lowerstr = str.lower()
    lowerbefore = before.lower()
    #Now we can be sure to find the position of before in the string
    position = lowerstr.find(lowerbefore)

    #Find out if first letter is capitalized.
    if str[position].upper() == str[position]: #it is capitalized
        before = before[0].upper() + before[1:] #capitalize before
        after = after[0].upper() + after[1:] #capitalize after

    return str.replace(before,after)



tests = [("A quick brown fox Jumped over the lazy dog", "jumped", "leaped"),
("Let us go to the store", "store", "mall"),
("He is Sleeping on the couch", "Sleeping", "sitting"),
("This has a spellngi error", "spellngi", "spelling"),
("His name is Tom", "Tom", "john"),
("Let us get back to more Coding", "Coding", "algorithms")]

for test in tests:
    print my_replace(test[0],test[1],test[2])
