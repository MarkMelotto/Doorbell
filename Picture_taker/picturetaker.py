import cv2
# initialize the camera

def take_a_picture_with_preview():

    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        # namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("cam-test",img)
        cv2.waitKey(0)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("../Pictures/current picture.jpg",img) #save image
        return True
    return False

def take_a_picture():

    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        # namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        # cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
        cv2.imwrite("../Pictures/current picture.jpg",img) #save image
        return True
    return False

def return_a_picture():

    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        return img
    return False

if __name__=="__main__":
    # take_a_picture_with_preview()
    take_a_picture()