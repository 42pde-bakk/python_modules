from ImageProcessor import ImageProcessor
from PIL import UnidentifiedImageError
import os


def test_invalid_file(imp: ImageProcessor, path: str, error) -> None:
    try:
        _ = imp.load(path)
    except error:
        pass
    else:
        assert False, f'Expected {error}'


def main() -> None:
    empty_file_path = 'empty_file.png'
    imp = ImageProcessor()
    test_invalid_file(imp, 'non_existing_file.png', FileNotFoundError)
    if not os.path.exists(empty_file_path):
        with open(empty_file_path, 'w') as _:
            # Just create an empty file if it doesn't already exist
            pass
    test_invalid_file(imp, empty_file_path, UnidentifiedImageError)

    arr = imp.load('../resources/42AI.png')
    print(f'{arr=}')
    imp.display(arr)


if __name__ == '__main__':
    main()
