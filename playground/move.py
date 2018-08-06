from sense_hat import SenseHat
import random

s = SenseHat()
xo = 0
yo = 0
zo = 0
firsttime = 1
while True:
    acc = s.get_accelerometer_raw()
    x = acc['x']
    y = acc['y']
    z = acc['z']
    x = round(x,1)
    y = round(y,1)
    z = round(z,1)
    if xo != x or yo != y or zo !=z:
        color = (255,0,0)
        color2 = (10,10,10)
        i = random.randint(0,7)
        j = random.randint(0,7)
        if firsttime == 0:
            s.set_pixel(i2,j2,color2)
            s.set_pixel(i,j,color)
        i2 = i
        j2 = j
        firsttime = 0
        print("x = {0}, y = {1}, z = {2}".format(x,y,z))
    xo = x
    yo = y
    zo = z
