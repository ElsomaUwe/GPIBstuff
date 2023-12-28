import pyvisa
class R6144:
    current = 0.0

    def __init__(self, rmhandle, gpibAdress):
        self.adress = gpibAdress
        self.rm = rmhandle
        self.handle = self.rm.open_resource("GPIB0::" + str(self.adress) + "::INSTR")
        self.handle.write("*RST")
        self.handle.write("*CLS")

    def write(self, command):
        self.handle.write(command)
 
    def setDC_V(self, voltage):
        #write voltage to R6144 with format D{voltage} and 3 digits after decimal point
        self.write("D{:.3f}V".format(voltage))

    def setDC_mV(self, voltage):
        #write voltage to R6144 with format D{voltage} and 3 digits after decimal point
        self.write("D{:.3f}MV".format(voltage))

    def setDC_mA(self, current):
        #write current to R6144 with format D{current} and 3 digits after decimal point
        self.write("D{:.3f}MA".format(current))

        pass
    def get_current(self):
        return self.current

    def close(self):
        self.handle.close()
        self.rm.close()
