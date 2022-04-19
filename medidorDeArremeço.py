from microbit import *
import radio
import math

radio.on()
radio.config(channel=30)
radio.config(power=7)

cont = 0

fraco = Image("00000:"
              "00000:"
              "00000:"
              "99000:"
              "99000")
medio = Image("00000:"
              "00000:"
              "99000:"
              "99000:"
              "99000")
forte = Image("00000:"
              "99000:"
              "99000:"
              "99000:"
              "99000")
superforte = Image("99000:"
              "99000:"
              "99000:"
              "99000:"
              "99000")




while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()from microbit import *
import radio
import math

radio.on()
radio.config(channel=30)
radio.config(power=7)

cont = 0

fraco = Image("00000:"
              "00000:"
              "00000:"
              "99000:"
              "99000")
medio = Image("00000:"
              "00000:"
              "99000:"
              "99000:"
              "99000")
forte = Image("00000:"
              "99000:"
              "99000:"
              "99000:"
              "99000")
superforte = Image("99000:"
              "99000:"
              "99000:"
              "99000:"
              "99000")




while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
