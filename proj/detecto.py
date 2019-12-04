import cv2
import numpy as np
from matplotlib import pyplot as plt

grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def detecto():
    global grid
    #***** cell one *****
    bgr_img = cv2.imread('thresh1.png')  # read as it is

    if bgr_img.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img)  # get b,g,r
        rgb_img = cv2.merge([r, g, b])  # switch it to rgb
        gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = bgr_img

    img = cv2.medianBlur(gray_img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        print(len(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[0][0] == 0:
            grid[0][0] = 'o'
            print(grid)

        #plt.subplot(121), plt.imshow(rgb_img)
        #plt.title('Input Image1'), plt.xticks([]), plt.yticks([])
        #plt.subplot(122), plt.imshow(cimg)
        #plt.title('Hough Transform1'), plt.xticks([]), plt.yticks([])
        #plt.show()

    #******** cell two *************
    bgr_img2 = cv2.imread('thresh2.png')  # read as it is

    if bgr_img2.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img2)  # get b,g,r
        rgb_img2 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img2 = cv2.cvtColor(bgr_img2, cv2.COLOR_BGR2GRAY)
    else:
        gray_img2 = bgr_img2

    img2 = cv2.medianBlur(gray_img2, 5)
    cimg2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    circles2 = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles2 is not None:
        circles2 = np.uint16(np.around(circles2))
        print(len(circles2))
        for i in circles2[0, :]:
            # draw the outer circle
            cv2.circle(cimg2, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg2, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[0][1] == 0:
            grid[0][1] = 'o'
            print(grid)

        # plt.subplot(121), plt.imshow(rgb_img6)
        # plt.title('Input Image6'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(cimg6)
        # plt.title('Hough Transform6'), plt.xticks([]), plt.yticks([])
        # plt.show()

    #********* cell three *********
    bgr_img3 = cv2.imread('thresh3.png')  # read as it is

    if bgr_img3.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img3)  # get b,g,r
        rgb_img3 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img3 = cv2.cvtColor(bgr_img3, cv2.COLOR_BGR2GRAY)
    else:
        gray_img3 = bgr_img3

    img3 = cv2.medianBlur(gray_img3, 5)
    cimg3 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)

    circles3 = cv2.HoughCircles(img3, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles3 is not None:
        circles3 = np.uint16(np.around(circles3))
        print(len(circles3))
        for i in circles3[0, :]:
            # draw the outer circle
            cv2.circle(cimg3, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg3, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[0][2] == 0:
            grid[0][2] = 'o'
            print(grid)

    #****** cell four ********
    bgr_img4 = cv2.imread('thresh4.png')  # read as it is

    if bgr_img4.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img4)  # get b,g,r
        rgb_img4 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img4 = cv2.cvtColor(bgr_img4, cv2.COLOR_BGR2GRAY)
    else:
        gray_img4 = bgr_img4

    img4 = cv2.medianBlur(gray_img4, 5)
    cimg4 = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)

    circles4 = cv2.HoughCircles(img4, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles4 is not None:
        circles4 = np.uint16(np.around(circles4))
        print(len(circles4))
        for i in circles4[0, :]:
            # draw the outer circle
            cv2.circle(cimg4, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg4, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[1][0] == 0:
            grid[1][0] = 'o'
            print(grid)

    #******* cell five ********
    bgr_img5 = cv2.imread('thresh5.png')  # read as it is

    if bgr_img5.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img5)  # get b,g,r
        rgb_img5 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img5 = cv2.cvtColor(bgr_img5, cv2.COLOR_BGR2GRAY)
    else:
        gray_img5 = bgr_img5

    img5 = cv2.medianBlur(gray_img5, 5)
    cimg5 = cv2.cvtColor(img5, cv2.COLOR_GRAY2BGR)

    circles5 = cv2.HoughCircles(img5, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles5 is not None:
        circles5 = np.uint16(np.around(circles5))
        print(len(circles5))
        for i in circles5[0, :]:
            # draw the outer circle
            cv2.circle(cimg5, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg5, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[1][1] == 0:
            grid[1][1] = 'o'
            print(grid)

    #********* cell six ***********
    bgr_img6 = cv2.imread('thresh6.png')  # read as it is

    if bgr_img6.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img6)  # get b,g,r
        rgb_img6 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img6 = cv2.cvtColor(bgr_img6, cv2.COLOR_BGR2GRAY)
    else:
        gray_img6 = bgr_img6

    img6 = cv2.medianBlur(gray_img6, 5)
    cimg6 = cv2.cvtColor(img6, cv2.COLOR_GRAY2BGR)

    circles6 = cv2.HoughCircles(img6, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        # print(circles)
    if circles6 is not None:
        circles6 = np.uint16(np.around(circles6))
        print(len(circles6))
        for i in circles6[0, :]:
            # draw the outer circle
            cv2.circle(cimg6, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg6, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[1][2] == 0:
            grid[1][2] = 'o'
            print(grid)

        #plt.subplot(121), plt.imshow(rgb_img6)
        #plt.title('Input Image6'), plt.xticks([]), plt.yticks([])
        #plt.subplot(122), plt.imshow(cimg6)
        #plt.title('Hough Transform6'), plt.xticks([]), plt.yticks([])
        #plt.show()

    #************ cell seven **********
    bgr_img7 = cv2.imread('thresh7.png')  # read as it is

    if bgr_img7.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img7)  # get b,g,r
        rgb_img7 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img7 = cv2.cvtColor(bgr_img7, cv2.COLOR_BGR2GRAY)
    else:
        gray_img7 = bgr_img7

    img7 = cv2.medianBlur(gray_img7, 5)
    cimg7 = cv2.cvtColor(img7, cv2.COLOR_GRAY2BGR)

    circles7 = cv2.HoughCircles(img7, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles7 is not None:
        circles7 = np.uint16(np.around(circles7))
        print(len(circles7))
        for i in circles7[0, :]:
            # draw the outer circle
            cv2.circle(cimg7, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg7, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[2][0] == 0:
            grid[2][0] = 'o'
            print(grid)

    #******** cell eight *************
    bgr_img8 = cv2.imread('thresh8.png')  # read as it is

    if bgr_img8.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img8)  # get b,g,r
        rgb_img8 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img8 = cv2.cvtColor(bgr_img8, cv2.COLOR_BGR2GRAY)
    else:
        gray_img8 = bgr_img8

    img8 = cv2.medianBlur(gray_img8, 5)
    cimg8 = cv2.cvtColor(img8, cv2.COLOR_GRAY2BGR)

    circles8 = cv2.HoughCircles(img8, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles8 is not None:
        circles8 = np.uint16(np.around(circles8))
        print(len(circles8))
        for i in circles8[0, :]:
            # draw the outer circle
            cv2.circle(cimg8, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg8, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[2][1] == 0:
            grid[2][1] = 'o'
            print(grid)

    #************ cell nine ************
    bgr_img9 = cv2.imread('thresh9.png')  # read as it is

    if bgr_img9.shape[-1] == 3:  # color image
        b, g, r = cv2.split(bgr_img9)  # get b,g,r
        rgb_img9 = cv2.merge([r, g, b])  # switch it to rgb
        gray_img9 = cv2.cvtColor(bgr_img9, cv2.COLOR_BGR2GRAY)
    else:
        gray_img9 = bgr_img9

    img9 = cv2.medianBlur(gray_img9, 5)
    cimg9 = cv2.cvtColor(img9, cv2.COLOR_GRAY2BGR)

    circles9 = cv2.HoughCircles(img9, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # print(circles)
    if circles9 is not None:
        circles9 = np.uint16(np.around(circles9))
        print(len(circles9))
        for i in circles9[0, :]:
            # draw the outer circle
            cv2.circle(cimg9, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg9, (i[0], i[1]), 2, (0, 0, 255), 3)
        if grid[2][2] == 0:
            grid[2][2] = 'o'
            print(grid)



detecto()