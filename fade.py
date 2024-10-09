import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness=1)
i = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255, 0, 255)
orange = (255, 60, 0)
purple = (255, 20, 130)
color_list = [ yellow]

def fade_out(clr):
    color = (255,0,0)
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
        red - red_orig - i * red_ratio
        np.fill((red,0,0))
        np.show()
        time.sleep(.1)


def fade_in(color):
    red_ratio = color[0] / 50
    red_orig = color[0]
    for i in range(1,51):
        red - red_orig + i * red_ratio
        np.fill((red,0,0))
        np.show()
        time.sleep(.1)

fade_in((255,50,0))
fade_out((255,50,0))

