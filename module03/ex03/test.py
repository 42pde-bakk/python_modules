from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


def main() -> None:
    imp = ImageProcessor()
    arr = imp.load("../resources/elon_canaGAN.png")
    # Output :
    # Loading image of dimensions 200 x 200

    cf = ColorFilter()
    # imp.display(arr)
    # imp.display(cf.invert(arr))
    # imp.display(cf.to_green(arr))
    # imp.display(cf.to_red(arr))
    # imp.display(cf.to_blue(arr))
    # cf.to_celluloid(arr)
    imp.display(cf.to_celluloid(arr))
    # imp.display(cf.to_grayscale(arr, 'm'))
    # imp.display(cf.to_grayscale(arr, 'weight', weights=[0.2, 0.3, 0.5]))


if __name__ == '__main__':
    main()
