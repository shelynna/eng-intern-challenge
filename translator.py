#!/usr/bin/env python3

import sys

# Define mappings for English to Braille
ENGLISH_TO_BRAILLE = {
    # Letters a-z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    # Numbers 0-9
    '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    # Space
    ' ': '......',
}

# Special symbols
CAPITALIZE = '.....O'  # Indicates that the next character is capitalized
NUMBER_SIGN = '....OO'  # Indicates that the following characters are numbers until a space

# Mapping letters a-j to numbers 1-0 (for Braille to English conversion)
NUMBERS_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0',
}

# Reverse mapping for Braille to English
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

def is_braille(input_str):
    """
    Determine if the input string is Braille.
    Only allows characters 'O', '.', and spaces.
    """
    valid_chars = {'O', '.', ' '}
    return all(char in valid_chars for char in input_str)

def english_to_braille(text):
    """
    Convert English text to Braille, handling capitalization and numbers.
    """
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():
            # Capital letter
            braille.append(CAPITALIZE)
            braille.append(ENGLISH_TO_BRAILLE[char.lower()])
            number_mode = False
        elif char.isdigit():
            # Number
            if not number_mode:
                braille.append(NUMBER_SIGN)
                number_mode = True
            braille.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            # Space
            braille.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        else:
            # Lowercase letter or unknown character
            braille.append(ENGLISH_TO_BRAILLE.get(char, '......'))
            number_mode = False

    return ''.join(braille)

def braille_to_english(braille_str):
    """
    Convert Braille string to English text, handling capitalization and numbers.
    """
    english = []
    i = 0
    number_mode = False
    capitalize_next = False
    braille_length = len(braille_str)

    while i + 6 <= braille_length:
        chunk = braille_str[i:i+6]

        if chunk == CAPITALIZE:
            capitalize_next = True
            i += 6
            continue
        elif chunk == NUMBER_SIGN:
            number_mode = True
            i += 6
            continue
        else:
            char = BRAILLE_TO_ENGLISH.get(chunk, '')
            if char == '':
                # Unrecognized Braille pattern
                english.append('?')
            else:
                if number_mode:
                    if char in NUMBERS_MAP:
                        english.append(NUMBERS_MAP[char])
                    else:
                        english.append('?')
                    # Do not reset number_mode; it continues until a space
                else:
                    if capitalize_next:
                        english.append(char.upper())
                        capitalize_next = False
                    else:
                        english.append(char)
            if char == ' ':
                number_mode = False  # Reset number mode at space
            i += 6

    # Handle any remaining incomplete Braille patterns
    if i < braille_length:
        english.append('?')  # Placeholder for incomplete chunk

    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py '<text or braille>'")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)

    print(output)

if __name__ == "__main__":
    main()
