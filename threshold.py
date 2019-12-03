# Python programe to illustrate
# simple thresholding type on an image

# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.imread('fifthbox.png')
image1 = cv2.resize(image1, (600, 600))
image2 = cv2.imread('firstbox.png')
image2 = cv2.resize(image2, (600, 600))
image3 = cv2.imread('sixthbox.png')
image3 = cv2.resize(image3, (600, 600))

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)


# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
#ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)

thresh4 = np.zeros(img.shape)
thresh4[img > 150] = 255

cir = np.zeros(img2.shape)
cir[img2 > 165] = 255

thresh6 = np.zeros(img3.shape)
thresh6[img3 > 165] = 255


# ret, thresh4 = img[img > 128]
#ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
#cv2.imshow('Binary Threshold', thresh1)
#cv2.imshow('Binary Threshold Inverted', thresh2)
#cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imwrite("thresh4.png", thresh4)
cv2.imshow('set zero', cir)
cv2.imwrite("cir.png", cir)
cv2.imshow('set zero', thresh6)
cv2.imwrite("thresh6.png", thresh6)
#cv2.imshow('Set to 0 Inverted', thresh5)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()