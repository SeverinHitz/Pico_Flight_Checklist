from time import sleep
from machine import ADC, Pin, I2C
import RGB1602

battery_voltage = ADC(28)
red_led = Pin(20, Pin.OUT)
green_led = Pin(21, Pin.OUT)

i2c = I2C(0, sda=Pin(4), scl=Pin(5),freq = 400000)
lcd = RGB1602.RGB1602(16,2,i2c)

try:
    while True:
        reading = battery_voltage.read_u16() >> 4
        voltage = reading * 3.3 / 4096
        print('Reading:\t', reading, '\tVoltage:\t', voltage, 'V')
        lcd.clear()
        lcd.printout_v2(str(reading)+'\n'+str(voltage)+'V')
        if voltage > 2.7:
            red_led.off()
            green_led.on()
        else:
            red_led.on()
            green_led.off()
        sleep(0.5)
finally:
    red_led.off()
    green_led.off()