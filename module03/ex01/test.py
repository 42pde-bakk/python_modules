from ImageProcessor import ImageProcessor
from PIL import UnidentifiedImageError


def test_invalid_file(imp: ImageProcessor, path: str, error) -> None:
    try:
        _ = imp.load(path)
    except error:
        pass
    else:
        assert False, f'Expected {error}'


def main() -> None:
    imp = ImageProcessor()
    test_invalid_file(imp, 'non_existing_file.png', FileNotFoundError)
    test_invalid_file(imp, 'empty_file.png', UnidentifiedImageError)

    arr = imp.load('../resources/42AI.png')
    print(f'{arr=}')
    imp.display(arr)


if __name__ == '__main__':
    main()
