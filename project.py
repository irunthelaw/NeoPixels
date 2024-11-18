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
brown = (250, 75, 20)
coloz = [red, yellow, green, cyan, blue, purple]

def bounce(fore, back, times = 2):
    a = 0
    direct = 1
    bounce = 0
    new_color = [int(c * 0.1) for c in brown]
    new_color2 = [int(c * 0.1) for c in red]
    while bounce < times:
        np.fill(back)
        np[a] = new_color
        if (a - 1) >= 0:
            np[(a - 1) % np.n] = new_color
        if (a - 2) >= 0:
            np[(a - 2) % np.n] = red
        if (a + 1) < 29:
            np[(a + 1) % np.n] = new_color
        if (a + 2) < 29:
            np[(a + 2) % np.n] = new_color2
        np.show()
        time.sleep(0.2)
           
        a += direct
        if a >= (np.n-1) or a <= 0:
            direct *= -1
            bounce += 1

while True:
    bounce(brown, green)
