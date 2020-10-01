import cv2
import numpy as np
 
img = cv2.imread('QUESTAO_02_Quadrados.jpg', 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
