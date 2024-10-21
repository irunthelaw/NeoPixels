import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.5)

orange = (255, 64, 0)
white = (255,255,255)
black = (0,0,0)
purple = (255,0,255)

def halloween(bg = orange, spark = purple):
    ohh = random.randint(1,2)
    for i in range(ohh):
        woo = random.randint(1, 8)
        woo = woo / 92
        np.fill(spark)
        np.show()
        time.sleep(woo)
        np.fill(bg)
        np.show()
        time.sleep(woo)
            
while True:
    halloween()
    time.sleep(2)
