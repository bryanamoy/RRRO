# Python programe to illustrate 
# corner detection with 
# Harris Corner Detection Method 

# organizing imports 
import cv2
import numpy as np

# path to input image specified and
# image is loaded with imread command
image = cv2.imread('grid2.jpg')
image = cv2.resize(image, (600, 600))

firstBox = image[80:204, 25:196] #[y, x]
cv2.imshow("0,0", firstBox)
cv2.imwrite("firstbox.png", firstBox)

secondBox = image[80:202, 220:378] #[y, x]
cv2.imshow("0,1", secondBox)
cv2.imwrite("secondbox.png", secondBox)

thirdBox = image[80:200, 401:572] #[y, x]
cv2.imshow("0,2", thirdBox)
cv2.imwrite("thirdbox.png", thirdBox)

fourthBox = image[227:344, 30:195] #[y, x]
cv2.imshow("1,0", fourthBox)
cv2.imwrite("fourthbox.png", fourthBox)

fifthBox = image[230:335, 230:380]
cv2.imshow("1,1", fifthBox)
cv2.imwrite("fifthbox.png", fifthBox)

sixthBox = image[220:338, 410:572]
cv2.imshow("1,2", sixthBox)
cv2.imwrite("sixthbox.png", sixthBox)

seventhBox = image[367:502, 25:197]
cv2.imshow("2,0", seventhBox)
cv2.imwrite("seventhbox.png", seventhBox)

eigthBox = image[365:500, 223:385]
cv2.imshow("2,1", eigthBox)
cv2.imwrite("eigthbox.png", eigthBox)

ninthBox = image[361:500, 415:587]
cv2.imshow("2,2", ninthBox)
cv2.imwrite("ninthbox.png", ninthBox)

# convert the input image into
# grayscale color space
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# modify the data type
# setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

# Reverting back to the original image,
# with optimal threshold value
image[dest > 0.01 * dest.max()] = [0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', image)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows() 