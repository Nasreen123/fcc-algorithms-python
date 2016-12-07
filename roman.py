"""Convert the given number into a roman numeral.
All roman numerals answers should be provided in upper-case.

Link to Free Code Camp challenge:
https://www.freecodecamp.com/challenges/roman-numeral-converter"""

#Roman numeral symbols and the amounts they symbolize:
symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
amounts = [1000, 500, 100, 50, 10, 5, 1]

#Lists for the cases when a smaller number symbol preceeds a larger symbol:
to_replace = ['VIIII', 'IIII', 'LXXXX', 'XXXX', 'DCCCC', 'CCCCC']
replace_with = ['IX', 'IV', 'XC', 'XL', 'CM', 'CD']

def convert_to_roman_numeral(num):
    roman_num = ''

    """Iterate through the symbols in the list of symbols.  If the number to
       convert is longer than the amount the symbol represents, add the symbol
       to the roman numeral, and remove the amount it represents from the
       number."""
    for i in range(len(symbols)):
        while num >= amounts[i]:
            num = num - amounts[i]
            roman_num = roman_num + symbols[i]

    """Iterate through the to_replace list, if an item from the list is present
       in the roman numeral, replace it with it's equivalent in replace_with."""
    for i in range(len(to_replace)):
        start = roman_num.find(to_replace[i])
        if start != -1:
            end = start + len(to_replace[i])
            roman_num = roman_num[:start] + replace_with[i] + roman_num[end:]

    return  roman_num

tests = [2, 3, 4, 5, 9, 12, 16, 29, 44, 45, 68, 83, 97, 99, 500, 501, 649, 798, \
891, 1000, 1004, 1006, 1023, 2014, 3999]

for number in tests:
    print number, convert_to_roman_numeral(number)
