from skimage import feature
import numpy as np
import math

def hogFeats(img, params=None):
    #print("Image inside hogFeats: ", img.shape, type(img))
    #print("Image : ", img)
   # img = np.reshape(img, (math.ceil(math.sqrt(len(img))), :))
    hog_img, bin_edges = feature.hog(img, **params) # visualize=True)
    return hog_img

def cannyEdge(img, params=None):
    canny_img = feature.canny(img, **params)
    return canny_img


