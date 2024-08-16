'''
Digital_Checklist
by Severin Hitz
'''
Version = 0.5

from time import sleep
from machine import Pin, Timer, I2C, ADC
import RGB1602
import bme280
import Checklist_DATA

###########################################################
# Initialiate I2C
i2c = I2C(0, sda=Pin(4), scl=Pin(5),freq = 400000)
print(i2c)
print(type(i2c))

###########################################################

# Initialiate BME 280
bme = bme280.BME280(i2c=i2c)
i2c.scan() # to solve compatibility problems with Display

# Get Data from BME280 Sensor
def bme_data():
    temp = round(bme.temp(), 1)
    pres = round(bme.pressure(), 1)
    hum = round(bme.humidity(), 1)
    alt = round(bme.alt(), 1)
    print(temp, pres, hum, alt)
    i2c.scan() # to solve compatibility problems with Display
    return temp, pres, hum, alt

###########################################################
# Initialiate I2C Devices
lcd = RGB1602.RGB1602(16,2,i2c) # LCD and LCD_led

##########################################################
# Display colors:
white = (255,255,255)
red = (255,0,0)
red_green = (255,255,0)
green = (0,255,0)
cyan = (50, 255, 50)
dark_red_green = (75, 75, 0)
violet = (255, 0, 100)
dim_white = (25,25,25)
##########################################################
# initialiate LED
on_board_led = Pin(25, Pin.OUT)
red_led = Pin(21, Pin.OUT)
yellow_led = Pin(20, Pin.OUT)
green_led = Pin(19, Pin.OUT)
# For StartUp LED On
red_led.on()
yellow_led.on()
green_led.on()
# Initialiate ADC
battery_voltage = ADC(28)
# Initialiate Buttons
pin_pox = Pin(6, Pin.IN, Pin.PULL_UP)    # POX
pin_sfu = Pin(7, Pin.IN, Pin.PULL_UP)    # SFU
pin_exit = Pin(10, Pin.IN, Pin.PULL_UP)  # Exit
pin_back = Pin(11, Pin.IN, Pin.PULL_UP)  # Back
pin_check = Pin(12, Pin.IN, Pin.PULL_UP) # Check
pin_enter = Pin(13, Pin.IN, Pin.PULL_UP) # Enter
pin_sos = Pin(14, Pin.IN, Pin.PULL_UP)   # SOS

###########################################################
# Checklist data in seperate File
###########################################################
# Global Functions

def menu_scroll(direction):
    '''Scroll through Menu'''
    global i
    if direction: # Forward direction
        i += 1 # One Forward
        if i > len(keys)-1: # End of list to beginning
            i = 0
    else: # Back direction
        i -=1
        if i < 0: # Beginning of list to end
            i = len(keys)-1
    lcd.clear()
    lcd.setRGB(*white)
    lcd.printout_v2(keys[i])

def check_scroll_down():
    '''Scroll through Checklist'''
    global i, j, k
    k += 1 # Next Position in 3 Level of List
    # print('scroll down\t' + str(k))
    if k%2 == 0: # Jump to next Item in Checklist
        j += 1 # Next Item in Checklist
        k = 0 # First Position of Checklist Item
    if j > len(checklist[keys[i]])-1: # One Section in Checklist completed
        i += 1 # Go to next Section
        if i > len(keys)-1: # End of Checklist
            i = 0 # Begining of Checklist
        j = -1 # 
        k = -1
        lcd.clear()
        lcd.setRGB(*white)
        lcd.printout_v2(keys[i])
    else:
        lcd.clear()
        if k%2 == 0: # Checklist item name
            lcd.setRGB(*checklist[keys[i]][j][2][0]) # set color of lcd
            lcd.printout_v2(checklist[keys[i]][j][k%2])
        else: # Checklist item required position
            lcd.setRGB(*checklist[keys[i]][j][2][1]) # set color of lcd
            lcd.printout_v2(checklist[keys[i]][j][k%2])
           
def check_scroll_up():
    global i, j, k
    # print('scroll up\t' + str(k))
    if abs(k%2) == 0:
        j -= 1 # Jump to previous Check of checklist section
    k = 0
    if j < 0: # One Section in Checklist endend (at beginning)
        lcd.clear()
        lcd.setRGB(*white)
        lcd.printout_v2(keys[i])
        i -= 1 # Jump to previous checklist section
        if i < 0: # At beginning of checklist 
            i = len(keys)-1 # Jump at end of checklist
        j = len(checklist[keys[i]])-1 # set to last Item of checklist section
        k = -1 # set so if next button press is scroll down
    else:
        lcd.clear()
        lcd.setRGB(*checklist[keys[i]][j][2][0]) # set color of lcd
        lcd.printout_v2(checklist[keys[i]][j][k%2])
        k = 0

