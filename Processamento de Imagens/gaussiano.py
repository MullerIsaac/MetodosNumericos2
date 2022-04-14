import numpy as np
import cv2
import matplotlib.pyplot as plt 
from matplotlib import cm 

def TranformarEmCinza(img):
    return np.matmul(img, [0.2989, 0.5870, 0.114]).astype(np.uint)


def convolucao(img: np.ndarray, filtro: np.ndarray):
    iw, ih = img.shape
    kw, kh = filtro.shape
    assert(kw % 2 == 1 and kh % 2 ==1 )
    kcx, kcy = kw//2, kh//2
    out = np.zeros(img.shape)

    for x, y in np.ndindex(*out.shape):
        sub_img = img[max(0, x-kcx): min(iw, x-kcx + (kw)),
                      max(0, y-kcy): min(ih, y-kcy + (kh))]

        sub_filt = filtro[max(0,kcx-x): (kw if iw > x+kcx else iw-(x+kcx)-1),
                            max(0, kcy-y): (kh if ih > y+kcy else ih-(y+kcy)-1)]

        out[x, y] = np.vdot(sub_img, sub_filt)/np.sum(sub_filt.flatten())
    out = np.abs(out) 
    return out.astype(np.uint8)

def kernel_gaussiano(size, sigma=1):
    center = size//2
    x, y = np.mgrid[-center:center+1, -center:center+1]
    return np.exp(-((x**2 + y**2) / (2*sigma**2)))


if __name__ == '__main__':
    img = plt.imread('Macaco.jpg')
    img = TranformarEmCinza(img)
    filt = np.ones(25**2).reshape(25,25)
    img = convolucao(img, filt)
    plt.imsave('macacoBlured.jpg', img, cmap=cm.gray)
