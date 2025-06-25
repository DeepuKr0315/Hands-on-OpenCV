import cv2 as cv

image = cv.imread('Photos/Golden-Retriever.jpg')
cv.imshow('Golden Retriever', image)

def rescale_frame(frame, scale=0.25):
    # For images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Rescaled Image', rescale_frame(image, scale=0.2))
# Read video
capture = cv.VideoCapture('Videos/2436088-uhd_3840_2160_25fps.mp4')

def change_resolution(width, height):
    # Only work for live videos
    capture.set(3, width)  # Width
    capture.set(4, height)



while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  # Exit loop if frame not read successfully

    frame_resized = rescale_frame(frame, scale=0.2)
    cv.imshow('Original Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
print("Opened?", capture.isOpened())