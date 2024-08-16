# Bibliotheken laden
from machine import Pin, I2C
# Initialisierung I2C
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
# I2C-Bus-Scan ausgeben
devices = i2c.scan()
if devices:
    for d in devices:
        print(hex(d))
print(i2c.scan())