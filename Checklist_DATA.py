# Checklist data for digital_checklist.py
##############################################################################
# Display colors:
white = (255,255,255)
red = (255,0,0)
red_green = (255,255,0)
green = (0,255,0)
cyan = (50, 255, 50)
dark_red_green = (75, 75, 0)
violet = (255, 0, 100)
##############################################################################
# POX
def pox_data():
    pox_keys = ['Aircraft:\nHB-POX', 'PREFLIGHT CHECK:',
        'CHECK BEFORE\nENGINE START:', 'ENGINE START:', 'CHECK AFTER\nENGINE START:',
        'TAXI CHECK:', 'RUN UP:', 'CHECK BEFORE\nDEPARTURE:',
        'LINE UP CHECK:', 'CLIMB CHECK:', 'CRUISE CHECK:',
        'DESCENT CHECK:', 'APPROACH CHECK:', 'LANDING CHECK:', 'AFTER LANDING\nCHECK:',
        'ENGINE SHUT DOWN\nAND PARKING:']
    pox_checklist = {pox_keys[0]:[['Checklist\nVersion 0.55','Date:\n06.10.2022', [cyan, cyan]]],
             pox_keys[1]:[['Outside check', 'COMPLETED', [red_green, green]],
                          ['Cargo door', 'CLOSED & LOCKED', [red_green, green]],
                          ['Aircraft papers','CHECKED', [red_green, green]],
                          ['Aircraft log','CHECKED', [red_green, green]],
                          ['Tow bar','REMOVED &\nSECURED', [red_green, green]],
                          ['Cabin','CHECKED', [red_green, green]],
                          ['Load sheet', 'WITHIN LIMITS', [red_green, green]],
                          ['PREFLIGHT CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[2]:[['Seats','ADJUSTED &\nLOCKED', [red_green, green]],
                          ['Parking brake','SET', [red_green, green]],
                          ['Seat belts &\nharness', 'FASTENED', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Circuits breakers','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['Battery master &\nalternator','ON', [red_green, green]],
                          ['Annunciator\nlights','Test', [red_green, green]],
                          ['ELT','AUTO, ARMED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [red_green, green]],
                          ['Mixture','RICH', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Throttle','IDLE', [red_green, green]],
                          ['Cabin door','CLOSED & LOCKED', [red_green, green]],
                          ['CHECK BEFORE\nENGINE START','COMPLETED', [red_green, green]],
                          ],
             pox_keys[3]:[['NAV lights','ON', [red_green, green]],
                          ['Fuel pump','ON', [red_green, green]],
                          ['Priming','ACCORDING AFM', [dark_red_green, green]],
                          ['Throttle','0.5 cm OPEN', [dark_red_green, green]],
                          ['Propeller area','CLEAR', [dark_red_green, green]],
                          ['Ignition key','START,\nTIME CHECK', [dark_red_green, green]],
                          ['Throttle','SET 1000 RPM', [dark_red_green, green]],
                          ['Oil pressure','MIN GREEN ARC\n(within 30\'\')', [dark_red_green, green]],
                          ['ENGINE START','COMPLETED', [red_green, green]]
                          ],
             pox_keys[4]:[['Alternator\noutput','CHECKED', [red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [red_green, green]],
                          ['Primer','IN & LOCKED', [red_green, green]],
                          ['Ventilation,\nheater,defroster','AS REQUIRED', [red_green, green]],
                          ['Avionics','ON\n(check ATIS)', [red_green, green]],
                          ['Flight\ninstruments','SET & CHECKED', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Avionics COM,\nNAV, Transp.','SET &\nPRESELECTED', [red_green, green]],
                          ['Autopilot test','COMPLETED', [red_green, green]],
                          ['CHECK AFTER\nENGINE START','COMPLETED', [red_green, green]]
                          ],
             pox_keys[5]:[['Brakes &\nsteering','CHECKED', [dark_red_green, green]],
                          ['Flight\ninstruments','CHECKED', [dark_red_green, green]],
                          ['TAXI CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[6]:[['Parking brake','SET', [red_green, green]],
                          ['Warm up time','CHECKED\nOIL T green arc', [red_green, green]],
                          ['Zone behind\naircraft','CLEAR', [red_green, green]],
                          ['Throttle','SET 2000 RPM', [dark_red_green, green]],
                          ['ENG INSTR,\nsuction, ammeter','CHECKED', [dark_red_green, green]],
                          ['Magnetos\n(L-B-R-L-B)','CHECKED (max-175,\nmax dev 50RPM)', [dark_red_green, green]],
                          ['Mixture','CHECK FUNCTION', [dark_red_green, green]],
                          ['Carburettor heat','CHECK FUNCTION', [dark_red_green, green]],
                          ['Throttle idle','CHECKED\n(500-700 RPM)', [dark_red_green, green]],
                          ['Throttle','SET 1000 RPM', [dark_red_green, green]],
                          ['RUN UP','COMPLETED', [red_green, green]]
                          ],
             pox_keys[7]:[['Fuel pump','ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT\nENDURANCE', [red_green, green]],
                          ['Fuel selector','SWITCH TO\nRIGHT TANK', [red_green, green]],
                          ['Mixture','AS REQUIRED', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Friction','SET', [red_green, green]],
                          ['Magnetos','BOTH', [red_green, green]],
                          ['Trim','SET FOR\nDEPARTURE (2)', [red_green, green]],
                          ['Flaps','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Flight inst.\n& avionics','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Seat positions','CHECKED &\nLOCKED', [red_green, green]],
                          ['Cabin & PAX','SECURED', [red_green, green]],
                          ['Flight\ncontrols','FREE &\nCORRECT', [red_green, green]],
                          ['Departure\nbriefing','COMPLETED', [red_green, green]],
                          ['CHECK BEFORE\nDEPARTURE','COMPLETED', [red_green, green]]
                          ],
             pox_keys[8]:[['Cabin door &\nwindow','CLOSED & LOCKED', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['Approach sector &\nrunway','CLEAR', [dark_red_green, green]],
                          ['Landing &\nrec lights','ON', [dark_red_green, green]],
                          ['Anti-collision\nlight (ACL)','ON', [dark_red_green, green]],
                          ['LINE UP CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[9]:[['Flaps','UP (CRUISE\nposition)', [dark_red_green, green]],
                          ['Climb power','SET', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [dark_red_green, green]],
                          ['CLIMB CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[10]:[['Altimeter','CHECKED\n(STD or QNH)', [red_green, green]],
                          ['Directional gyro','CHECKED, SET', [red_green, green]],
                          ['Cruise power','SET', [red_green, green]],
                          ['Mixture','SET', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Fuel pressure','PRESSURE CHECKED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','AS REQUIRED', [red_green, green]],
                          ['CRUISE CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[11]:[['ATIS or\nAD information','NOTED', [dark_red_green, green]],
                          ['Approach\nbriefing','COMPLETED', [dark_red_green, green]],
                          ['Avionics','SET & CHECKED', [dark_red_green, green]],
                          ['Directional gyro','SET & CHECKED', [dark_red_green, green]],
                          ['Circuit breakers','CHECKED', [dark_red_green, green]],
                          ['Cabin & PAX','SECURED', [dark_red_green, green]],
                          ['DESCENT CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[12]:[['Altimeter','QNH SET', [dark_red_green, green]],
                          ['Fuel pump','ON,\nPRESSURE CHECKED', [dark_red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [dark_red_green, green]],
                          ['Fuel selector','RIGHT TANK\nlow => LEFT TANK', [dark_red_green, green]],
                          ['Mixture','AS REQUIRED', [dark_red_green, green]],
                          ['Carburettor\nheat','AS REQUIRED', [dark_red_green, green]],
                          ['APPROACH CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[13]:[['Flaps','SET FOR LANDING', [dark_red_green, green]],
                          ['Mixture','AS REQUIRED', [dark_red_green, green]],
                          ['Carburettor\nheat','OFF', [dark_red_green, green]],
                          ['LANDING CHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[14]:[['Anti-collision\nlights (ACL)','OFF', [dark_red_green, green]],
                          ['Landing &\nrec. lights','OFF', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [dark_red_green, green]],
                          ['Flaps','UP', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['AFTER LANDING\nCHECK','COMPLETED', [red_green, green]]
                          ],
             pox_keys[15]:[['Parking brake','SET', [red_green, green]],
                          ['Throttle','SET 1000 RPM', [red_green, green]],
                          ['121.500 MHz\n(ELT)','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Mixture','LEAN, CUT OFF', [red_green, green]],
                          ['Magnetos','OFF, KEY REMOVED', [red_green, green]],
                          ['NAV lights','OFF', [red_green, green]],
                          ['Flight data &\ndocuments','NOTED &\nCOMPLETED', [red_green, green]],
                          ['Battery master &\nalternator','OFF', [red_green, green]],
                          ['Aircraft','TO BE SECURED', [red_green, green]],
                          ['PARKING CHECK','COMPLETED', [red_green, green]]
                          ]
             }
    return pox_keys, pox_checklist

##############################################################################
# SGZ
def sgz_data():
    sgz_keys = ['Aircraft:\nHB-SGZ', 'PREFLIGHT CHECK:',
        'CHECK BEFORE\nENGINE START:', 'ENGINE START:', 'CHECK AFTER\nENGINE START:',
        'TAXI CHECK:', 'RUN UP:', 'CHECK BEFORE\nDEPARTURE:',
        'LINE UP CHECK:', 'CLIMB CHECK:', 'CRUISE CHECK:',
        'DESCENT CHECK:', 'APPROACH CHECK:', 'LANDING CHECK:', 'AFTER LANDING\nCHECK:',
        'ENGINE SHUT DOWN\nAND PARKING:']
    sgz_checklist = {sgz_keys[0]:[['Checklist\nVersion 0.5','Date:\n24.09.2022', [cyan, cyan]]],
             sgz_keys[1]:[['Outside check', 'COMPLETED', [red_green, green]],
                          ['Cargo door', 'CLOSED & LOCKED', [red_green, green]],
                          ['Aircraft papers','CHECKED', [red_green, green]],
                          ['Aircraft log','CHECKED', [red_green, green]],
                          ['Tow bar','REMOVED &\nSECURED', [red_green, green]],
                          ['Cabin','CHECKED', [red_green, green]],
                          ['Load sheet', 'WITHIN LIMITS', [red_green, green]],
                          ['PREFLIGHT CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[2]:[['Seats','ADJUSTED &\nLOCKED', [red_green, green]],
                          ['Parking brake','SET', [red_green, green]],
                          ['Seat belts &\nharness', 'FASTENED', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Circuits breakers','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['P/S heat switch','OFF', [red_green, green]],
                          ['ALT1 / BAT','ON', [red_green, green]],
                          ['WRNG LGTS\nALT,ENG,P/S HEAT','ON', [red_green, green]],
                          ['ELT','AUTO, ARMED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','SWITCH to\nEMPTIER TANK', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Throttle','IDLE', [red_green, green]],
                          ['Canopy','CLOSED & LOCKED', [red_green, green]],
                          ['CHECK BEFORE\nENGINE START','COMPLETED', [red_green, green]],
                          ],
             sgz_keys[3]:[['NAV lights','ON', [red_green, green]],
                          ['Fuel pump','ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Magnetos','OFF', [red_green, green]],
                          ['Throttle\ncold engine','IDLE', [dark_red_green, green]],
                          ['Throttle\nhot engine','0.5 cm OPEN', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [dark_red_green, green]],
                          ['Propeller area','CLEAR', [dark_red_green, green]],
                          ['Choke\ncold engine','PULL', [dark_red_green, green]],
                          ['Choke\nhot engine','OFF', [dark_red_green, green]],
                          ['Ignition','START, then BOTH\nTIME CHECK', [dark_red_green, green]],
                          ['Throttle','SET 820 RPM 2\',\nthen 1030 RPM', [dark_red_green, green]],
                          ['Oil pressure','GREEN\n(within 10\'\')', [dark_red_green, green]],
                          ['ENGINE START','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[4]:[['ALT1 & ALT2','WRNG LGTS OUT', [red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [red_green, green]],
                          ['Annunciator\nlights','TEST WRNG LGTS', [red_green, green]],
                          ['Ventilation,\nheater,defroster','AS REQUIRED', [red_green, green]],
                          ['Avionics','ON\n(check ATIS)', [red_green, green]],
                          ['Flight\ninstruments','SET & CHECKED', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Avionics COM,\nNAV, XPDR','SET &\nPRESELECTED', [red_green, green]],
                          ['Flaps','UP (CRUISE\nposition)', [red_green, green]],
                          ['P/S heat\nswitch','ON,\nWRNG LGT OFF', [red_green, green]],
                          ['P/S heat\nswitch','OFF,\nWRNG LGT ON', [red_green, green]],
                          ['CHECK AFTER\nENGINE START','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[5]:[['Brakes &\nsteering','CHECKED', [dark_red_green, green]],
                          ['Flight\ninstruments','CHECKED', [dark_red_green, green]],
                          ['TAXI CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[6]:[['Parking brake','SET', [red_green, green]],
                          ['Warm up time','CHECKED\n(OIL T min 50C)', [red_green, green]],
                          ['Zone behind\naircraft','CLEAR', [red_green, green]],
                          ['Throttle','SET 1700 RPM', [dark_red_green, green]],
                          ['ENG INSTR,\nvoltmeter','CHECKED', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','CHECK FUNCTION\n(3x)', [dark_red_green, green]],
                          ['Magnetos\n(L-B-R-L-B)','CHECKED (max-120,\nmax dev 50RPM)', [dark_red_green, green]],
                          ['Carburettor heat','CHECK FUNCTION\n(max -50 RPM)', [dark_red_green, green]],
                          ['Throttle idle','CHECKED\n(500-700 RPM)', [dark_red_green, green]],
                          ['Throttle','SET 1030 RPM', [dark_red_green, green]],
                          ['RUN UP','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[7]:[['Fuel pump','ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT\nENDURANCE', [red_green, green]],
                          ['Fuel selector','FULLER TANK', [red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Magnetos','BOTH', [red_green, green]],
                          ['Trim','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Flaps','SET T/O\nPOSITION', [red_green, green]],
                          ['Flight inst.\n& avionics','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Seat positions','CHECKED &\nLOCKED', [red_green, green]],
                          ['Cabin & PAX','SECURED', [red_green, green]],
                          ['Flight\ncontrols','FREE &\nCORRECT', [red_green, green]],
                          ['Departure\nbriefing','COMPLETED', [red_green, green]],
                          ['CHECK BEFORE\nDEPARTURE','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[8]:[['Canopy & windows','CLOSED & LOCKED', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['Approach sector &\nrunway','CLEAR', [dark_red_green, green]],
                          ['Landing light','ON', [dark_red_green, green]],
                          ['Anti-collision\nlight (ACL)','ON', [dark_red_green, green]],
                          ['LINE UP CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[9]:[['Flaps','UP (CRUISE\nposition)', [dark_red_green, green]],
                          ['Climb power\nthrottle','SET FULL', [dark_red_green, green]],
                          ['Climb power\nprop control lev','SET 2386(max 5\')\nthen 2260 RPM', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [dark_red_green, green]],
                          ['CLIMB CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[10]:[['Altimeter','CHECKED\n(STD or QNH)', [red_green, green]],
                          ['Cruise power','SET', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Fuel pump','ABV 6000ft ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','AS REQUIRED', [red_green, green]],
                          ['P/S heat\nswitch','AS REQUIRED,\nOFF at OAT > 15C', [red_green, green]],
                          ['CRUISE CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[11]:[['ATIS or\nAD information','NOTED', [dark_red_green, green]],
                          ['Approach\nbriefing','COMPLETED', [dark_red_green, green]],
                          ['Avionics','SET & CHECKED', [dark_red_green, green]],
                          ['Circuit breakers','CHECKED', [dark_red_green, green]],
                          ['Cabin & PAX','SECURED', [dark_red_green, green]],
                          ['Carburettor heat','AS REQUIRED', [dark_red_green, green]],
                          ['DESCENT CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[12]:[['Altimeter','QNH SET', [dark_red_green, green]],
                          ['Fuel pump','ON, PRESSURE\nCHECKED', [dark_red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [dark_red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [dark_red_green, green]],
                          ['Carburettor\nheat','ON', [dark_red_green, green]],
                          ['APPROACH CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[13]:[['Flaps','SET FOR LANDING', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [dark_red_green, green]],
                          ['Carburettor\nheat','OFF', [dark_red_green, green]],
                          ['LANDING CHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[14]:[['Anti-collision\nlights (ACL)','OFF', [dark_red_green, green]],
                          ['Landing light','OFF', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nPRESSURE CHECKED', [dark_red_green, green]],
                          ['Flaps','UP (CRUISE\nposition)', [dark_red_green, green]],
                          ['Carburettor','OFF', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['AFTER LANDING\nCHECK','COMPLETED', [red_green, green]]
                          ],
             sgz_keys[15]:[['Parking brake','SET', [red_green, green]],
                          ['Throttle','IDLE', [red_green, green]],
                          ['Flaps','DOWN\n(LDG position)', [red_green, green]],
                          ['121.500 MHz\n(ELT)','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Magnetos','OFF, KEY REMOVED', [red_green, green]],
                          ['NAV lights','OFF', [red_green, green]],
                          ['ALT1 & BAT','OFF', [red_green, green]],
                          ['Flight data &\ndocuments','NOTED &\nCOMPLETED', [red_green, green]],
                          ['Aircraft','TO BE SECURED', [red_green, green]],
                          ['PARKING CHECK','COMPLETED', [red_green, green]]
                          ]
             }
    return sgz_keys, sgz_checklist

##############################################################################
# SFU
def sfu_data():
    sfu_keys = ['Aircraft:\nHB-SFU/SFS', 'PREFLIGHT CHECK:',
        'CHECK BEFORE\nENGINE START:', 'ENGINE START:', 'CHECK AFTER\nENGINE START:',
        'TAXI CHECK:', 'RUN UP:', 'CHECK BEFORE\nDEPARTURE:',
        'LINE UP CHECK:', 'CLIMB CHECK:', 'CRUISE CHECK:',
        'DESCENT CHECK:', 'APPROACH CHECK:', 'LANDING CHECK:', 'AFTER LANDING\nCHECK:',
        'ENGINE SHUT DOWN\nAND PARKING:']
    sfu_checklist = {sfu_keys[0]:[['Checklist\nVersion 0.5','Date:\n24.09.2022', [cyan, cyan]]],
             sfu_keys[1]:[['Outside check', 'COMPLETED', [red_green, green]],
                          ['Cargo door', 'CLOSED & LOCKED', [red_green, green]],
                          ['Aircraft papers','CHECKED', [red_green, green]],
                          ['Aircraft log','CHECKED', [red_green, green]],
                          ['Tow bar','REMOVED &\nSECURED', [red_green, green]],
                          ['Cabin','CHECKED', [red_green, green]],
                          ['Load sheet', 'WITHIN LIMITS', [red_green, green]],
                          ['PREFLIGHT CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[2]:[['Seats','ADJUSTED &\nLOCKED', [red_green, green]],
                          ['Parking brake','SET', [red_green, green]],
                          ['Seat belts &\nharness', 'FASTENED', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Circuits breakers','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['Battery master &\nalternator','ON', [red_green, green]],
                          ['Warning lights\n(alt, fuel pressure)','ON', [red_green, green]],
                          ['ELT','AUTO, ARMED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','SWITCH to\nEMPTIER TANK', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Throttle','IDLE', [red_green, green]],
                          ['Canopy','CLOSED & LOCKED', [red_green, green]],
                          ['CHECK BEFORE\nENGINE START','COMPLETED', [red_green, green]],
                          ],
             sfu_keys[3]:[['NAV lights','ON', [red_green, green]],
                          ['Fuel pump','ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Magnetos','OFF', [red_green, green]],
                          ['Throttle\ncold engine','IDLE', [dark_red_green, green]],
                          ['Throttle\nhot engine','0.5 cm OPEN', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [dark_red_green, green]],
                          ['Propeller area','CLEAR', [dark_red_green, green]],
                          ['Choke\ncold engine','PULL', [dark_red_green, green]],
                          ['Choke\nhot engine','OFF', [dark_red_green, green]],
                          ['Ignition','START, then BOTH\nTIME CHECK', [dark_red_green, green]],
                          ['Throttle','SET 820 RPM 2\',\nthen 1030 RPM', [dark_red_green, green]],
                          ['Oil pressure','GREEN\n(within 10\'\')', [dark_red_green, green]],
                          ['ENGINE START','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[4]:[['Alternator light','OUT', [red_green, green]],
                          ['Fuel pump','OFF,\nWRNG LGT OUT', [red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [red_green, green]],
                          ['Annunciator\nlights','TEST WRNG LGTS', [red_green, green]],
                          ['Ventilation,\nheater,defroster','AS REQUIRED', [red_green, green]],
                          ['Avionics','ON\n(check ATIS)', [red_green, green]],
                          ['Flight\ninstruments','SET & CHECKED', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Avionics COM,\nNAV, Transp.','SET &\nPRESELECTED', [red_green, green]],
                          ['Flaps','UP (CRUISE\nposition)', [red_green, green]],
                          ['CHECK AFTER\nENGINE START','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[5]:[['Brakes &\nsteering','CHECKED', [dark_red_green, green]],
                          ['Flight\ninstruments','CHECKED', [dark_red_green, green]],
                          ['TAXI CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[6]:[['Parking brake','SET', [red_green, green]],
                          ['Warm up time','CHECKED\n(OIL T min 50C)', [red_green, green]],
                          ['Zone behind\naircraft','CLEAR', [red_green, green]],
                          ['Throttle','SET 1700 RPM', [dark_red_green, green]],
                          ['ENG INSTR,\nvoltmeter','CHECKED', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','CHECK FUNCTION\n(3x)', [dark_red_green, green]],
                          ['Magnetos\n(L-B-R-L-B)','CHECKED (max-120,\nmax dev 50RPM)', [dark_red_green, green]],
                          ['Carburettor heat','CHECK FUNCTION\n(max -50 RPM)', [dark_red_green, green]],
                          ['Throttle idle','CHECKED\n(500-700 RPM)', [dark_red_green, green]],
                          ['Throttle','SET 1030 RPM', [dark_red_green, green]],
                          ['RUN UP','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[7]:[['Fuel pump','ON,\nWRNG LGT OUT', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT\nENDURANCE', [red_green, green]],
                          ['Fuel selector','FULLER TANK', [red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [red_green, green]],
                          ['Carburettor heat','OFF', [red_green, green]],
                          ['Magnetos','BOTH', [red_green, green]],
                          ['Trim','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Flaps','SET T/O\nPOSITION', [red_green, green]],
                          ['Flight inst.\n& avionics','SET FOR\nDEPARTURE', [red_green, green]],
                          ['Seat positions','CHECKED &\nLOCKED', [red_green, green]],
                          ['Cabin & PAX','SECURED', [red_green, green]],
                          ['Flight\ncontrols','FREE &\nCORRECT', [red_green, green]],
                          ['Departure\nbriefing','COMPLETED', [red_green, green]],
                          ['CHECK BEFORE\nDEPARTURE','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[8]:[['Canopy & windows','CLOSED & LOCKED', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['Approach sector &\nrunway','CLEAR', [dark_red_green, green]],
                          ['Landing light','ON', [dark_red_green, green]],
                          ['Anti-collision\nlight (ACL)','ON', [dark_red_green, green]],
                          ['LINE UP CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[9]:[['Flaps','UP (CRUISE\nposition)', [dark_red_green, green]],
                          ['Climb power','SET\n(FULL / 2260 RPM)', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nWRNG LGT OUT', [dark_red_green, green]],
                          ['CLIMB CHECK','COMPLETED', [dark_red_green, green]]
                          ],
             sfu_keys[10]:[['Altimeter','CHECKED\n(STD or QNH)', [red_green, green]],
                          ['Directional gyro','CHECKED, SET', [red_green, green]],
                          ['Cruise power','SET', [red_green, green]],
                          ['Engine\ninstruments','CHECKED', [red_green, green]],
                          ['Fuel pump','ABV 6000ft ON,\nPRESSURE CHECKED', [red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [red_green, green]],
                          ['Fuel selector','AS REQUIRED', [red_green, green]],
                          ['CRUISE CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[11]:[['ATIS or\nAD information','NOTED', [dark_red_green, green]],
                          ['Approach\nbriefing','COMPLETED', [dark_red_green, green]],
                          ['Avionics','SET & CHECKED', [dark_red_green, green]],
                          ['Directional gyro','SET & CHECKED', [dark_red_green, green]],
                          ['Circuit breakers','CHECKED', [dark_red_green, green]],
                          ['Cabin & PAX','SECURED', [dark_red_green, green]],
                          ['Carburettor heat','AS REQUIRED', [dark_red_green, green]],
                          ['DESCENT CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[12]:[['Altimeter','QNH SET', [dark_red_green, green]],
                          ['Fuel pump','.ON,\nWRNG LGT OUT', [dark_red_green, green]],
                          ['Fuel quantity','LEFT + RIGHT,\nENDURANCE', [dark_red_green, green]],
                          ['Fuel selector','SWITCH to\nFULLER TANK', [dark_red_green, green]],
                          ['Carburettor\nheat','ON', [dark_red_green, green]],
                          ['APPROACH CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[13]:[['Flaps','SET FOR LANDING', [dark_red_green, green]],
                          ['Propeller\ncontrol lever','HIGH RPM', [dark_red_green, green]],
                          ['Carburettor\nheat','OFF', [dark_red_green, green]],
                          ['LANDING CHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[14]:[['Anti-collision\nlights (ACL)','OFF', [dark_red_green, green]],
                          ['Landing light','OFF', [dark_red_green, green]],
                          ['Fuel pump','OFF,\nWRNG LTG OUT', [dark_red_green, green]],
                          ['Flaps','UP (CRUISE\nposition)', [dark_red_green, green]],
                          ['Carburettor','OFF', [dark_red_green, green]],
                          ['Time','NOTED', [dark_red_green, green]],
                          ['AFTER LANDING\nCHECK','COMPLETED', [red_green, green]]
                          ],
             sfu_keys[15]:[['Parking brake','SET', [red_green, green]],
                          ['Throttle','IDLE', [red_green, green]],
                          ['Flaps','DOWN\n(LDG position)', [red_green, green]],
                          ['121.500 MHz\n(ELT)','CHECKED', [red_green, green]],
                          ['Avionics','OFF', [red_green, green]],
                          ['Electrical\nconsumers','OFF', [red_green, green]],
                          ['Magnetos','OFF, KEY REMOVED', [red_green, green]],
                          ['NAV lights','OFF', [red_green, green]],
                          ['ALT1 & BAT','OFF', [red_green, green]],
                          ['Flight data &\ndocuments','NOTED &\nCOMPLETED', [red_green, green]],
                          ['Aircraft','TO BE SECURED', [red_green, green]],
                          ['PARKING CHECK','COMPLETED', [red_green, green]]
                          ]
             }
    return sfu_keys, sfu_checklist