###########################################################

###########################################################
# ADC Variables
adc_steps = 4096
adc_high = 3.3
bat_lev_low = 3.15
bat_cut_off = 2.5
R1 = 10000 # Resistor 1 of Voltage devider
R2 = 10000 # Resistor 2 of Voltage devider
# Look up Table for Percentage
look_up = {2.5: 100, 2.6: 2, 2.7: 3, 2.8: 6, 2.9: 8, 3.0: 12, 3.1: 18,
           3.2: 25, 3.3: 39, 3.4: 50, 3.5: 59, 3.6: 70, 3.7: 80,
           3.8: 88, 3.9: 98, 4.0: 99, 4.1: 100, 4.2:100}
# ADC Functions
def bat_check():
    adc_volt = read_adc() #Read current value on adc input (return Volt)
    if adc_volt > bat_lev_low: # If Bat Volt is high green on red off
        green_led.on()
        red_led.off()
    else: # else Bat Volt is low green off red on
        green_led.off()
        red_led.on()
    # Update Values in List
    pop_adc_values()
    set_adc_values()

def read_adc():
    reading = battery_voltage.read_u16() >> 4 # Read ADC input (>>4 to convert 16 bit to 12 bit)
    voltage = (reading * adc_high / adc_steps) / (R2/(R1+R2)) # For Voltage Devider
    return voltage

def pop_adc_values():
    try:
        checklist[keys[0]].pop(3) # Try poping the Index 3 (Bat Info)
    except Exception:
        pass
    
def set_adc_values():
    adc_volt = read_adc()
    # perc = round(((adc_volt-bat_cut_off)/1.7)*100,2) # Calculation for Percentage linear
    round_adc_volt = round(adc_volt, 1)
    if round_adc_volt > 4.2:
        perc = 100
    elif round_adc_volt < 2.5:
        perc = 0
    else:
        perc = look_up[round(adc_volt, 1)] # Via Lookup Table
    if round_adc_volt > 4.3:
        perc_str = 'Bat Percentage:\n' + 'Charging'
    else:
        perc_str = 'Bat Percentage:\n' + str(perc) + ' %'
    volt_str = 'Bat Voltage:\n' + str(round(adc_volt,2)) + ' V'
    checklist[keys[0]].insert(3, [volt_str, perc_str, [cyan, cyan]])# Insert at 3 Index
    
###########################################################
# Button Functions
def enter_press(channel):
    global debounce_2, hum_act # debounce counter and human interaction var
    print('###enter Pressed:\tDebounce Var:\t', debounce_2)
    if debounce_2 == False:
        debounce_2 = True # Debounce Counter
        debounce_timer_2() # Debounce Timer Set
        hum_act = True # Indicates a Human Interaction
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        global l
        if l == 0:
            l = 1
            check_scroll_down()

def check_press(channel):
    global debounce_1, hum_act # debounce counter and human interaction var
    print('###check Pressed:\tDebounce Var:\t', debounce_1)
    if debounce_1 == False:
        debounce_1 = True # Debounce Counter
        debounce_timer_1()  # Debounce Counter Set
        hum_act = True # Indicates a Human Interaction
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        if l == 0: # In Menu
            menu_scroll(True)
        elif l == 1: # In Checklist
            check_scroll_down()

def back_press(channel):
    global debounce_1, hum_act # debounce counter and human interaction var
    print('###back Pressed:\tDebounce Var:\t', debounce_1)
    if debounce_1 == False:
        debounce_1 = True # Debounce Counter
        debounce_timer_1()  # Debounce Counter Set
        hum_act = True # Indicates a Human Interaction
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        if l == 0: # In Menu
            menu_scroll(False)
        elif l == 1: # In Checklist
            check_scroll_up()

def exit_press(channel):
    global debounce_1, hum_act # debounce counter and human interaction var
    print('###exit Pressed:\tDebounce Var:\t', debounce_1)
    if debounce_1 == False:
        debounce_1 = True # Debounce Counter
        debounce_timer_1()  # Debounce Counter Set
        hum_act = True # Indicates a Human Interaction
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        global i, j, l, k
        if l == 0: # Only when allready in Menu go to Begining to Checklist
            i = 0 # list level 0
        j = -1 # list level 1
        k = -1 # list level 2
        l = 0 # menu level
        lcd.clear()
        lcd.setRGB(*white)
        lcd.printout_v2(keys[i])

def sos_press(channel):
    global debounce_1, hum_act # debounce counter and human interaction var
    print('###sos Pressed:\tDebounce Var:\t', debounce_1)
    if debounce_1 == False:
        debounce_1 = True # Debounce Counter
        debounce_timer_1()  # Debounce Counter Set
        hum_act = True # Indicates a Human Interaction
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        lcd.clear()
        lcd.setRGB(*red)
        lcd.printout_v2('SOS\nV bestGlide')

