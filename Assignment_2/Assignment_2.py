import cv2
import numpy as np

org = cv2.imread('/Users/mayurdongre/Downloads/Rohit.jpeg')

imageHeight = len(org)
imageWidth = len(org[0])

gr = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth): 
        gr[i][j] = int(org[i][j][0] * 0.2126 + org[i][j][1] * 0.7152 + org[i][j][2] * 0.0722)

sb = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        sb[i][j] = int(org[i][j][0] * 0.2126 + org[i][j][1] * 0.7152 + org[i][j][2] * 0.0722)

for i in range(200, imageHeight-200):
    for j in range(200, imageWidth-200):
        sb[i][j] = int(org[i][j][0] * 0 + org[i][j][1] * 0 + org[i][j][2] * 0)


cv2.imshow('org', org)              
cv2.imshow('gray', gr)
cv2.imshow('some_black', sb)  
cv2.imshow('sub',gr-sb)            
cv2.waitKey(0)