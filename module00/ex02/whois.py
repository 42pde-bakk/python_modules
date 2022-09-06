import sys


def main() -> None:
    try:
        assert(len(sys.argv) > 1), "no arguments provided"
        assert(len(sys.argv) == 2), "more than one argument are provided"
        assert(sys.argv[1].isdigit()), "argument is not an integer"
        nb = int(sys.argv[1])
        if nb % 2 == 0:
            print('I\'m Even.')
        else:
            print('I\'m Odd.')
    except AssertionError as e:
        print(f'AssertionError: {e}')


if __name__ == '__main__':
    main()
