from sense_hat import SenseHat

s = SenseHat()

s.clear()
old_humidity = 0
while True:
    humidity = s.get_humidity()
    if humidity != old_humidity:
        print(humidity)
        s.show_message(str(round(humidity,2)))
    old_humidity = humidity
