from PIL import ImageGrab
import cv2
import numpy as np


def findCircles(img):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (1, 1))
    circles = cv2.HoughCircles(gray_blurred,  cv2.HOUGH_GRADIENT, 1.3,25)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        rgb_arr = [img[y,x,:] for (x,y,r) in circles]
        rgb_arr = np.array(rgb_arr)
        rgb_mean = np.mean(rgb_arr,axis=0)
        diff = abs(rgb_arr-rgb_mean)
        diff = np.sum(diff,axis=1)
        i = np.argmax(diff)
        c = circles[i]
        cv2.circle(img,(c[0],c[1]),c[2],(255,255,255),5)
        cv2.circle(img,(c[0],c[1]),2,(255,255,255),5)

    return img



while True:
    img_rgb = ImageGrab.grab()
    img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    img_bgr = img_bgr[190:960,750:1190]
    try:
        img_circle = findCircles(img_bgr)
    except:
        img_circle = img_bgr
    
    img_bgr = cv2.resize(img_bgr,(960,540))
    cv2.imshow('lyto', img_circle)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




