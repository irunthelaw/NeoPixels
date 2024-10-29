import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.5)

red = (255,30,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255, 0, 255)
orange = (255, 60, 0)
purple = (128, 0, 128)
black= (0,0,0)
white = (255,255,255)
coloz = [red, yellow, green, cyan, blue, purple]

def lightning(bg = orange, spark = orange):
    """
    light flashes orange a random amount of times (1-4)

    Args:
        bg: controls the background color of the neopixel strip to orange
        spark: changes color the spark of lightning, also orange.
    """
    ohh = random.randint(1,2)
    for i in range(ohh):
        woo = random.randint(1, 8)
        woo = woo / 92
        np.fill(spark)
        np.show()
        time.sleep(woo)
        np.fill(bg)
        np.show()
        time.sleep(woo)
        
def lightning3(bg = white, spark = white):
    """
    light flashes orange a random amount of times (1-4)

    Args:
        bg: controls the background color of the neopixel strip to orange
        spark: changes color the spark of lightning, also orange.
    """
    ohh = random.randint(1,2)
    for i in range(ohh):
        woo = random.randint(1, 8)
        woo = woo / 92
        np.fill(spark)
        np.show()
        time.sleep(woo)
        np.fill(bg)
        np.show()
        time.sleep(woo)


def chase(color):
    """
    The color black chases the color purple.

    Args:
        color: Changes the color of the neopixel
    """
    count = 0
    for i in range(np.n):
        np.fill(color)
    for i in range(np.n):
        if (i + count) % 3 == 0:
            np[i] = (0,0,0)

        
        np.show()
        time.sleep(0.1)  

        count += 2
        
      

        
def spark(back=orange, sc=purple, dee=.06, spark=5):
    
    """
    Random neopixels on the led lights up.

    Args:
        back: background color
        sc: spark color
        dee: delay between spark
        spark = how manty sparks at a time

    """
    for i in range(spark):
        wan = random.randint(0,29)
        too = random.randint(0,29)
        tree = random.randint(0,29)
        np.fill(back)
        np[wan] = sc
        np[too] = sc
        np[tree] = sc
        np.show()
        time.sleep(dee)
            
            
def fade_out(color, fading = 0.025, rob = 50):
    
    """
    The color fades out to black

    Args:
        color: the color of the 
        fading: speed of the fade
        rob = value to divide and get the fade from
    """
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
        time.sleep(fading)

def fade_in(colors, fading = 0.025, rob = 50):
    
    """
    The color fades in to black

    Args:
        color: the color of the 
        fading: speed of the fade
        rob: value to divide and get the fade from
    """
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
        time.sleep(fading)


        
def lightning2(bg = purple, spark = purple): #
    
    """
    light flashes orange a random amount of times (1-4)

    Args:
        bg: controls the background color of the neopixel strip to orange
        spark: changes color the spark of lightning, also orange.
    """
    
    ohh = random.randint(1,2)
    for i in range(ohh):
        woo = random.randint(1, 8)
        woo = woo / 92
        np.fill(spark)
        np.show()
        time.sleep(woo)
        np.fill(bg)
        np.show()
        time.sleep(woo)
        
        
def code(back=orange, sc=red, dee=.3, spark=15):
    """
    Random neopixels on the led lights up red.

    Args:
        back: background color
        sc: spark color
        dee: delay between spark
        spark = how manty sparks at a time

    """
    for i in range(spark):
        wan = random.randint(0,29)
        too = random.randint(0,29)
        tree = random.randint(0,29)
        np.fill(back)
        np[wan] = sc
        np[too] = sc
        np[tree] = sc
        np.show()
        time.sleep(dee)
  
    
def fire(am):
    """
    Random neopixels on the led lights up red.

    Args:
        am: how may times fire runs

    """
    for i in range(am):
        code(orange, red, 0.05 )
        
    
    
while True:
    me = random.choice(coloz)
    lightning3(black)
    fire(2)
    fade_out(orange)
    fade_in(purple)
    chase(purple)
    lightning(black)
    chase(orange)
    lightning2(black)
    lightning3(black)
    
    
