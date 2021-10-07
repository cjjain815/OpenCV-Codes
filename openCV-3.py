import cv2
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("WEBcam", grayFrame)
    cv2.moveWindow("WEBcam", 0, 0)
    if cv2.waitKey(1)&0xff == ord('q'):
        break
cam.release()