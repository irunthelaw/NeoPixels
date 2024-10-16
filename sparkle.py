import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=0.5)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255, 0, 255)
orange = (255, 60, 0)
purple = (128, 0, 128)

def halloween(back=cyan, sc=purple, dee=.06, spark=5):
    while True:
        for i in range(spark):
            wan = random.randint(0,29)
            too = random.randint(0,29)
            tree = random.randint(0,29)
            np.fill(back)
            np[wan] = sc
            np[too] = sc
            np[tree] = sc
            np.show()
            time.sleep(dee)
        

halloween()








