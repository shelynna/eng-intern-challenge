import sys
import argparse
from typing import List

# Braille to English and English to Braille mappings
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

braille_to_english_map = {v: k for k, v in braille_map.items()}

CAPITALIZE_SYMBOL = '.....O'
NUMBER_SYMBOL = '....OO'
braille_to_number_map = {c: str(i) for i, c in enumerate('abcdefghij', start=1)}

def is_braille(input_str: str) -> bool:
    """Check if the input string is Braille."""
    return all(c in {'O', '.', ' '} for c in input_str)

def english_to_braille(text: str) -> str:
    """Convert English text to Braille."""
    braille = []
    for char in text:
        if char.isupper():
            braille.append(CAPITALIZE_SYMBOL)
            braille.append(braille_map[char.lower()])
        elif char.isdigit():
            braille.append(NUMBER_SYMBOL)
            braille.append(braille_map[char])
        elif char in braille_map:
            braille.append(braille_map[char])
        else:
            braille.append('??????')  # Handle unsupported characters
    return ''.join(braille)

def braille_to_english(braille_str: str) -> str:
    """Convert Braille to English text."""
    english = []
    i = 0
    is_number_mode = False
    is_capital_mode = False

    while i < len(braille_str):
        chunk = braille_str[i:i + 6]

        if chunk == CAPITALIZE_SYMBOL:
            is_capital_mode = True
            i += 6
            continue

        if chunk == NUMBER_SYMBOL:
            is_number_mode = True
            i += 6
            continue

        if chunk in braille_to_english_map:
            letter = braille_to_english_map[chunk]

            if is_number_mode:
                if letter in braille_to_number_map:
                    english.append(braille_to_number_map[letter])
                else:
                    english.append('?')
                is_number_mode = False
            elif is_capital_mode:
                english.append(letter.upper())
                is_capital_mode = False
            else:
                english.append(letter)
        else:
            english.append('?')  # Handle unrecognized Braille chunks

        i += 6

    return ''.join(english)

def process_input(input_str: str) -> str:
    """Process the input and determine whether it's Braille or English."""
    if is_braille(input_str):
        return braille_to_english(input_str)
    return english_to_braille(input_str)

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Translate between Braille and English.")
    parser.add_argument('text', metavar='TEXT', type=str, help="Text or Braille to translate")
    return parser.parse_args()

def main() -> None:
    """Main entry point for the script."""
    args = parse_arguments()
    input_str = args.text

    output = process_input(input_str)
    print(output)

if __name__ == "__main__":
    main()
