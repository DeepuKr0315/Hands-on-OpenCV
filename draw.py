import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# Paint the image a acertain color
blank[:] = 0, 255, 0  # Green color
cv.imshow("Green", blank)

blank[:] = 0, 0, 255 # Red color
cv.imshow("Red", blank)

blank[200:300, 300:400] = 255, 0, 0  # Blue square
cv.imshow("Blue Square", blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=2)
cv.imshow("Rectangle", blank)

cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow("Filled Rectangle with thickness=-1 method", blank)
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
cv.imshow("Filled Rectangle with FILLED method", blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness=-1)
cv.imshow("One forth Green Rectangle", blank)

# Draw a circle
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=5)
cv.imshow("Circle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow("Filled Circle", blank)

# Draw a line
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.line(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=50)
cv.imshow("Line", blank)

# Write text on the image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.putText(blank, "Hello, OpenCV!", (50, 250), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)