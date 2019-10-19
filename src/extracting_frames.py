import cv2

def get_image():
    cap = cv2.VideoCapture(0)
    while 1:
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('frame', frame)
            cv2.imwrite(filename='.data/output_images/me.jpg', img=frame)
        q = cv2.waitKey(1)
        if q == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()