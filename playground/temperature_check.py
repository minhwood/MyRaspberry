from sense_hat import SenseHat

s = SenseHat()

old_t = 0
while True:
    t = s.get_temperature()
    t = round(t,1)
    if t != old_t:
        print(t)
    old_t = t


