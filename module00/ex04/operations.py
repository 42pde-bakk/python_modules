import sys


def print_operations(a: int, b: int) -> None:
    print(f'Sum:\t\t{a + b}')
    print(f'Difference:\t{a - b}')
    print(f'Product:\t{a * b}')
    try:
        quotient = a / b
        remainder = a % b
    except ZeroDivisionError:
        quotient = 'ERROR (division by zero)'
        remainder = 'ERROR (modulo by zero)'
    print(f'Quotient:\t{quotient}')
    print(f'Remainder:\t{remainder}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python operations.py <number1> <number2>', file=sys.stderr)
        exit(1)
    try:
        print_operations(int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
        print(f'Please give valid numerical arguments')
