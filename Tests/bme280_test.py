from machine import Pin, I2C
import bme280
import RGB1602
import time

i2c = I2C(0, sda=Pin(4), scl=Pin(5))
bme = bme280.BME280(i2c=i2c)
lcd = RGB1602.RGB1602(16,2,i2c)
while True:
    print(bme.values)
    print(bme.temp(), 'Temp')
    print(bme.pressure(), 'Pressure')
    print(bme.humidity(), 'Humidity')
    print(bme.alt(), 'Altitude')
    time.sleep(0.5)