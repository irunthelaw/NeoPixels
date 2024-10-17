import board
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write = False, brightness=0.3)

def chase():
    np.fill((0,0,0))
    np.show()
    count = 0
    for i in range(np.n):
        if i % 3 == 0:
            np[i] = (255,0,0)
            np.show()
            time.sleep(0.05)
        if i % 3 == 1:
            np[i] = (0,255,100)
            time.sleep(0.05)
            np.show()
        if i % 3 == 2:
            np[i] = (0,255,0)
            time.sleep(0.05)
            np.show()

while True:
    chase()






