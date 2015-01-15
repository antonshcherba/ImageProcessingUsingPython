__author__ = 'aDmin'

import math
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

def blurImage(image,matrixSize):
    radius = (matrixSize-1) / 2
    blurredImage = image

    width, height, channel = image.shape
    for i in range(0,width-1):
        for j in range(0,height-1):
            di = dj = ddi = ddj = 0
            if i-radius < 0:
                di = i - radius
            if j-radius < 0:
                dj = j - radius
            if i+radius > width:
                ddi = i+radius-width
            if j+radius > height:
                ddj = j+radius-height
            for k in range(0,channel-1):
                blurredImage[i,j,k] = np.average(image[i-radius-di:i+radius-ddi,j-radius-dj:j+radius-ddj,k])

    return blurredImage

def ImageRotation():
    auto = plt.imread('D:/Anton/coursera/1.jpg')
    plt.imshow(auto)
    plt.show()

    autoRotated = np.zeros((800,800,3),dtype=np.int32)
    #autoRotated.shape = auto.shape
    width,height, c = auto.shape

    cos = math.cos(np.pi/4)
    sin = math.sin(np.pi/4)
    rotationMatrix = [[cos,sin,0],
                      [-sin,cos,0],
                      [0,0,1]]
    for i in range(0,width-1):
        for j in range(0,height-1):

            # x = int(i * cos - j * sin)
            # y = int(i * sin + j *cos)
            matrix = np.dot([i, j, 1],rotationMatrix)
            x = int(math.ceil( matrix[0]))
            y = int(math.ceil( matrix[1]))

            #autoRotated[x,y] = auto[i,j]
            autoRotated[x,y,0] = auto[i,j,0]
            autoRotated[x,y,1] = auto[i,j,1]
            autoRotated[x,y,2] = auto[i,j,2]


   #aaa = blurImage(autoRotated,5)
    plt.imshow(autoRotated,None)
    plt.show()
    return

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


    # plt.imshow(auto)
    # plt.show()

    # print width,height, channel
    #
    # plt.imshow(autoWithBlur)
    # plt.show()



    return