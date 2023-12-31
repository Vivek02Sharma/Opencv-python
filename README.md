# Opencv-python

OpenCV (Open Source Computer Vision) is an open-source computer vision and machine learning library that provides various tools and functions for image and video processing. The `opencv-python` module is the Python interface to OpenCV, allowing developers to use OpenCV functionalities in Python scripts.

## Installation

You can install `opencv-python` using the following pip command:

```bash
pip install opencv-python
```

## Example : 

```import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading the image using opencv
image = cv2.imread("img.jpg",-1)
image = cv2.resize(image,(500,500))
cv2.imshow("Image Window",image)
cv2.waitKey(0) #input is milliseconds,0 means infinite
cv2.destroyAllWindows()
```
## Output :

![image](https://github.com/Vivek02Sharma/Opencv-python/assets/112774647/7d450415-b09f-459e-a502-53d91cfeb724)


## Key Functions and Concepts in OpenCV

1. **cv2.imread():** Loads an image from a file.
2. **cv2.cvtColor():** Converts an image from one color space to another.
3. **cv2.imshow():** Displays an image in a window.
4. **cv2.imwrite():** Saves an image to a file.
5. **cv2.VideoCapture():** Captures video from a camera or a file.
6. **cv2.Canny():** Applies the Canny edge detector.
7. **cv2.findContours():** Finds contours in a binary image.
8. **cv2.drawContours():** Draws contours on an image.
9. **cv2.resize():** Resizes an image.
10. **cv2.threshold():** Applies a fixed-level threshold to an image.

#### For more details you can visit `opencv-python` documentation [opencv-python](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html).

