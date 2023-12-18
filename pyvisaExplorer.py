import pyvisa

# Connect to the instrument
rm = pyvisa.ResourceManager()
instrument = rm.open_resource('GPIB0::8::INSTR')

# Send commands to the instrument
instrument.write('*IDN?')
response = instrument.read()

# Print the instrument's response
print(response)

# Close the connection
instrument.close()
rm.close()
