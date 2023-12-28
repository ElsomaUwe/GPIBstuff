import re

def str2num(measurement_string):
    # Define a regular expression pattern to match a float number in exponential format and unit
    pattern = re.compile(r'([-+]?\d*\.\d+([eE][-+]?\d+)?|\d+([eE][-+]?\d+)?)\s*([a-zA-Zµ]+)')

    # Use the findall function to extract matches from the input string
    matches = pattern.findall(measurement_string)

    if matches:
        # The first match group contains the float number, and the fourth group contains the unit
        number, _, _, unit = matches[0]
        return float(number), unit
    else:
        # Return None if no match is found
        return None

if __name__ == "__main__":
# Example usage:
    measurement_string = "1.23e-5µA,200234SEC"
    result = str2num(measurement_string)

    if result:
        number, unit = result
        print(f"Number: {number}, Unit: {unit}")
    else:
        print("No valid measurement found.")
