import re
from collections import namedtuple

tMesswert = namedtuple('tMesswert', ['value', 'unit'])
tMesswert.__doc__ = """Messwert mit Wert und Einheit"""

def str2tupel(measurement_string):
    # Define a regular expression pattern to match a float number in exponential format and unit
    pattern = re.compile(r'([-+]?\d*\.\d+([eE][-+]?\d+)?|\d+([eE][-+]?\d+)?)\s*([a-zA-Zµ]+)')
    retval = tMesswert(0.0, "V")

    # Use the findall function to extract matches from the input string
    matches = pattern.findall(measurement_string)
    #print(matches)

    if matches:
        # The first match group contains the float number, and the  group contains the unit
        number, _, _, unit = matches[0]
        retval = tMesswert(float(number), unit)
    else:
        # Return None if no match is found
        retval = tMesswert(None, None)
    return retval

if __name__ == "__main__":
# Example usage:
    measurement_string = "0.23e-5µA"
    result = str2tupel(measurement_string)

    if result:
        number, unit = result
        print(f"Number by order: {number}, Unit: {unit}")
        print(f"Number by name: {result.value}, Unit: {result.unit}")
    else:
        print("No valid measurement found.")

    measurement_string = "NaN"
    result = str2tupel(measurement_string)
    print(result)

    if result:
        number, unit = result
        print(f"Number by order: {number}, Unit: {unit}")
        print(f"Number by name: {result.value}, Unit: {result.unit}")
    else:
        print("No valid measurement found.")

