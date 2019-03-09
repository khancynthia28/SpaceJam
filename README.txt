Project: Space Jam

Team:
Srilekha Divyakolu
Cynthia Khan

Platforms:
Python 3.6
MATLAB2018

Modules to install for python:
AWS CLI 
numpy
boto3
pyttsx3
argparse
imutils
opencv-python

Modules:
Classification modules:
	cv.py - for classification of room based on objects in it, used aws rekognition api
Dimensionality core modules:
	switch_template.py - for template matching and to get outlet label or switch board height and width in pixels
	edge_detection.py - for edge detection of the image
	edgedetection.m - matlab file used for joining small edges with gaps to form one straight edge
	line_detection.m - to detect lines from the outputs of edge_detection.py,edgedetection.m and switch_template.py and measure actual dimensions using proportionality
	
Dimensionality Supporting modules:
	lineseg.m, maxlinedev.m, edgelink.m, findendsjunctions.m, drawedgelist.m are submodules used by edgedetection.m to join small edges to large edges

How to run:
To run
cv.py 
1. first install aws cli and configure it
and in command-prompt, run python cv.py imagePath

To run switch_template.py
use the following command-prompt after going to files folder
python .\switch_template.py --template '.\CV project\switch_1.jpg' --image '.\CV project\switch.jpg'
output will be as in fig 2 in report and text as follows
switch height and switch width are  59.0 40.0

To run edge_detection.py
python edge_detection.py
output will save an image with edges detected and saved as "houghlines3.jpg" and shown 

To run edgedetection.m
just run edgedetection.m in MATLAB2018, this will save an image in the name edgedetected.jpg

To line_detection.m
just run line_detection.m in MATLAB2018, code has inputs from edgedetection.m, edge_detection.py and switch_template.py and also real measurements
The output will be as follows
in pixels room height: 943.1357 and width: 1371.2607
in inches height: 5.4331 and width: 3.5827
in pixels height: 59 and width: 40
in inches observed room height: 86.8495 and width: 126.2738
in inches real room height: 98.8976 and width: 157.2441
error in % for room height: 12.1824 and width: 19.6956
 