import cv2
import numpy as np
import math
img = cv2.imread("thresh4.png")
img = cv2.resize(img, (600, 600))
# Taking a matrix of size 5 as the kernel #geeksforgeeks
kernel = np.ones((1, 1), np.uint8)
img_dilation = cv2.dilate(img, kernel, iterations=1)

gray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=100)
slopes = []
findx = False
for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
   slope = (y2-y1) / (x2-x1)
   slopes.append(slope)
   #print(x1, y1, x2, y2)
for s in slopes:
   for j in slopes:
      angle = math.atan((s-j)/(1+(s*j)))
      angle = math.degrees(angle)
      angle = abs(angle)
      print(angle)

#cv2.imshow("linesEdges", edges)
#print(len(lines))
cv2.imshow("linesDetected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()