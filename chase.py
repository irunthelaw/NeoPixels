import board
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)

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

while True:
    chase((0,255, 255), "forward")
    time.sleep(.01)  




