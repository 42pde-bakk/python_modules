import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path: str) -> np.ndarray:
        im_frame = Image.open(path)
        print(f'Loading image of dimensions {im_frame.width} x {im_frame.height}')
        return np.asarray(im_frame)

    def display(self, array: np.ndarray) -> None:
        image = Image.fromarray(array)
        plt.imshow(image)
        plt.show()
        # Image.fromarray(array).show()
