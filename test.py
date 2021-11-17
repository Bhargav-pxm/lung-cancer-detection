import numpy as np
import cv2
import pydicom
from skimage import data, exposure, img_as_float
filename = "dicom_dir/ID_0053_AGE_0073_CONTRAST_0_CT.dcm"
ds = pydicom.read_file(filename)
image = ds.pixel_array
image = exposure.equalize_adapthist(image)
cv2.imwrite("test.png",image*255)
cv2.imshow("dicom", image)
cv2.waitKey(0)
