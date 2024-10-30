import board
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)

red = (255,00,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (106, 49, 81)
orange = (255, 60, 0)
purple = (128, 0, 128)
black= (0,0,0)
white = (255,255,255)

coloz = [red, yellow, green, cyan, blue, purple]

def bounce(fg, bg, direction = -1):
    g = 0
    for i in range(np.n):
        np.fill(bg)
        np.show()
        np[(g + direction) % np.n] = bg
        np[g % np.n] = fg
        np.show()
        g = (g + direction) % np.n
        time.sleep(0.1)
       

while True:
    bounce(red, black)
