import numpy as np
import cv2

def img_to_8bit(img):
    print("img b4 scaling: ", img)
    scale = 255/np.max(img)
    return np.multiply(img, scale)



