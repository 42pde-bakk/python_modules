import string
import sys


def count(s, marks):
    return sum(1 for c in s if c in marks)


def should_keep(s: str, n: int) -> bool:
    return len(s) - count(s, string.punctuation) > n


def clean_word(s: str) -> str:
    return s.translate(str.maketrans('', '', string.punctuation))


def filter_words(s: str, n: int) -> None:
    words = s.split()
    print([clean_word(word) for word in words if should_keep(word, n)])


if __name__ == '__main__':
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print('ERROR', file=sys.stderr)
    else:
        filter_words(sys.argv[1], int(sys.argv[2]))
