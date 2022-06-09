'''
https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
'''

import cv2

def facial_reqocnition(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_fontalface.xml')
    # Read the input image
    # img = cv2.imread('test_image.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

if __name__ == "__main__":
    img = cv2.imread('test_image.jpg')
    facial_reqocnition(img)