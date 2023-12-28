import pyvisa
class R6144:
    current = 0.0

    def __init__(self, rmhandle, gpibAdress):
        self.adress = gpibAdress
        self.rm = rmhandle
        self.handle = self.rm.open_resource("GPIB0::" + str(self.adress) + "::INSTR")
        self.handle.write("*RST")
        self.handle.write("*CLS")
        
    def set_current(self, current):
        pass
    def get_current(self):
        return self.current

    def close(self):
        self.handle.close()
        self.rm.close()
        