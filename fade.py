import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)
i = 0



def fade_out(color):
    red_ratio = color[0] / 50
    red_orig = color[0]
    for i in range(1,51):
        red - red_orig - i * red_ratio
        np.fill((red,0,0))
        np.show()
        time.sleep(.1)
        
def fade_in(color):
    red_ratio = color[0] / 50
    red_orig = color[0]
    for i in range(1,51):
        red + red_orig - i * red_ratio
        np.fill((red,0,0))
        np.show()
        time.sleep(.1)


fade_in((255,150,22))
fade_out((255,150,22))

