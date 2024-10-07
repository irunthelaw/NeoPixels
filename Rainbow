import board
from neopixel import NeoPixel
import time

np = NeoPixel(board.NEOPIXEL, 1, auto_write=False, brightness=1)

red = 0
green = 0
blue = 0

def grn():
    for green in range(256):
        np.fill((255-green, green, 0))
        np.show()
        time.sleep(0.0001)
 
def bl():
    for blue in range(256):
        np.fill((0,255-blue, blue))
        np.show()
        time.sleep(0.0001)
        
def r():
    for red in range(256):
        np.fill((red, 0, 255-red))
        np.show()
        time.sleep(0.0001)
    
    
grn()
bl()
r()
