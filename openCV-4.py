import cv2
cam = cv2.VideoCapture(0)
while True:
    _, originalFrame = cam.read()
    grayFrame = cv2.cvtColor(originalFrame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("CAM-1", originalFrame)
    cv2.imshow("CAM-2", grayFrame)
    cv2.imshow("CAM-3", grayFrame)
    cv2.imshow("CAM-4", originalFrame)
    cv2.moveWindow("CAM-1" , 0, 0)
    cv2.moveWindow("CAM-2" , 640, 0)
    cv2.moveWindow("CAM-3" , 0, 480)
    cv2.moveWindow("CAM-4" , 640, 480)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()