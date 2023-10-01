import cv2
import numpy as np
import os
from PIL import Image


def transparent_image(res_image):
    # threshold on black to make a mask
    color = (255, 255, 255)
    mask = np.where((res_image == color).all(axis=2), 0, 255).astype(np.uint8)

    # put mask into alpha channel
    transparent_img = res_image.copy()
    transparent_img = cv2.cvtColor(transparent_img, cv2.COLOR_BGR2BGRA)
    transparent_img[:, :, 3] = mask

    return transparent_img


def image_preprocessing(input_img):
    # Normalization
    norm_img = np.zeros((input_img.shape[0], input_img.shape[1]))
    norm_img = cv2.normalize(input_img, norm_img, 0, 255, cv2.NORM_MINMAX)
    # cv2.imshow('norm_img', norm_img)

    # skew correction
    # co_ords = np.column_stack(np.where(norm_img > 0))
    # angle = cv2.minAreaRect(co_ords)[-1]
    # if angle < -45:
    #     angle = -(90 + angle)
    # else:
    #     angle = -angle
    # (h, w) = image.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # cv2.imshow('rotated', rotated)

    # image scaling
    scaled_image = Image.fromarray(norm_img)
    length_x, width_y = scaled_image.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = scaled_image.resize(size, Image.ANTIALIAS)
    im_resized = np.array(im_resized)
    # cv2.imshow('im_resized', im_resized)

    # Noise Removal
    sharped_img = cv2.fastNlMeansDenoisingColored(im_resized, None, 10, 10, 7, 15)
    # cv2.imshow('sharped_img', sharped_img)

    # Thinning and Skeletonization
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(sharped_img, kernel, iterations=1)
    # cv2.imshow('erosion', erosion)
    return erosion


# if __name__ == '__main__':
def main_fun(img_path):
    img = cv2.imread(img_path)
    img = image_preprocessing(img)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = np.zeros_like(img)
    image[gray_image > 150] = [255, 255, 255]
    final_res = transparent_image(image)
    path = 'static/out_put/out_put.png'
    cv2.imwrite(path, final_res)
    return path
