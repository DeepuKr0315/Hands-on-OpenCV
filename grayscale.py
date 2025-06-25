import cv2 as cv

img = cv.imread('Photos/Golden-Retriever.jpg')
cv.imshow('Golden Retriever', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Blur the image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT) # here 5 is the kernel size, must be odd, can be 3, 7, etc.
cv.imshow("Blurred Image", blur)

# Edge cascade
edges = cv.Canny(img, 125, 175) # lower and upper threshold
cv.imshow("Edges", edges)

edges_blur = cv.Canny(blur, 125, 175)
cv.imshow("Blurred Edges", edges_blur)

# Dilating the image
dilated = cv.dilate(edges, (3, 3), iterations=1) # (3, 3) is the kernel size, iterations is how many times to dilate
cv.imshow("Dilated Edges", dilated)

dilated_blur = cv.dilate(edges_blur, (3, 3), iterations=1)
cv.imshow("Dilated Blurred Edges", dilated_blur)

# Eroding the image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded Edges", eroded)

eroded = cv.erode(dilated, (3, 3), iterations=10)
cv.imshow("Eroded Edges 10 iterations", eroded)

# Resize the image
resized = cv.resize(img, (500, 500)) # resizing to 500x500 pixels
cv.imshow("Resized Image", resized)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) # using area interpolation
cv.imshow("Resized Image with INTER_AREA", resized)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # using cubic interpolation
cv.imshow("Resized Image with INTER_CUBIC", resized)

# Cropping the image
cropped = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)