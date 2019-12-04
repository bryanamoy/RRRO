import cv2
import numpy as np
import math

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def detectx():
    global grid
    #*********** cell one ***********
    img1 = cv2.imread("thresh1.png")
    img1 = cv2.resize(img1, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img1, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 1")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img1, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[0][0] == 0:
            grid[0][0] = 'x'
            print(grid)
    cv2.imshow("linesDetected1", img1)
    #************ cell two ***********
    img2 = cv2.imread("thresh2.png")
    img2 = cv2.resize(img2, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img2, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 2")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img2, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[0][1] == 0:
            grid[0][1] = 'x'
            print(grid)
    cv2.imshow("linesDetected2", img2)
    #************ cell three **********
    img3 = cv2.imread("thresh3.png")
    img3 = cv2.resize(img3, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img1, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 3")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img3, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[0][2] == 0:
            grid[0][2] = 'x'
            print(grid)
    cv2.imshow("linesDetected3", img3)
    #************ cell four ***********
    img4 = cv2.imread("thresh4.png")
    img4 = cv2.resize(img4, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img4, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 4")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img4, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[1][0] == 0:
            grid[1][0] = 'x'
            print(grid)
    cv2.imshow("linesDetected4", img4)
    # *********** cell five ***********
    img = cv2.imread("thresh5.png")
    img = cv2.resize(img, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 5")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[1][1] == 0:
            grid[1][1] = 'x'
            print(grid)

    # cv2.imshow("linesEdges", edges)
    # print(len(lines))
    cv2.imshow("linesDetected5", img)
    #********** cell six **************
    img6 = cv2.imread("thresh6.png")
    img6 = cv2.resize(img6, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img6, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 6")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img6, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[1][2] == 0:
            grid[1][2] = 'x'
            print(grid)
    cv2.imshow("linesDetected6", img6)
    #************ cell seven *********
    img7 = cv2.imread("thresh7.png")
    img7 = cv2.resize(img7, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img7, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 7")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img7, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[2][0] == 0:
            grid[2][0] = 'x'
            print(grid)
    cv2.imshow("linesDetected7", img7)
    #********* cell 8 *************
    img8 = cv2.imread("thresh8.png")
    img8 = cv2.resize(img8, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img8, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 8")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img8, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[2][1] == 0:
            grid[2][1] = 'x'
            print(grid)
    cv2.imshow("linesDetected8", img8)
    #********** cell nine **********
    img9 = cv2.imread("thresh9.png")
    img9 = cv2.resize(img9, (600, 600))
    # Taking a matrix of size 5 as the kernel #geeksforgeeks
    kernel = np.ones((1, 1), np.uint8)
    img_dilation = cv2.dilate(img9, kernel, iterations=1)

    gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    slopes = []
    findx = False
    print("cell 9")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img9, (x1, y1), (x2, y2), (0, 0, 128), 1)
        if (x2 - x1) > 0:
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        # print(x1, y1, x2, y2)
    for s in slopes:
        if findx == True:
            break
        for j in slopes:
            angle = math.atan((s - j) / (1 + (s * j)))
            angle = math.degrees(angle)
            angle = abs(angle)  # if angle >60 or <120 there is an x
            print(angle)
            if angle >= 60 and angle <= 120:
                findx = True
                break
    if findx == True:
        if grid[2][2] == 0:
            grid[2][2] = 'x'
            print(grid)
    cv2.imshow("linesDetected9", img9)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


detectx()
