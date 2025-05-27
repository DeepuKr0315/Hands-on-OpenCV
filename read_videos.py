import cv2 as cv

capture = cv.VideoCapture('Videos/2436088-uhd_3840_2160_25fps.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()