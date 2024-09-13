#!/usr/bin/env python3

import sys

# Define mappings for English to Braille
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', ' ': '......',
}


CAPITALIZE = '.....O'  
NUMBER_SIGN = '....OO'


# Visual representation map for Braille
BRAILLE_VISUAL = {
    'O': '●',  
    '.': 'o',  
}

# Mapping letters a-j to numbers 1-0
NUM_MAPPING = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6',
    'g': '7', 'h': '8', 'i': '9', 'j': '0'
}


BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}


def is_braille(input_str):
    
    valid_chars = {'O', '.'}
    return all(char in valid_chars for char in input_str.replace(' ', ''))


def visualize_braille(braille_str):
    
    visual_representation = []
   
    for i in range(0, len(braille_str), 6):
        chunk = braille_str[i:i + 6]
        if len(chunk) == 6:
            visual = (f"{BRAILLE_VISUAL[chunk[0]]} {BRAILLE_VISUAL[chunk[1]]}\n"
                      f"{BRAILLE_VISUAL[chunk[2]]} {BRAILLE_VISUAL[chunk[3]]}\n"
                      f"{BRAILLE_VISUAL[chunk[4]]} {BRAILLE_VISUAL[chunk[5]]}")
            visual_representation.append(visual)
        else:
            visual_representation.append('Invalid Braille Chunk')

   
    return "\n\n".join(visual_representation)


def english_to_braille(text, visualize=False):
   
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille.append(CAPITALIZE)  # Capitalize next letter
            braille.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                braille.append(NUMBER_SIGN) 
                number_mode = True
            braille.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            braille.append(ENGLISH_TO_BRAILLE[' ']) 
            number_mode = False
        else:
            braille.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))  # Default for unknown char
            number_mode = False

    braille_str = ''.join(braille)

    
    if visualize:
        print(visualize_braille(braille_str))

    return braille_str


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py \"<text or braille>\" [--visual]")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    visualize = False

    # Check if the user wants visual representation
    if "--visual" in input_str:
        visualize = True
        input_str = input_str.replace("--visual", "").strip()

    if is_braille(input_str):
        print("Braille to English translation not supported in visual mode yet.")
    else:
        output = english_to_braille(input_str, visualize)
        if not visualize:
            print(output)


if __name__ == "__main__":
    main()
