__author__ = 'aDmin'

import scipy
from scipy import ndimage
from scipy import misc

import matplotlib.pyplot as plt
import numpy as np

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