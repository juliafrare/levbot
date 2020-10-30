from cv2 import imread, imwrite, resize, INTER_NEAREST
import os

def resize_small(filename):
    image = imread(filename)
    new_image = resize(image, (image.shape[1] // 8, image.shape[0] // 8), interpolation=INTER_NEAREST)
    name_mini = os.path.splitext(filename)[0] + "mini.jpg"
    imwrite(name_mini, new_image)
    return name_mini

def resize_big(filename):
    image = imread(filename)
    new_image = resize(image, (image.shape[1] * 8, image.shape[0] * 8), interpolation=INTER_NEAREST)
    name_big = os.path.splitext(filename)[0] + "big.jpg"
    imwrite(name_big, new_image)
    return name_big

def moremorejpeg(filename):
    small = resize_small(filename)
    new_name = resize_big(small)
    return new_name


moremorejpeg("tristeza.jpg")