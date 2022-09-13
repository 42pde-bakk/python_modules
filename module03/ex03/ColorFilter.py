import numpy as np


class ColorFilter:
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
        for y, row in enumerate(array):
            for x, rgb in enumerate(row):
                new_arr[y][x][:2] = 0
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
        for y, row in enumerate(array):
            for x, rgb in enumerate(row):
                new_arr[y][x][0] = 0
                new_arr[y][x][2] = 0
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
        for y, row in enumerate(array):
            for x, rgb in enumerate(row):
                new_arr[y][x][1:3] = 0
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
        pass

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
        new_array = array.copy()
        for y, row in enumerate(new_array):
            for x, item in enumerate(row):
                if Filter == 'mean' or Filter == 'm':
                    avg = sum(item[:3]) / 3
                    new_array[0] = avg
                    new_array[1] = avg
                    new_array[2] = avg
                elif Filter == 'weight' or Filter == 'w':
                    new_array[y][x][0] *= kwargs['weights'][0]
                    new_array[y][x][1] *= kwargs['weights'][1]
                    new_array[y][x][2] *= kwargs['weights'][2]
        return new_array
