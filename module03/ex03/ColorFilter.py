import numpy as np


RED = 0
GREEN = 1
BLUE = 2


class ColorFilter:
    """Different libs represent RGB values differently
    Here, I assume RGB is represented as 3 uint8 values:
    [0, 12, 254] for example
    """
    def invert(self, array: np.ndarray) -> np.ndarray | None:
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()

        new_arr[:, :, :3] = 255 - new_arr[:, :, :3]
        # Not doing
        # return 255 - new_arr
        # Because I want the possible alpha values to remain the same
        return new_arr

    def to_blue(self, array: np.ndarray) -> np.ndarray | None:
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        new_arr[:, :, RED] = 0
        new_arr[:, :, GREEN] = 0
        return new_arr

    def to_green(self, array: np.ndarray) -> np.ndarray | None:
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        new_arr[:, :, RED] = 0
        new_arr[:, :, BLUE] = 0
        return new_arr

    def to_red(self, array: np.ndarray) -> np.ndarray | None:
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        new_arr[:, :, GREEN] = 0
        new_arr[:, :, BLUE] = 0
        return new_arr

    def to_celluloid(self, array: np.ndarray) -> np.ndarray | None:
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        new_array = array.copy()
        for i in range(3):
            new_array[new_array[:, :, i] <= 64, i] = 0
            new_array[((new_array > 64) & (new_array <= 128))[:, :, i], i] = 64
            new_array[((new_array > 128) & (new_array <= 192))[:, :, i], i] = 128
            new_array[new_array[:, :, i] > 192, i] = 192
        return new_array

    def to_grayscale(self, array: np.ndarray, Filter, **kwargs) -> np.ndarray | None:
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(Filter, str):
            return None
        new_array = np.array(array)
        if Filter in ('mean', 'm'):
            for row in new_array:
                for rgb in row:
                    avg = sum(rgb[0:3]) / 3  # Not using the alpha value
                    rgb[0:3] = avg
        elif Filter in ('weight', 'w'):
            if 'weights' not in kwargs:
                return None
            weights = np.array(kwargs['weights'])
            for row in new_array:
                for rgb in row:
                    avg = sum(rgb[0:3] * weights) / 3
                    rgb[0:3] = avg
        else:
            return None
        return new_array
