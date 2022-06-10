'''
https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
'''

import cv2
import numpy as np

def facial_recognition(img):
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
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

def show_face_from_picure(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_fontalface.xml')
    # Read the input image
    # img = cv2.imread('test_image.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # face = img.copy()

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        # face = np.array((w, h, 3))
        face = img[y:y+w, x:x+h]
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
    # Display the output
    cv2.imshow('img', face)
    cv2.waitKey()

def save_face_from_picure(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_fontalface.xml')
    # Read the input image
    # img = cv2.imread('test_image.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # face = img.copy()

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        # face = np.array((w, h, 3))
        face = img[y:y+w, x:x+h]
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
    # Display the output
    cv2.imwrite("../Pictures/faces/current_face.jpg",face) #save image

def test_save_face_from_picure(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_fontalface.xml')
    # Read the input image
    # img = cv2.imread('test_image.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # face = img.copy()

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        # face = np.array((w, h, 3))
        face = img[y:y+w, x:x+h]
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
    # Display the output
    cv2.imwrite("../Pictures/faces/test_1.jpg",face) #save image


if __name__ == "__main__":
    img = cv2.imread('test_image.jpg')
    # facial_recognition(img)
    # show_face_from_picure(img)
    test_save_face_from_picure(img)