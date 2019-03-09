import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('.\CV project\switch.jpg')
#img = cv2.imread('./edgedetected.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayimage',gray)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
#cv2.imshow('edgesimage',edges)
minLineLength=img.shape[1]-300
lines = cv2.HoughLinesP(image=edges,rho=0.02,theta=np.pi/500,    
    threshold=10,lines=np.array([]),                                 
    minLineLength=minLineLength, maxLineGap=100)
a,b,c = lines.shape

for i in range(a):
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2],
        lines[i][0]   [3]), (0, 0, 255), 3, cv2.LINE_AA)
cv2.imwrite('houghlines3.jpg',edges)
winname = "Test"
cv2.namedWindow(winname,0) # Create a named window
cv2.resizeWindow(winname,800,600);  # Move it to (40,30)
cv2.imshow(winname, edges)
cv2.waitKey(10000)
