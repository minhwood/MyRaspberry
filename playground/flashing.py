from sense_hat import SenseHat
import time
santa = "Noel.png"
sword = "sword1.png"
ball = "ball5.png"

imgs = [santa,sword,ball]
s = SenseHat()
i = 0
while True:
  s.load_image(imgs[i])
  time.sleep(1)
  s.flip_h()
  time.sleep(1)
  i = i + 1
  if i == 3:
      i = 0


