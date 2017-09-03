from sense_hat import SenseHat
sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 2)
    p = round(p, 2)
    h = round(h, 2)

    msg = "Temp = {0}, Press = {1}, Hum = {2}".format(t,p,h)

    sense.show_message(msg, scroll_speed=0.1)
