from machine import Pin, PWM
from time import sleep

pwm_red = PWM(Pin(21))
pwm_yellow = PWM(Pin(20))
pwm_green = PWM(Pin(19))

full = 65535
half = 32768
quater = 16384
eighth = 8192
sixteenth = 4096
thirty_secound = 2048

pwm_red.freq(1000)
pwm_yellow.freq(1000)
pwm_green.freq(1000)

for i in range(5):
    print('full')
    pwm_red.duty_u16(full)
    pwm_yellow.duty_u16(full)
    pwm_green.duty_u16(full)
    sleep(1)
    print('half')
    pwm_red.duty_u16(half)
    pwm_yellow.duty_u16(half)
    pwm_green.duty_u16(half)
    sleep(1)
    print('quater')
    pwm_red.duty_u16(quater)
    pwm_yellow.duty_u16(quater)
    pwm_green.duty_u16(quater)
    sleep(1)
    print('eighth')
    pwm_red.duty_u16(eighth)
    pwm_yellow.duty_u16(eighth)
    pwm_green.duty_u16(eighth)
    sleep(1)
    print('sixteenth')
    pwm_red.duty_u16(sixteenth)
    pwm_yellow.duty_u16(sixteenth)
    pwm_green.duty_u16(sixteenth)
    sleep(1)
    print('thirty_secound')
    pwm_red.duty_u16(thirty_secound)
    pwm_yellow.duty_u16(thirty_secound)
    pwm_green.duty_u16(thirty_secound)
    sleep(1)

while True:
    for duty in range(65535):
        pwm_red.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65535, 0, -1):
        pwm_red.duty_u16(duty)
        sleep(0.0001)