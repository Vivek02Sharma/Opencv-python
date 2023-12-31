import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    width = int(video.get(3))
    height = int(video.get(4))
    container = np.zeros(frame.shape,np.uint8)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    container[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    container[height//2:,:width//2] = smaller_frame
    container[:height//2,width//2:] = smaller_frame
    container[height//2:,width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    cv2.imshow("Video Windows",container)


    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

print(width,height)
