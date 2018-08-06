from sense_hat import SenseHat
import random

s = SenseHat()
s.clear()
n = random.randint(0,7)
m = random.randint(0,7)
i = 4
j = 4
i2 = 0
j2 = 0
xo = 0
yo = 0
zo = 0
offset = 10
color = (255,0,0)
first_time = 1
s.set_pixel(n,m,(0,255,0))
while True:
    acc = s.get_orientation()
    x = acc['pitch']
    y = acc['yaw']
    z = acc['roll']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)

    if xo != x or zo !=  z:
        first_time = 0
        if x>xo: i = i - 1
        elif x<xo: i = i + 1
        if z>zo: j = j + 1
        elif z<zo: j = j - 1
        
        if j>7:
            s.show_message("Game Over")
            break;
        elif j<0:
            s.show_message("Game Over")
            break;

        if i>7: 
            s.show_message("Game Over")
            break;
        elif i<0:
            s.show_message("Game Over")
            break;

        if i == n and j == m:
            s.show_message("Winner")
            break;
        s.set_pixel(i2,j2,(0,0,0))
        s.set_pixel(i,j,color)
        print("x = {0}, y = {1}, z = {2}".format(x,y,z))
        xo = x
        yo = y
        zo = z
        i2 = i
        j2 = j
