import numpy as np
from ScrapBooker import ScrapBooker


def main():
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    crop_result = spb.crop(arr1, (3, 1), (1, 0))
    print(f'{crop_result = }')

    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    print(f"{arr2 = }")
    thin_result = spb.thin(arr2, 3, 0)
    print(f'{thin_result = }')
    print(f"{np.delete(arr2, np.s_[0::3], axis=1) = }")
    # arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    # juxtapose_result = spb.juxtapose(arr3, 3, 1)
    # print(f'{juxtapose_result = }')


def test_thin():
    arr = np.arange(0, 25).reshape(5, 5)
    slic = np.s_[1::2]
    arr2 = np.delete(arr, slic, 1)
    print(f'{arr=}')
    print(f'{arr2=}')


if __name__ == '__main__':
    # test_thin()
    main()
