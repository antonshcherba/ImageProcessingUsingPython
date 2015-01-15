__author__ = 'aDmin'

import scipy
from scipy import ndimage
from scipy import misc

import matplotlib.pyplot as plt
import numpy as np

def imageInfo(img):
    """
    Prints size and bits per pixel of img
    :param img:
    :return:
    """
    print type(img)
    print img.shape, img.dtype
    return

def imageQuantization(levels):
    maxIntensity = 256.0
    step = maxIntensity / levels

    lena = misc.lena()
    lenaQuantized = lena
    width, height = lena.shape
    for i in range(0, width):
        for j in range(0,height):
            lenaQuantized[i,j]= int(lena[i,j] / step) * step

    return lenaQuantized

def process():
    lena = misc.lena()
    # misc.imsave('lena.png', lena)
    #
    # plt.imshow(lena)
    # plt.show()

    print type(lena)
    print lena.shape, lena.dtype

    lena.tofile('lena.raw')
    lena_from_raw = np.fromfile('lena.raw',dtype = np.int32)
    print lena_from_raw.shape

    lena_from_raw.shape = (512,512)
    print lena_from_raw.shape

    lena_memmap = np.memmap('lena.raw',dtype=np.int32,shape=(512,512))

    # auto = plt.imread('D:/Anton/coursera/1.jpg')
    # autoWithBlur = auto
    # plt.imshow(auto)
    # plt.show()

    # width, height, channel = auto.shape
    # for i in range(0,width-1):
    #     for j in range(0,height-1):
    #         if i > 0 and j > 0 and i < width-1 and j < height-1:
    #             for k in range(0,channel-1):
    #                 autoWithBlur[i,j,k] = np.average([auto[i-1,j,k], auto[i-1,j-1,k], auto[i,j-1,k], auto[i+1,j,k], auto[i,j+1,k], auto[i+1,j+1,k], auto[i-1,j+1,k], auto[i+1,j-1,k]])
    # print width,height, channel
    #
    # plt.imshow(autoWithBlur)
    # plt.show()

    lenaQuantized = imageQuantization(4)
    plt.imshow(lenaQuantized,plt.cm.gray)
    plt.show()
    return