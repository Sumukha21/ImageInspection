import skimage
import numpy as np

def hogFeats(img, params={visualise=True}):
    hog_img, bin_edges = skimage.feature.hog(img, **params)
    return hog_img

def cannyEdge(img, params=None):
    canny_img = skimage.feature.canny(img, params)
    return canny_img


