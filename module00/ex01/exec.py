import sys


def alter_string(s: str) -> str:
    return s[::-1].swapcase()


def main():
    if len(sys.argv) > 1:
        print(' '.join(alter_string(arg) for arg in sys.argv[1:][::-1]))


if __name__ == '__main__':
    main()
