import numpy as np
from ScrapBooker import ScrapBooker


def main():
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    crop_result = spb.crop(arr1, (3, 1), (1, 0))
    print(f'{crop_result = }')

    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    thin_result = spb.thin(arr2, 3, 0)
    print(f'{thin_result = }')
    arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    juxtapose_result = spb.juxtapose(arr3, 3, 1)
    print(f'{juxtapose_result = }')


if __name__ == '__main__':
    main()
