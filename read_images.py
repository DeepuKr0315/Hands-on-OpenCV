import cv2 as cv

img = cv.imread('Photos/Unknown.jpeg')
cv.imshow('Cat', img)
cv.waitKey(0)