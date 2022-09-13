import numpy as np
from PIL import Image


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path: str) -> np.ndarray:
        im_frame = Image.open(path)
        print(f'Loading image of dimensions {im_frame.width} x {im_frame.height}')
        return np.array(im_frame)

    def display(self, array: np.ndarray) -> None:
        Image.fromarray(array).show()
