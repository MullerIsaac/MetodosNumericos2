import numpy as np
import cv2
import matplotlib.pyplot as plt 
from matplotlib import cm 

def convolution(image, kernel):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    output = np.zeros(image.shape)

    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image


    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])


    return output


def kernel_gaussiano(size, sigma=1):
    center = size//2
    x, y = np.mgrid[-center:center+1, -center:center+1]
    return np.exp(-((x**2 + y**2) / (2*sigma**2)))


if __name__ == '__main__':
    img = plt.imread('Processamento de Imagens/Macaco.jpg')
    filt = np.ones(25**2).reshape(25,25)
    img = convolution(img, filt)
    plt.imsave('Processamento de Imagens/macacoBlured.jpg', img, cmap=cm.gray)