import RGB1602
import time
import math
from machine import I2C, Pin
colorR = 64
colorG = 128
colorB = 64

i2c = I2C(0, sda=Pin(4), scl=Pin(5),freq = 400000)
lcd=RGB1602.RGB1602(16,2,i2c)




rgb0 = (255,255,0)
rgb1 = (255,0,150) 
rgb2 = (255,0,200) 
rgb3 = (255,0,100) 
rgb4 = (50,50,0) 
rgb5 = (255,255,0)
rgb6 = (150,150,0)
rgb7 = (255,255,0) 
rgb8 = (75,75,0) 
rgb9 = (50,50,0) 

# set the cursor to column 0, line 1

lcd.setCursor(0, 0)
# print the number of seconds since reset:

# print the number of seconds since reset:
lcd.printout_v2("Waveshare\nHello,World!")
#   
# lcd.setCursor(0, 1)
# 
# lcd.printout("Hello,World!")
# 
#
while True:
    lcd.clear()
    lcd.setRGB(*rgb0);
    lcd.printout_v2('Farbe 0')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb1[0],rgb1[1],rgb1[2]);
    lcd.printout_v2('Farbe 1')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb2[0],rgb2[1],rgb2[2]);
    lcd.printout_v2('Farbe 2')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb3[0],rgb3[1],rgb3[2]);
    lcd.printout_v2('Farbe 3')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb4[0],rgb4[1],rgb4[2]);
    lcd.printout_v2('Farbe 4')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb5[0],rgb5[1],rgb5[2]);
    lcd.printout_v2('Farbe 5')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb6[0],rgb6[1],rgb6[2]);
    lcd.printout_v2('Farbe 6')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb7[0],rgb7[1],rgb7[2]);
    lcd.printout_v2('Farbe 7')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb8[0],rgb8[1],rgb8[2]);
    lcd.printout_v2('Farbe 8')
    time.sleep(1)
    lcd.clear()
    lcd.setRGB(rgb9[0],rgb9[1],rgb9[2]);
    lcd.printout_v2('Farbe 9')
    time.sleep(1)



    
