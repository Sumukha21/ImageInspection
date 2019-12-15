import skimage
import io
from PIL import Image
import numpy as np
from models.feature_extractors import *

def staticMain(img_bin, feature_extractor_params={}):
    """
    params:
        img_bin : type- binary string.
                 Image in binary string format
        feature_extractor : type- Dictionary
                            Feature wise params
                            Ex : {'Hog' : {**params}}
    """
    img = np.array(Image.open(io.BytesIO(img_bin)))
    for feature in list(feature_extractor_params.keys()): 
        parameters = feature_extractor_params[feature]
        if parameters:
            if feature.lower() == 'hog':
                print("Extractng Histogram of Oriented Gradients features")
                hog_features = hogFeats(img, feature_extractor_params[feature])
                return hog_features
            elif feature.lower() == 'canny':
                print("Extracting Canny edge features")
                canny_edges = cannyEdge(img, feature_extractor_params[feature])
                return canny_edges
        else: 
            if feature.lower() == 'hog':
                print("Extractng Histogram of Oriented Gradients features")
                hog_features = hogFeats(img)
                return hog_features
            elif feature.lower() == 'canny':
                print("Extracting Canny edge features")
                canny_edges = cannyEdge(img)
                return canny_edges

