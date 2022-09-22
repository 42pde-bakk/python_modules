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


def generator(s: str, sep=' ', option=None) -> str | None:
    """Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before it is yielded.
    """
    if not isinstance(s, str):
        print(f'ERROR', file=sys.stderr)
        return None
    arr = [word for word in s.split(sep) if word]  # Remove empty strings
    if option:
        if option == 'shuffle':
            arr = randomize_array(arr)
        elif option == 'unique':
            arr = list(set(arr))
        elif option == 'ordered':
            arr.sort()
        else:
            print(f'ERROR', file=sys.stderr)
            return
    for item in arr:
        yield item


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please give me some input to put through the generator', file=sys.stderr)
    else:
        string = sys.argv[1]
        option = sys.argv[2] if len(sys.argv) == 3 else None
        for word in generator(string, ' ', option):
            print(f'{word = }')
