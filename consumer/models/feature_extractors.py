from skimage import feature
import numpy as np
import math
import cv2
from models.utils import *

def hogFeats(img, params={'visualize': True}):
    save_path = '/home/sumukha/Downloads/brain_hog.jpg'
    print("Image: ", img)
    bin_edges, hog_img = feature.hog(img, **params) # visualize=True)
    print("Hog features shape: ", hog_img.shape)
    cv2.imwrite(save_path, img_to_8bit(hog_img))
    return hog_img

def cannyEdge(img, params={}):
    canny_img = feature.canny(img, **params)
    return canny_img


