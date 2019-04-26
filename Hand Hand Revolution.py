"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2
import pyautogui
import numpy as np
from time import sleep


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    detect_1 = False
    detect_2 = False
    detect_3 = False
    detect_4 = False
    while True:
        ret_val, img = cam.read()
        img = cv2.circle(img,(250,600), 63, (128,0,128), 4)
        img = cv2.circle(img,(500,600), 63, (128,0,128), 4)
        img = cv2.circle(img,(750,600), 63, (128,0,128), 4)
        img = cv2.circle(img,(1000,600), 63, (128,0,128), 4)
        color1, std = cv2.meanStdDev(img[600-64:600+64, 250-64:250+64])
        color2, std = cv2.meanStdDev(img[600-64:600+64, 500-64:500+64])
        color3, std = cv2.meanStdDev(img[600-64:600+64, 750-64:750+64])
        color4, std = cv2.meanStdDev(img[600-64:600+64, 1000-64:1000+64])
        print((color1, color2, color3, color4))
        cv2.imshow('my webcam', img)
        keypress = cv2.waitKey(1)
        if keypress == 27: 
            break  # esc to quit
        if keypress == 32: 
            break  # space to begin
    while True:
        ret_val, img = cam.read()
        # img = cv2.circle(img,(250,600), 63, (128,0,128), 4)
        # img = cv2.circle(img,(500,600), 63, (128,0,128), 4)
        # img = cv2.circle(img,(750,600), 63, (128,0,128), 4)
        # img = cv2.circle(img,(1000,600), 63, (128,0,128), 4)
        newcolor1, std = cv2.meanStdDev(img[600-64:600+64, 250-64:250+64])
        newcolor2, std = cv2.meanStdDev(img[600-64:600+64, 500-64:500+64])
        newcolor3, std = cv2.meanStdDev(img[600-64:600+64, 750-64:750+64])
        newcolor4, std = cv2.meanStdDev(img[600-64:600+64, 1000-64:1000+64])
        # print((newcolor1 - color1), (newcolor2 - color2), (newcolor3 - color3), (newcolor4 - color4))
        threshold = 100
        new_detect_1 = np.linalg.norm(newcolor1 - color1) > threshold
        new_detect_2 = np.linalg.norm(newcolor2 - color2) > threshold
        new_detect_3 = np.linalg.norm(newcolor3 - color3) > threshold
        new_detect_4 = np.linalg.norm(newcolor4 - color4) > threshold
        if not detect_1 and new_detect_1:
            pyautogui.press('right')
            detect_1 = True
        elif detect_1 and not new_detect_1:
            detect_1 = False

        if not detect_2 and new_detect_2:
            pyautogui.press('up')
            detect_2 = True
        elif detect_2 and not new_detect_2:
            detect_2 = False

        if not detect_3 and new_detect_3:
            pyautogui.press('down')
            detect_3 = True
        elif detect_3 and not new_detect_3:
            detect_3 = False

        if not detect_4 and new_detect_4:
            pyautogui.press('left')
            detect_4 = True
        elif detect_4 and not new_detect_4:
            detect_4 = False
        # cv2.imshow('my webcam', img)
        keypress = cv2.waitKey(1)
        if keypress == 27: 
            break  # esc to quit
        if keypress == 32:
            color1, std = cv2.meanStdDev(img[600-64:600+64, 250-64:250+64])
            color2, std = cv2.meanStdDev(img[600-64:600+64, 500-64:500+64])
            color3, std = cv2.meanStdDev(img[600-64:600+64, 750-64:750+64])
            color4, std = cv2.meanStdDev(img[600-64:600+64, 1000-64:1000+64])

    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()