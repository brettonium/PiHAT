from sense_hat import SenseHat
from time import sleep
from decimal import *

sense = SenseHat()
sense.clear()
tempAdjust = 10

while True:
  temp = sense.get_temperature()
  temp = round(temp, 3)
  f = ((temp * 1.8) + 32) - 10
  ftemp = Decimal(str(f)).quantize(Decimal('.001'), rounding=ROUND_UP)
  press = sense.get_pressure()
  press = round(press, 3)
  hum = sense.get_humidity()
  hum = round(hum, 3)

  msg = "Temperature. = {0}, Pressure. = {1}, Humidity. = {2}".format(ftemp, press, hum)
  
  print(msg)
  sleep (.5)
