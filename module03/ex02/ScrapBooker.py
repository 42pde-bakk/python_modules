import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array: np.ndarray, dim: tuple[int, int], position: tuple[int, int]) -> np.ndarray | None:
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or not isinstance(position, tuple):
            return None
        if len(dim) != 2 or len(position) != 2 or any([not isinstance(x, int) for x in dim + position]):
            return None
        x1, y1 = position
        x2, y2 = x1 + dim[0], y1 + dim[1]
        new_arr = array[x1:x2, y1:y2]
        return new_arr

    def thin(self, array: np.ndarray, n: int, axis: int) -> np.ndarray | None:
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thinned numpy.ndarray.
        None (if combination of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(n, int) or not isinstance(axis, int) or not (axis == 0 or axis == 1):
            return None
        if not isinstance(array, np.ndarray) or n > array.shape[axis]:
            return None
        print(f'{n = }, {np.s_[0:-1:3] = }, {axis = }')
        print(f'{array[np.s_[0::n]] = }')
        return np.delete(array, np.s_[::n], axis=axis)

    def juxtapose(self, array: np.ndarray, n: int, axis: int) -> np.ndarray | None:
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int):
            return None
        if n <= 0 or not (0 <= axis <= 1):
            return None
        if axis == 0:
            return np.tile(array, (n, 1))
        else:
            return np.tile(array, (1, n))

    def mosaic(self, array: np.ndarray, dim: tuple[int, int]) -> np.ndarray | None:
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, int) or any(not isinstance(x, int) for x in dim):
            return None
        return np.tile(array, dim)
