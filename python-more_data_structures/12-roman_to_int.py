#!/usr/bin/python3
def roman_to_int(roman_string):
    out = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, \
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i > 0 and roman_numerals[roman_string[i]] >\
                roman_numerals[roman_string[i - 1]]:
            out += roman_numerals[roman_string[i]] -\
                2 * roman_numerals[roman_string[i - 1]]
        else:
            sum += roman_numerals[roman_string[i]]
    return out
