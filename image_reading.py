import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading the image using opencv
image = cv2.imread("img.jpg",-1)
cv2.imshow("Image Window",image)
cv2.waitKey(0) #input is milliseconds,0 means infinite
cv2.destroyAllWindows()

#reading the image using matplotlib
# image = cv2.imread("img.jpg")
# plt.imshow(image)
# plt.waitforbuttonpress()
# plt.close('all')

#resize,rotate and saving the image
# image = cv2.imread("img.jpg",0)
# image = cv2.resize(image,(500,600))
# image = cv2.rotate(image,cv2.ROTATE_180)
# cv2.imwrite("imgcopy.jpg",image)
# cv2.imshow("Image Window",image)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()






