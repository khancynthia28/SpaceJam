import numpy as np
import argparse
import imutils
import cv2
from math import *
 
 # construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True, help="Path to template image")
ap.add_argument("-i", "--image", required=True,
help="Path to images where template will be matched")
args = vars(ap.parse_args())
 
# load the image image, convert it to grayscale, and detect edges
template = cv2.imread(args["template"])
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
#cv2.imshow("Template", template)
# loop over the images to find the template in
# load the image, convert it to grayscale, and initialize the
# bookkeeping variable to keep track of the matched region
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
found = None
 
# loop over the scales of the image
for scale in np.linspace(0.2, 1.0, 20)[::-1]:
	# resize the image according to the scale, and keep track
	# of the ratio of the resizing
	resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
	r = gray.shape[1] / float(resized.shape[1])
 
	# if the resized image is smaller than the template, then break
	# from the loop
	if resized.shape[0] < tH or resized.shape[1] < tW:
		break
		# detect edges in the resized, grayscale image and apply template
	# matching to find the template in the image
	edged = cv2.Canny(resized, 50, 200)
	result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
	(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

	# if we have found a new maximum correlation value, then update
	# the bookkeeping variable
	if found is None or maxVal > found[0]:
		found = (maxVal, maxLoc, r)
# unpack the bookkeeping variable and compute the (x, y) coordinates
# of the bounding box based on the resized ratio
(_, maxLoc, r) = found
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
 
# draw a bounding box around the detected result and display the image
switch_height = sqrt( (startX - startX)**2 + (endY - startY)**2 )
switch_width = sqrt( (endX - startX)**2 + (startY - startY)**2 )
print("switch height and switch width are ",switch_height,switch_width)
text = "Height:"+str(switch_height)+" Width:"+str(switch_width)
cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(image,text,(int(startX)-400,int(endY)-100), font, 2,(255,255,255),2,cv2.LINE_AA)
winname = "Test"
cv2.namedWindow(winname,0) # Create a named window
cv2.resizeWindow(winname,800,600);  # Move it to (40,30)
cv2.imshow(winname, image)
cv2.waitKey(10000)
