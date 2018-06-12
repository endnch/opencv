import cv2
import numpy as np

# img = cv2.imread('e.png')
# img = cv2.imread('f.png')
# img = cv2.imread('test.jpg')
img = cv2.imread('p.jpg')
height, width, channels = img.shape

def step1():
	for i in range(0, height, 2):
		img[[i, i + 1]] = img[[i + 1, i]]

	for i in range(0, width, 2):
		img[:, [i, i + 1]] = img[:, [i + 1, i]]
	
def step2():
	img[:, [0, width - 1]] = img[:, [width - 1, 0]]

	for i in range(1, width - 1, 2):
		img[:, [i, i + 1]] = img[:, [i + 1, i]]

	for i in range(0, height, 2):
		img[[i, i + 1]] = img[[i + 1, i]]

def blur():
	step1()
	step2()

def unblur():
	step2()
	step1()

gen = np.array(img, dtype = np.uint8)

def nothing(x):
    pass

WINDOW_NAME   = 'Proyecto'
TRACKBAR_NAME = 'Presiona Z para realizar n reps\nA para deshacer n reps\nX para realizar el paso1\nS para realizar el paso2'

cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TRACKBAR_NAME, WINDOW_NAME, 1, 500, nothing)

ESC = 27

while(1):
    cv2.imshow(WINDOW_NAME, gen)
    k = cv2.waitKey(1) & 0xFF
    if k == ESC:
        break
    else:
    	s = cv2.getTrackbarPos(TRACKBAR_NAME, WINDOW_NAME)
    	if k == ord('z'):
    		for i in range(s):
    			blur()
    	elif k == ord('a'):
    		for i in range(s):
    			unblur()
    	elif k == ord('x'):
    		step1()
    	elif k == ord('s'):
    		step2()
    	gen = np.array(img, dtype = np.uint8)

cv2.destroyWindow(WINDOW_NAME)


