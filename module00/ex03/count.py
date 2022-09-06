import string
import sys
from typing import Union


def count(s, marks):
    return sum(1 for c in s if c in marks)


def text_analyzer(s: Union[str, None]) -> None:
    """Takes a string and outputs the amount of characters, upper- and lowercase letters, punctuations and spaces"""
    if s is None:
        s = input('What is the text to analyze?\n')
    try:
        assert(isinstance(s, str)), "argument is not a string"
    except AssertionError as e:
        print(f'AssertionError: {e}')
        return
    print(f'The text contains {len(s)} character(s):')
    print(f'- {count(s, set(string.ascii_uppercase))} upper letter(s)')
    print(f'- {count(s, set(string.ascii_lowercase))} lower letter(s)')
    print(f'- {count(s, set(string.punctuation))} punctuation mark(s)')
    print(f'- {count(s, set(string.whitespace))} space(s)')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Please only provide me with one argument')
    else:
        if len(sys.argv) == 1:
            text_analyzer(None)
        else:
            text_analyzer(sys.argv[1])
