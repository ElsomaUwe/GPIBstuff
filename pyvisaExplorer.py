import pyvisa
from GPIBDeviceList import gpibDevAdr
import Keithley2700
from Keithley2700 import DmmResult
import R6144
from collections import namedtuple
import os

clear = lambda: os.system('cls')
#defune global variables
dmm = None
def startupProcedure():
    global dmm,rm
    clear()
    print("Startup procedure")
    print("1. Check if GPIB-USB adapter is connected")
    # Connect to USB-GPIB adapter using try/except and print error if not found
    try:
        rm = pyvisa.ResourceManager()
    except:
        print("No USB-GPIB adapter found")
        exit()

    # connect to Keithley 2700 using try/except and print error if not found
    print("2. Check if Keithley 2700 is connected")
    try:
        dmm = Keithley2700.Keithley2700(rm,gpibDevAdr["Keithley2700"])
    except:
        print("No Keithley 2700 found")
        exit()
    dmm.reset()

    # connect to R6144 using try/except and print error if not found
    print("3. Check if R6144 is connected")     
    try:
        vsrc = R6144.R6144(rm, gpibDevAdr["R6144"])
    except:
        print("No R6144 found")
        exit()

startupProcedure()

# prepare Multimeter
print("4. Set Multimeter to DC Voltage")
dmm.setVDC()
dmm.setValueOnly()
#dmm.mpxclose(1,12)

print("5. Start measurement")
dmmResult = dmm.getVDC()
print(f"Voltage: {dmmResult[0].value:.4e} {dmmResult[0].unit} at T={dmmResult[1].value:.2e}{dmmResult[1].unit}")

# Close the connection
dmm.close()
rm.close()
