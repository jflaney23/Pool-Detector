from cgi import test
import cv2 as cv
import sys

img = cv.imread()
    

if img is None:
    sys.exit("Could not read image")

cv.imshow("Display window", img)
k = cv.waitkey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)