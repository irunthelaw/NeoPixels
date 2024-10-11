import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
val = [red, yellow, green, cyan, blue, purple]


def fade_out(color, fading = 0.025, rob = 50):
    red_rat = color[0] / rob
    red_org = color[0]
    green_rat = color[1] / rob
    green_org = color[1]
    blue_rat = color[2] / rob
    blue_org = color[2]
    for i in range(1, 51):
        rad = red_org - i * red_rat
        gran = green_org - i * green_rat
        blau = blue_org - i * blue_rat
        np.fill((rad, gran, blau))
        np.show()
        print(np[0])
        time.sleep(fading)

def fade_in(colors, fading = 0.025, rob = 50):
    red_rat = colors[0] / rob
    red_org = colors[0]
    green_rat = colors[1] / rob
    green_org = colors[1]
    blue_rat = colors[2] / rob
    blue_org = colors[2]
    for i in range(1, 51):
        rad = red_org + i * red_rat
        gran = green_org + i * green_rat
        blau = blue_org + i * blue_rat
        np.fill((rad, gran, blau))
        np.show()
        print(np[0])
        time.sleep(fading)


def lights():
    while True:
        rainbows = random.choice(val)
        fade_in(rainbows)
        fade_out(rainbows)

lights()
