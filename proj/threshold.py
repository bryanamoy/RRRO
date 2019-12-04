# Python programe to illustrate
# simple thresholding type on an image

# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.imread('firstbox.png') #1st box
image1 = cv2.resize(image1, (600, 600))

image2 = cv2.imread('secondbox.png') #2nd box
image2 = cv2.resize(image2, (600, 600))

image3 = cv2.imread('thirdbox.png') #3rd box
image3 = cv2.resize(image3, (600, 600))

image4 = cv2.imread('fourthbox.png') #4th box
image4 = cv2.resize(image4, (600, 600))

image5 = cv2.imread('fifthbox.png') #5th box
image5 = cv2.resize(image5, (600, 600))

image6 = cv2.imread('sixthbox.png') #6th box
image6 = cv2.resize(image6, (600, 600))

image7 = cv2.imread('seventhbox.png') #7th box
image7 = cv2.resize(image7, (600, 600))

image8 = cv2.imread('eigthbox.png') #8th box
image8 = cv2.resize(image8, (600, 600))

image9 = cv2.imread('ninthbox.png') #9th box
image9 = cv2.resize(image9, (600, 600))

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
img5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
img6 = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)
img7 = cv2.cvtColor(image7, cv2.COLOR_BGR2GRAY)
img8 = cv2.cvtColor(image8, cv2.COLOR_BGR2GRAY)
img9 = cv2.cvtColor(image9, cv2.COLOR_BGR2GRAY)


# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
#ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

thresh1 = np.zeros(img.shape)
thresh1[img > 150] = 255

thresh2 = np.zeros(img2.shape)
thresh2[img2 > 150] = 255

thresh3 = np.zeros(img3.shape)
thresh3[img3 > 150] = 255

thresh4 = np.zeros(img4.shape)
thresh4[img4 > 150] = 255

thresh5 = np.zeros(img5.shape)
thresh5[img5 > 150] = 255

thresh6 = np.zeros(img6.shape)
thresh6[img6 > 150] = 255

thresh7 = np.zeros(img7.shape)
thresh7[img7 > 150] = 255

thresh8 = np.zeros(img8.shape)
thresh8[img8 > 150] = 255

thresh9 = np.zeros(img9.shape)
thresh9[img9 > 150] = 255


# ret, thresh4 = img[img > 128]
#ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
#cv2.imshow('Binary Threshold', thresh1)
#cv2.imshow('Binary Threshold Inverted', thresh2)
#cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('box 1', thresh1)
cv2.imwrite("thresh1.png", thresh1)

cv2.imshow('box 2', thresh2)
cv2.imwrite("thresh2.png", thresh2)

cv2.imshow('box 3', thresh3)
cv2.imwrite("thresh3.png", thresh3)

cv2.imshow('box 4', thresh4)
cv2.imwrite("thresh4.png", thresh4)

cv2.imshow('box5', thresh5)
cv2.imwrite("thresh5.png", thresh5)

cv2.imshow('box 6', thresh6)
cv2.imwrite("thresh6.png", thresh6)

cv2.imshow('box 7', thresh7)
cv2.imwrite("thresh7.png", thresh7)

cv2.imshow('box 8', thresh8)
cv2.imwrite("thresh8.png", thresh8)

cv2.imshow('box 9', thresh9)
cv2.imwrite("thresh9.png", thresh9)
#cv2.imshow('Set to 0 Inverted', thresh5)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()