# Import all necessary modules for the code.
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Finds the smallest (minimum) and largest (maximum) numbers
# out of the values of x, y and z
α = min(x, y, z)
ω = max(x, y, z)

# In order to calculate the "Middle Value" we use the min & max value and
# subtract it from the total value of all numbers to get the "Mid-Value"
middle_value = x + y + z - α - ω

# Displays the numbers in ascending order as output
stdio.writeln(f"{α} {middle_value} {ω}")
