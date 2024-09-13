
import sys

# created a dictionary that contains english letters and braille chracters
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', ' ': '......',
    ',': '..O...', ';': '..OO..', ':': '...O..', '.': '...OO.', '!': '...OO.', '?': '..O.O.'
}

# used capitalize to signal conversion and nuber sign to signal numbers
CAPITALIZE = '.....O'  
NUMBER_SIGN = '....OO'  

# Mapping letters a-j to numbers 1-0 
NUM_MAPPING = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6',
    'g': '7', 'h': '8', 'i': '9', 'j': '0'
}
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# created a function that checks for valid braille string
def is_braille(input_str):
    valid_chars = {'O', '.'}
    return all(char in valid_chars for char in input_str.replace(' ', ''))


def english_to_braille(text):
    
    braille = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille.append(CAPITALIZE)  # Capitalize next letter
            braille.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                braille.append(NUMBER_SIGN)  # Enter number mode
                number_mode = True
            braille.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            braille.append(ENGLISH_TO_BRAILLE[' '])  # Add space
            number_mode = False
        else:
            braille.append(ENGLISH_TO_BRAILLE.get(char.lower(), '......'))  # Default for unknown char
            number_mode = False

    return ''.join(braille)

# this section contains functions that convert braille to english

def braille_to_english(braille_str):
    english = []
    i = 0
    capitalize_next = False
    number_mode = False
    braille_length = len(braille_str)

    while i + 6 <= braille_length:
        chunk = braille_str[i:i + 6]

        if chunk == CAPITALIZE:
            capitalize_next = True
        elif chunk == NUMBER_SIGN:
            number_mode = True
        else:
            char = BRAILLE_TO_ENGLISH.get(chunk, '?')
            if number_mode and char in NUM_MAPPING:
                english.append(NUM_MAPPING[char])
            elif capitalize_next:
                english.append(char.upper())
                capitalize_next = False
            else:
                english.append(char)

            # Exit number mode when a space or invalid character appears
            if char == ' ' or char == '?':
                number_mode = False

        i += 6

    # Handle any remaining characters that don't form a complete Braille chunk
    if i < braille_length:
        remaining = braille_str[i:]
        english.append('?')  # Placeholder for incomplete chunk

    return ''.join(english)

    def validate_input(input_str):
    if not input_str:
        raise ValueError("Input cannot be empty.")

    # Check if it's Braille
    if is_braille(input_str):
        return "braille"
    elif all(char.isalnum() or char.isspace() or char in ',;:!?.' for char in input_str):
        return "english"
    else:
        raise ValueError("Input contains invalid characters. Please provide valid English or Braille text.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py \"<text or braille>\"")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])

    try:
        input_type = validate_input(input_str)

        if input_type == "braille":
            output = braille_to_english(input_str)
        else:
            output = english_to_braille(input_str)

        print(output)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()