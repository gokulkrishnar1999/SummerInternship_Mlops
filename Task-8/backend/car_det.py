#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp
import cgi
import os
import time
import matplotlib.pyplot as plt
import cv2
import imutils 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


form = cgi.FieldStorage()
Vid = form.getvalue("my1")


lic_data = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def plt_show(image, title="", gray = False, size = (100, 100)):
    temp = image 
    if gray == False:
        temp = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
        plt.title(title) 
        plt.imshow(temp, cmap='gray') 
        plt.show()

def detect_number(img):
    temp = img 
    gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    number = lic_data.detectMultiScale(img,1.2)
#     print("number plate detected: "+str(len (number)))
    for numbers in number:
        (x,y,w,h) = numbers 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+h]
        cv2.rectangle(temp, (x,y) , (x+w,y+h), (0,255,0), 3)
#     plt_show(temp)

import cv2

cap = cv2.VideoCapture(Vid)
car_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

while True:    
    ret, img = cap.read()
    #Take input of car image with number plate 
    if img is None:
        cv2.destroyAllWindows()
        break
    detect_number(img)
    
    image = img 
    ratio = image.shape[0]/500.0 
    orig = image.copy 
    image = imutils.resize(image, height = 500)
    # convert the image to grayscale, blur it, and find edges # in the image 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny (gray, 75, 200)
    # show the original image and the edge detected image print("STEP 1: Edge Detection")
    cv2.imshow('vid', image)
    k = cv2.waitKey(27)
    if k == 27:
        cv2.destroyAllWindows()
        break
    
    contours = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse = True)[:10] 
    screenCnt = None
    
    for c in contours:
    # approximate the contour 
        peri = cv2.arcLength(c, True) 
        approx = cv2.approxPolyDP(c, 0.018 * peri, True) 
        # if our approximated contour has four points, then # we can assume that we have found our screen 
        if len(approx) == 4:
            screenCnt = approx
            break
    
    if screenCnt is None:
        detected = 0
        print ("No contour detected")
    else:
        detected = 1
    if detected == 1:
        cv2.drawContours (img, (screenCnt), -1, (0, 0, 255), 3)
        # Masking the part other than the number plate 
        import numpy as np
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [screenCnt],0,255,-1) 
        # Now crop 
        (x, y) = np.where(mask == 255) 
        (topx, topy) = (np.min(x), np.min(y)) 
        (bottomx, bottomy) = (np.max(x), np.max(y)) 
        Cropped = gray[topx: bottomx+1, topy: bottomy+1]
        plt.imshow(Cropped, cmap = 'gray');
        
        #Read the number plate
        num = pytesseract.image_to_string(Cropped, config='..psm 11')
        

if num == "MH01CT8454"
	list = ["Name : Anil Kapoor",
	"Vehicle No. : AP31CG3600",
	"Address : Suncity-36",
	"City : Madurai",
	"Mobile No. : 7898787754",
	"Registration Date : 15/9/2006"]

	for i in list:
		print(i)
elif :
	print("Record Not Found!!!")