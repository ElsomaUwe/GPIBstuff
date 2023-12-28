import pyvisa
from GPIBDeviceList import gpibDevAdr
import Keithley2700
from Keithley2700 import DmmResult
import R6144
from collections import namedtuple
import os
import time
import matplotlib.pyplot as plt
import numpy as np

clear = lambda: os.system('cls')
#defune global variables
dmm = None
vsrc = None
rm = None
voltage = 0.0
vstart = -0.00001
vstop = 0.00001
vstep = 0.0000001

def startupProcedure():
    global dmm,rm,vsrc
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

# prepare Voltage Source
print("5. Set Voltage Source to 0.0V and turn it on")
voltage = vstart
vsrc.setDC_V(vstart)
vsrc.write("E1")
time.sleep(1)
resultlist = []

print("6. Start measurement loop")
j=0
while True:
    vsrc.setDC_V(voltage)
    time.sleep(0.1)
    [spg,tstamp] = dmm.getVDC()

    print(f"Voltage: {spg.value:.4e} {spg.unit}")
    try:
        delta = (spg.value - voltage)
    except:
        delta = 0.0
    resultlist.append((j,spg.value,spg.unit,voltage,delta))
    
    voltage = voltage + vstep
    j = j + 1
    if voltage > vstop + 1E-10:
        break
 
# turn off voltage source
vsrc.write("H1")

# Close the connection
dmm.close()
vsrc.close()
rm.close()

print("7. Finished")
#print(resultlist)
x = np.array(resultlist,dtype=[('i',float),('value',float),('unit',object),('voltage',float),('delta',float)])
#now plot a dot diagram of the results
plt.figure()

plt.plot(x['voltage'],x['delta'],'o')
#set grid on
plt.grid()
#plt.xticks(np.arange(0,len(x['i']),1))
plt.show()