###########################################################
# InFlight Functions

def jump_to_climb_check():
    global i, j, k, l, climb_check, hum_act # Global Variables to Jump to Begin of Cruise Check
    print('+++400ft above Ground, Climb Check')
    if hum_act is False: # If no Human interaction
        climb_check = True # Set Take off Variable to True so that the Check is Prompted only once
        hum_act = True # Indicates a Human Interaction (to make sure no other interrupt checks come up)
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        l = 1 # Sets Checklevel to right place
        i = keys.index('CLIMB CHECK:') # Gets Index of Cruise Check end jumps to it
        j = -1 # sets level 1 of checklist item
        k = -1 # Sets level 2 to first position
        lcd.clear()
        lcd.setRGB(*violet)
        lcd.printout_v2('400 ft AGL:\n>CLIMB CHECK<', 0.05)   
        
    
def reached_fl_060():
    global i, j, k, l, hum_act, fl_060 # Global Variables to Jump to Begin of Cruise Check
    print('+++6000ft reached')
    if hum_act is False and keys[i] in ['CLIMB CHECK:', 'CRUISE CHECK:',
            'DESCENT CHECK:']:
            # If no Human interaction and in right place of Checklist
            fl_060 = True # Set FL 060 indicater Variable to Above FL 060
            hum_act = True # Indicates a Human Interaction (to make sure no other interrupt checks come up)
            hum_act_tim() # Starts Timer to Reset Variable hum_act
            l = 1 # Sets Checklevel to right place
            i = keys.index('CRUISE CHECK:') # Gets Index of Cruise Check end jumps to it
            j = -1 # sets level 1 of checklist item
            k = -1 # Sets level 2 to first position
            lcd.clear()
            lcd.setRGB(*violet)
            lcd.printout_v2('Above FL 060:\n>CRUISE CHECK<', 0.05)

def jump_to_cruise_check(channel):
    global i, j, k, l, hum_act # Global Variables to Jump to Begin of Cruise Check
    print('+++Cruise Check Timer ended')
    if hum_act is False and keys[i] in ['CLIMB CHECK:', 'CRUISE CHECK:',
        'DESCENT CHECK:']:
        # If no Human interaction and in right place of Checklist
        hum_act = True # Indicates a Human Interaction (to make sure no other interrupt checks come up)
        hum_act_tim() # Starts Timer to Reset Variable hum_act
        #cruise_timer() # Restarts the Cruise Timer for the next itteration
        l = 1 # Sets Checklevel to right place
        i = keys.index('CRUISE CHECK:') # Gets Index of Cruise Check end jumps to it
        j = -1 # sets level 1 of checklist item
        k = -1 # Sets level 2 to first position
        lcd.clear()
        lcd.setRGB(*violet)
        lcd.printout_v2('15 min elapsed:\n>CRUISE CHECK<', 0.05)
    else:
        # cruise_timer(cruise_check_backuptime) # Restarts the Cruise Timer with shorter intervall
        pass        

###########################################################
# BME Functions
def pop_bme_values():
    checklist[keys[0]].pop(1)
    checklist[keys[0]].pop(1)

def set_bme_values(data):
    temp_str = 'Temperatur:\n' + str(data[0]) + ' C'
    pres_str = 'Pressure:\n' + str(data[1]) + ' hpa'
    hum_str = 'Humidity:\n' + str(data[2]) + ' %'
    alt_str = 'Altitude:\n' + str(data[3]) + ' ft (QNE)'
    checklist[keys[0]].insert(1, [temp_str, pres_str, [cyan, cyan]])
    checklist[keys[0]].insert(2, [hum_str, alt_str, [cyan, cyan]])

###########################################################
# Start up Sequence

# set Variables
i = 0 # list level 0
j = -1 # list level 1
k = -1 # list level 2
l = 0 # menu level
debounce_1 = False # debounce counter
debounce_2 = False # Backup debounce (enter)
hum_act = False # Variable to indicate past human interaction
in_air = False # Variable to indicate if Take off has accured
climb_check = False # Variable to indicate if Take off check is completed
fl_060 = False # Variable to indicate if above or below FL 060
cruise_timer_bool = False # Variable that makes sure the cruise timer is only started once

# Check Status of Aircraft-Switch
if not pin_pox.value():
    print('pox')
    checklist = Checklist_DATA.pox_data()[1] # Data from seperate File
    keys = Checklist_DATA.pox_data()[0] # Data from seperate File
elif not pin_sfu.value():
    print('sfu')
    checklist = Checklist_DATA.sfu_data()[1] # Data from seperate File
    keys = Checklist_DATA.sfu_data()[0] # Data from seperate File
