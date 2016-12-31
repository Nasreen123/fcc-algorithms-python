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
        positions = []
        for letter in vowels:
            place = english_word.find(letter)
            positions.append(place)
        positions = [i if i != -1 else 100 for i in positions]
        first_vowel = min(positions)
        translated_word = english_word[first_vowel:] + english_word[0:first_vowel] + 'ay'

    return translated_word

tests = ['california', 'paragraphs', 'glove', 'algorithm', 'eight']

for test in tests:
    print translate_pig_latin(test)
