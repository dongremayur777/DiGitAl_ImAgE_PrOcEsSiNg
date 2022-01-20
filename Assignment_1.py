import cv2
import numpy as np

org = cv2.imread('/Users/mayurdongre/Downloads/Rohit.jpeg')

imageHeight = len(org)
imageWidth = len(org[0])

gr = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

//Gray_Scale

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        gr[i][j] = int(org[i][j][0] * 0.2126 + org[i][j][1] * 0.7152 + org[i][j][2] * 0.0722)

b = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

//Binary

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        if gr[i][j] >= 127:
            b[i][j] = 255
        else:
            b[i][j] = 0

rb = np.zeros((imageHeight, imageWidth, 3), dtype=np.uint8)

//Constant_Added

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        rb[i][j] = org[i][j] + np.uint(20)

cv2.imshow('org', org)              //Original Image
cv2.imshow('gray', gr)              //GrayScale Image
cv2.imshow('binary', b)             //Binary Image
cv2.imshow('RGB + 20', rb)          //Constant_added_to_img
cv2.imshow('gray + binary',gr+b)    //I1+I2(Gray+Binary)
cv2.waitKey(0)