else:
    print('sgz')
    checklist = Checklist_DATA.sgz_data()[1] # Data from seperate File
    keys = Checklist_DATA.sgz_data()[0] # Data from seperate File

# Ad BME Sensor data to First Item on Checklist
start_bme = bme_data()
set_bme_values(start_bme)

# Ad ADC Battery Info to First Item on Checklist
bat_check()

# Printout fist line
lcd.printout_v2(keys[i], 0.1)
###########################################################
# Interrupts
pin_enter.irq(trigger=Pin.IRQ_FALLING, handler=enter_press)
pin_check.irq(trigger=Pin.IRQ_FALLING, handler=check_press)
pin_back.irq(trigger=Pin.IRQ_FALLING, handler=back_press)
pin_exit.irq(trigger=Pin.IRQ_FALLING, handler=exit_press)
pin_sos.irq(trigger=Pin.IRQ_FALLING, handler=sos_press)

###########################################################
# Variables for Checklist Interrupts:
## Climb Check:
### 400 ft AGL:
agl_400 = 400 # ft
## Cruise Check:
### Variance for Take Off dedection:
var_t_o = 50 # ft
### 6000 ft dedection Variance (+/-)
up_fl_060 = 6250 # ft
down_fl_060 = 5750 # ft

###########################################################

# Timers
## Timer Times:
### Debounce Time
debounce_time = 300 # Time of Debounce Timer
### Cruise Check Time
cruise_check_time = 900000 # ms
#### Cruise Check Time if not possible the first time
# cruise_check_backuptime = 11000 # not in  use
### last human interaction Time
hum_act_time = 20000 # ms

# Debounce Timer
def debounce_reset(channel):
    global debounce_1, debounce_2
    debounce_1 = False
    debounce_2 = False
    print('Reset Debonuce')
def debounce_timer_1():
    deb_tim_1 = Timer(-1)
    deb_tim_1.init(period=debounce_time, mode=Timer.ONE_SHOT, callback=debounce_reset)
def debounce_timer_2():
    deb_tim_2 = Timer(-1)
    deb_tim_2.init(period=debounce_time, mode=Timer.ONE_SHOT, callback=debounce_reset)

# Cruise Check Timer
# Starts Timer after Take Off for Repeated Cruise Check
def cruise_timer(time=cruise_check_time):   
    timer = Timer(-1)
    timer.init(period=time, mode=Timer.PERIODIC, callback=jump_to_cruise_check)
    print('***New Cruise Timer Started')
    
# Human interaction Timer
# Runs if a Interaction with the Device was made in the last XX min
def hum_act_reset(channel): # Resets the Variable hum_act
    global hum_act, debounce_1
    hum_act = False
    lcd.setRGB(*dim_white)
    print('***reset hum_act')

def hum_act_tim(): # Starts Timer after last Human Interaction
    global hum_tim
    try:
        hum_tim.deinit()
        print('***reset timer hum_act')
    except Exception:
        print('***First Interaction in a while')
    hum_tim = Timer(-1)
    hum_tim.init(period=hum_act_time, mode=Timer.ONE_SHOT, callback=hum_act_reset)
###########################################################
# Main Loop
try:
    while True:
        #on_board_led.toggle()
        sleep(5)
        yellow_led.on()
        print('STATUS:' + '\thum_act= ' + str(hum_act) + '\t\tdebounce_1= ' + str(debounce_1) +
              '\tdebounce_2= ' + str(debounce_2) + '\tin_air= ' + str(in_air) +
              '\tclimb_check= ' + str(climb_check) + '\tfl_060= ' + str(fl_060))
        bat_check() # Update LED and Info in List about BAT
        if hum_act is False:
            print('__________\nChecking BME280')
            live_bme = bme_data() # Reads Out BME Data
            pop_bme_values()
            set_bme_values(live_bme) # Sets BME Data in Display to new Values
            if live_bme[3] > start_bme[3]+var_t_o and in_air is False:
                in_air = True
                print('Take Off dedected')
            if in_air is True and cruise_timer_bool is False: # If Take_off is dedected
                cruise_timer_bool = True
                cruise_timer() # Starts Timer for Cruise Check
            if live_bme[3] > start_bme[3]+agl_400 and climb_check is False: # If 400 ft AGL is reached
                print('400 ft above ground')
                jump_to_climb_check()
            if live_bme[3] > up_fl_060 and fl_060 is False:
                reached_fl_060()
            if live_bme[3] < down_fl_060:
                fl_060 = False
        yellow_led.off()
                
                
    
finally:
    green_led.off()
    yellow_led.off()
    red_led.on()
    on_board_led.off()
    lcd.clear()

    
    