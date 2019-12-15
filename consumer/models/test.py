import numpy as np
import cv2
from feature_extractors import *
from feature_extractor_main import *

img_path = '/home/sumukha/Downloads/brain.jpeg'

img = cv2.imread(img_path, -1)
print("Image : ", img)

img_str = np.ndarray.tobytes(img)
print("Image string : ", img_str)

hog_features = staticMain(img_str, {"Hog":{}})
print("Hog Features : ", hog_features)

