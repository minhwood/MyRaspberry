from sense_hat import SenseHat
import time
s = SenseHat()

red = (255,0,0)
black = (0,0,0)
white = (0,0,0)

for i in range(8):
    time.sleep(.200)
    for j in range(8):
        s.set_pixel(i,j,white)  

s.set_pixel(0,1,red)
time.sleep(.300)

s.set_pixel(0,2,red)
time.sleep(.300)

s.set_pixel(1,3,red)
time.sleep(.300)

s.set_pixel(2,4,red)
time.sleep(.300)

s.set_pixel(3,5,red)
time.sleep(.300)

s.set_pixel(4,4,red)
time.sleep(.300)

s.set_pixel(5,3,red)
time.sleep(.300)

s.set_pixel(6,2,red)
time.sleep(.300)

s.set_pixel(6,1,red)
time.sleep(.300)

s.set_pixel(5,0,red)
time.sleep(.300)

s.set_pixel(4,0,red)
time.sleep(.300)

s.set_pixel(3,1,red)
time.sleep(.300)

s.set_pixel(2,0,red)
time.sleep(.300)

s.set_pixel(1,0,red)
time.sleep(.300)








