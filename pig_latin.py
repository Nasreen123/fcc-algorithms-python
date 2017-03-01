"""
TASK: Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an "ay".

If a word begins with a vowel you just add "way" to the end.

Input strings are guaranteed to be English words in all lowercase.

Link:https://www.freecodecamp.com/challenges/pig-latin
"""


def translate_pig_latin(english_word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if english_word[0] in vowels:
        translated_word = english_word + 'way'

    else:
        #find the positions of all the vowels in the word:
        positions_of_vowels = [english_word.find(letter) for letter in vowels if english_word.find(letter) != -1]
        #use positions of all the vowels to find the first vowel
        first_vowel = min(positions_of_vowels)
        #slice the word at the first vowel
        translated_word = english_word[first_vowel:] + english_word[0:first_vowel] + 'ay'

    return translated_word

tests = ['california', 'paragraphs', 'glove', 'algorithm', 'eight']

for test in tests:
    print translate_pig_latin(test)
