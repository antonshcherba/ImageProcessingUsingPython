__author__ = 'aDmin'

import scipy
from scipy import ndimage
from scipy import misc

import matplotlib.pyplot as plt
import numpy as np

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

    for i in range(10):
        im = np.random.random_integers(0,255,10000).reshape((100,100))
        misc.imsave('random_%02d.png' % i, im)

    img = plt.imread('D:/Anton/coursera/1.jpg')
    plt.imshow(img)
    plt.show()

    def imageInfo(img):
        """
        Prints size and bits per pixel of img
        :param img:
        :return:
        """
        print type(lena)
        print lena.shape, lena.dtype
        return

    imageInfo(lena)
    help(imageInfo)
    return