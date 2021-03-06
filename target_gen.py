#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Adapted from these sources:
# https://www.learnopencv.com/alpha-blending-using-opencv-cpp-python/

import numpy as np
import cv2

from ImageGenerator.proto import Target
from ImageGenerator.proto import Color

# TODO: add Anti-aliasing
# TODO: add Noise addition


def create_target_image(target):
    # TODO: build a function to render targets. This should look like the function below but using the target
    #  object passed in instead of hardcoded values
    # creates an image rendering in 4 channels (BGRA) of the target passed to it. This should use the same methods as
    # the create_target_image_test function below.
    img = np.zeros((10, 10, 10, 10))
    return


def create_target_image_test():

    # Parameters for input shape
    shape_color_bgr = (0., 255., 255.)   # White
    letter_color_bgr = (192., 137., 121.)

    # Read the images
    # binary filter and create alpha channel for letter
    png_letter = cv2.imread('Letters/n.png', cv2.IMREAD_UNCHANGED)
    letter_filter = cv2.inRange(png_letter, (100, 0, 0), (255, 255, 255))
    # add an alpha channel by extending the same array to alpha channel
    img_letter = np.repeat(letter_filter[:, :, np.newaxis], 4, axis=2)

    # repeat for shape
    png_shape = cv2.imread('Shapes/4.png', cv2.IMREAD_UNCHANGED)
    shape_filter = cv2.inRange(png_shape, (100, 0, 0), (255, 255, 255))
    img_shape = np.repeat(shape_filter[:, :, np.newaxis], 4, axis=2)

    img_letter = img_letter.astype(float)
    img_shape = img_shape.astype(float)
    alpha = img_letter/255.

    color_norm = np.reshape(letter_color_bgr + (255.,), [1, 1, 4])/255.
    color_mat = np.tile(color_norm, list(np.shape(img_letter)[0:2])+[1])
    img_letter = np.multiply(img_letter, color_mat)/255.

    color_norm = np.reshape(shape_color_bgr + (255.,), [1, 1, 4])/255.
    color_mat = np.tile(color_norm, list(np.shape(img_shape)[0:2])+[1])
    img_shape = np.multiply(img_shape, color_mat)/255.

    # linear interpolation based on alpha

    # Multiply the background with ( 1 - alpha )

    img_shape = cv2.multiply(1.0 - alpha, img_shape)
    img_out = cv2.add(img_shape, img_letter)
    return img_out


if __name__ == '__main__':
    cv2.imshow('output', create_target_image_test())
    cv2.waitKey(0)
