import numpy as np
import cv2
import matplotlib.pyplot as plt

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

def sobel_filter(image, filter, name):
    new_image = convolution(image, filter)
 
    cv2.imwrite(name, new_image)
    return new_image
 
 
if __name__ == '__main__':
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    image = plt.imread('macacoBlured.jpg')
    
    '''geracao da matriz A'''
    image_y = sobel_filter(image, filter, "macacoSobely.jpg")

    '''geracao da matriz B'''
    image_x = sobel_filter(image, np.flip(filter.T, axis=0), "macacoSobelx.jpg")

    '''geracao da matriz C'''
    gradiente = np.sqrt(np.square(image_x) + np.square(image_y))
 
    cv2.imwrite('gradient.jpg', gradiente)

    thr = float(0.5)

    '''geracao da matriz D'''
    matrix_d = np.zeros(image.shape)

    gd_row, gd_col = gradiente.shape

    for row in range(gd_row):
        for col in range(gd_col):
            if abs(gradiente[row, col]) >= thr : 
                matrix_d[row, col] = 1
            else:
                matrix_d[row, col] = 0
    
    cv2.imwrite('matrizD.jpg', matrix_d)



