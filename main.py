import skimage
import numpy as np
from featureExtractors import *

def staticMain(img_bin, feature_extractor_params={}):
    """
    params:
        img_bin : type- binary string.
                 Image in binary string format
        feature_extractor : type- Dictionary
                            Feature wise params
                            Ex : {'Hog' : {**params}}
    """
    img = np.fromstring(img_bin)
    for feature in list(feature_extractor_params.keys()):
        if feature.lower() == 'hog':
            print("Extractng Histogram of Oriented Gradients features")
            hog_features = hofFeats(img, feature_extractor_params[feature])
            return hog_features
        elif feature.lower() == 'canny':
            print("Extracting Canny edge features")
            canny_edges = cannyEdge(img, feature_extractor_params[feature])
            return canny_edges


