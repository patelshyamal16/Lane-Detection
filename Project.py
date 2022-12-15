# University of Illinois at Chicago
# ECE 415
# Term Project- Lane Detection
# Name: Shyamal Patel and Shaikh Haque

import cv2
import numpy as np

line = 0

img = cv2.imread('Image/Test1.jpg')
cv2.imshow("Original Image", img)
cv2.waitKey(2)

height = img.shape[0]
width = img.shape[1]
edges_lines_vertices = [(0, height), (width / 2, height / 2), (width, height)]

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Grayscale", gray)
cv2.waitKey(3)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Image with edge detection", edges)
cv2.waitKey(4)

ver = np.array([edges_lines_vertices], np.int32),
mask = np.zeros_like(edges)
cv2.fillPoly(mask, ver, 255)
mask = cv2.bitwise_and(edges, mask)

cv2.imshow("Image with lane edge detection", mask)
cv2.waitKey(6)

lines = cv2.HoughLinesP(mask, 6, np.pi / 180, 160, np.array([]), 40, 25)

image_with_lines = np.copy(img)
edges_line = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

while line < len(lines):
    for x1, y1, x2, y2 in lines[line]:
        cv2.line(edges_line, (x1, y1), (x2, y2), (255, 255, 0), 10)
    line += 1

Lane_lines = cv2.addWeighted(img, 0.8, edges_line, 1, 0.0)

cv2.imshow("Original Image with lanes lines", Lane_lines)
cv2.waitKey(0)
