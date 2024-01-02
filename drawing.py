import cv2
import numpy as np

img = np.zeros((500,500,3),dtype='uint8')
img[10:200,10:200] = 255,0,0
img = cv2.rectangle(img,(10,10),(200,200),(0,255,0),2)
img = cv2.circle(img,(img.shape[0]//2,img.shape[1]//2),50,(0,0,255),2)
img = cv2.line(img,(250,250),(350,350),(200,23,0),2)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
