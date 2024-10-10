import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 37)
purple = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
orange = (255, 64, 0)
val = [red, orange, yellow, green, cyan, blue, purple]


def fade_out(color, fading):
    red_rat = color[0] / 50
    red_org = color[0]
    green_rat = color[1] / 50
    green_org = color[1]
    blue_rat = color[2] / 50
    blue_org = color[2]
    for i in range(1, 51):
        rad = red_org - i * red_rat
        gran = green_org - i * green_rat
        blau = blue_org - i * blue_rat
        np.fill((rad, gran, blau))
        np.show()
        time.sleep(fading)

def fade_in(colors, fadings2):
    red_rat = colors[0] / 50
    red_org = colors[0]
    green_rat = colors[1] / 50
    green_org = colors[1]
    blue_rat = colors[2] / 50
    blue_org = colors[2]
    for i in range(1, 51):
        rad = red_org + i * red_rat
        gran = green_org + i * green_rat
        blau = blue_org + i * blue_rat
        np.fill((rad, gran, blau))
        np.show()
        time.sleep(fadings2)

while True:
    speed = 0.01
    rainbows = random.choice(val)
    fade_in(rainbows, speed)
    fade_out(rainbows, speed)

