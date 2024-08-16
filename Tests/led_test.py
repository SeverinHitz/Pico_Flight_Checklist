
from time import sleep
from machine import Pin




# initialiate LED
red_led = Pin(20, Pin.OUT)
green_led = Pin(21, Pin.OUT)
red_led.value(0)
green_led.value(1)

try:
    while True:
        red_led.value(0)
        green_led.value(1)
        sleep(0.5)
        red_led.value(1)
        green_led.value(0)
        sleep(0.5)

finally:
    pass