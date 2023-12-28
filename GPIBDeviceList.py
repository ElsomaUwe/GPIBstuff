
#define a dict to store the GPIB address of each device
#the key is the device name, the value is the GPIB address
#fill with some default values
gpibDevAdr = {"HP4192A":1,
              "HP66309D":6,
              "Keithley2700":8,
              "R6144":17
              }

#this function adds a device to the list
def addDevice(name, adress):
    gpibDevAdr[name] = adress

#this function removes a device from the list
def removeDevice(name):
    del gpibDevAdr[name]

