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

def bounce(fg, bg, bounces = 10):
    g = 0
    b = 1
    bc = 0
    while bc < bounces:
        np.fill(fg)
        np[g] = bg
        np[g+1] = bg
        np[g+2] = bg
        np[g-1] = bg
        np[g-2] = bg
        np.show()
        g += b
        if g >= (np.n-1) or g <=0:
            b *= -1
            bc += 1
        time.sleep(0.03)
        if g >= (np.n-1) or g <=0:
            b *= -1
            bc += 1
            
            if pix + 1 == p-1:
        
             

while True:
    bounce(red, blue)
