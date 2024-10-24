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

def halloween(back=orange, sc=red, dee=.3, spark=15):
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
  

def chase(color, direction):
    count = 0
    while True:
        for i in range(np.n):
            np.fill(color)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0,0,0)

        
        np.show()
        time.sleep(0.2)  

        count += 2
      
def fire(am):
    for i in range(am):
        halloween(orange, red, 0.05 )
        

