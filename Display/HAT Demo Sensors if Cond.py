from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 2)
    p = round(p, 2)
    h = round(h, 2)
    f = (t * 1.8) + 32

    if f > 70 and f < 100:
        bg = (0, 0, 0)  # green
    else:
        bg = (100, 0, 0)  # red

    msg = "Temp. = {0}, Press. = {1}, Hum. = {2}".format(f, p, h)

    sense.show_message(msg, scroll_speed=0.1, back_colour=bg)
    sleep(2)

    
