#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    total = 0

    for i in range(len(roman_string)):
        if roman_val.get(roman_string[i], 0) == 0:
            return 0

        if (i != (len(roman_string) - 1) and
                roman_val[roman_string[i]] < roman_val[roman_string[i + 1]]):
            total += roman_val[roman_string[i]] * -1
        else:
            total += roman_val[roman_string[i]]

    return total
