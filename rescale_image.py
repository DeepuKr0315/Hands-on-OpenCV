import cv2 as cv

def rescale_frame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read video
capture = cv.VideoCapture('Videos/2436088-uhd_3840_2160_25fps.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  # Exit loop if frame not read successfully

    frame_resized = rescale_frame(frame)
    cv.imshow('Original Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
print("Opened?", capture.isOpened())