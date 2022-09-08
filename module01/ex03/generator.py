import sys
from random import randint


def rng(floor: int, ceiling: int) -> int:
    return randint(floor, ceiling)


def randomize_array(arr: list[str]) -> list[str]:
    new_arr = []
    while arr:
        random_idx = int(rng(0, len(arr) - 1))
        new_arr.append(arr[random_idx])
        arr.pop(random_idx)
    return new_arr


def generator(s: str, sep=' ', option=None) -> str:
    """Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before it is yielded.
    """
    if not isinstance(s, str):
        print(f'ERROR\n', file=sys.stderr)
        return
    arr = s.split(sep)
    if option:
        if option == 'shuffle':
            arr = randomize_array(arr)
        elif option == 'unique':
            arr = list(set(arr))
        elif option == 'ordered':
            arr.sort()
        else:
            print(f'ERROR\n', file=sys.stderr)
            return
    for item in arr:
        yield item


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        for word in generator(arg, ' ', 'unique'):
            print(word)
