from auxstuff import str2num
from collections import namedtuple

DmmResult = namedtuple('DmmResult', ['value', 'unit', 'tstamp', 'tunit'])

class Keithley2700(object):
    name = 'Keithley 2700'
    adress = None
    rm = None
    handle = None

    def __init__(self, rmhandle, gpibAdress):
        self.adress = gpibAdress
        self.rm = rmhandle
        self.handle = self.rm.open_resource("GPIB0::" + str(self.adress) + "::INSTR")
        self.handle.write("*RST")
        self.handle.write("*CLS")

    def write(self, command):
        self.handle.write(command)

    def read(self):
        self.handle.write(':READ?')
        return self.handle.read()

    def close(self):
        self.handle.close()

    def reset(self):
        self.write('*RST')
    
    def setValueOnly(self):
        self.handle.write(':FORM:ELEM READ,UNIT,TST')

    def setVDC(self):
        self.handle.write(":SENSe:FUNCtion 'VOLT:DC'")
    
    def setVAC(self):
        self.handle.write(":SENSe:FUNCtion 'VOLT:AC'")
    
    def setIDC(self):
        self.handle.write(":SENSe:FUNCtion 'CURR:DC'")

    def setIAC(self):
        self.handle.write(":SENSe:FUNCtion 'CURR:AC'")

    def set2W(self):
        self.handle.write(":SENSe:FUNCtion 'FRES'")
    
    def set4W(self):
        self.handle.write(":SENSe:FUNCtion 'FRES'")

    def setTemp(self):
        self.handle.write(":SENSe:FUNCtion 'TEMP'")

    def setFreq(self):
        self.handle.write(":SENSe:FUNCtion 'FREQ'")

    def setPeriod(self):
        self.handle.write(":SENSe:FUNCtion 'PER'")
    
    def setCont(self):
        self.handle.write(":SENSe:FUNCtion 'CONT'")

    def trigger(self):
        self.handle.write(":INIT:IMMediate")

    def mpxclose(self,slot,ch):
        #slot is single digit, ch is 2 digit concatenated as 3 digit number appended to the @ sign
        print(":ROUTe:CLose (@{a:01d}{b:02d})".format(a=slot,b=ch))
        self.handle.write(":ROUTe:CLose (@{a:01d}{b:02d})".format(a=slot,b=ch))

    def setNPLC(self, nplc):
        self.handle.write(":SENSe:VOLTage:DC:NPLCycles " + str(nplc))

    def getVDC(self):
        result = self.read()
        result = result.split(',')
        print(result)
        value,unit = str2num(result[0])
        #split the timestamp into time and unit discard the unit
        tstamp,tunit = str2num(result[1])
        return(value,unit,tstamp, tunit)

   