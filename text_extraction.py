# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

def getTextOverlay(input_image):

    # Write your code here for output

    kernel = np.ones((7,7),np.uint8)

    # convert to grayscale
    gray = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
    
    # do gaussian blur to remove noise
    blur = cv2.GaussianBlur(gray,(9,9),0)

    # threshold the image
    rt,th1 = cv2.threshold(blur,4,255,cv2.THRESH_BINARY)


    # Remove noise

    opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)

    #closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    
    return opening
   

if __name__ == '__main__':
    image = cv2.imread('/home/dell/Downloads/simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################
