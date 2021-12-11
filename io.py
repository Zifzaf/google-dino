#! .venv/bin/python3

from PIL import Image
import time
import mss
import cv2
import numpy as np
from pynput.keyboard import Key, Controller

keyboard = Controller()

def press_up(t=10.0):
    r = float(t*np.random.rand(1)/1000.0)
    keyboard.press(Key.up)
    time.sleep(r)
    keyboard.release(Key.up)

def press_down(t=10.0):
    r = float(t*np.random.rand(1)/1000.0)
    keyboard.press(Key.down)
    time.sleep(r)
    keyboard.release(Key.down)

def get_fame_small_gray(sct):
    monitor = {"top": 345+238, "left": 660, "width": 600, "height": 50}
    return cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_BGR2GRAY)

def get_fame_gray(sct):
    monitor = {"top": 345+148, "left": 660, "width": 600, "height": 150}
    return cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_BGR2GRAY)

def get_fame_bin(sct):
    gimg = get_fame_gray(sct)
    thresh, bi = cv2.threshold(gimg, 127, 255, cv2.THRESH_BINARY)
    return bi

def get_fame_small_bin(sct):
    gimg = get_fame_small_gray(sct)
    thresh, bi = cv2.threshold(gimg, 127, 255, cv2.THRESH_BINARY)
    return bi

def main():
    with mss.mss() as sct:
        st = time.time()
        gimg = get_fame_small_gray(sct)
        et = time.time()
        print(et-st)
        im = Image.fromarray(gimg)
        im.save("gtest.jpg")
        st = time.time()
        bi = get_fame_small_bin(sct)
        et = time.time()
        print(et-st)
        im = Image.fromarray(bi)
        im.save("btest.jpg")


if __name__ == '__main__':
    main()
