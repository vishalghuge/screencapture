from PIL import ImageGrab
import cv2
import numpy as np
from datetime import datetime
import time


def screen_capture():
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 800, 600)))
    cv2.imshow('Python Window', screen)
    count = 0
    timeout = 1
    import tkinter as tk

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_height, screen_width)

    while True:
        count += 1
        start_time = datetime.now()
        # do your work here
        # print('Duration: {}'.format(end_time - start_time))
        screen = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
        # cv2.resizeWindow('jpg', screen_width, screen_height)
        cv2.imshow('window', screen)
        # cv2.destroyAllWindows()
        end_time = datetime.now()
        print("count in one second", count)
        # print('Duration: {}'.format(end_time - start_time))
        second = time.localtime().tm_sec
        print(second)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

