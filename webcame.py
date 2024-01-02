import cv2

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    img = cv2.flip(frame,1)
    img = cv2.putText(img,"Press (Q) to quite",(10,455),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1,cv2.LINE_AA)
    cv2.imshow("Video Windows",img)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

