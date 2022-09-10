import sys
from csvreader import CsvReader


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 test.py [csvfile.csv]', file=sys.stderr)
        exit(1)
    with CsvReader(sys.argv[1], skip_top=1) as f:
        if f is None:
            print(f'File {f} is corrupted', file=sys.stderr)
        else:
            print(f'{f.getdata() = }')
            print(f'{f.getheader() = }')


if __name__ == '__main__':
    main()
