# Import all necessary modules for the code.
import math
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Converts variable values from degrees (°) to radians.
x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)

# Separates expressions to minimize long lines of code.
expr_1 = math.sin(x1_rad) * math.sin(x2_rad)
expr_2 = math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad-y2_rad)
expr = expr_1 + expr_2

# Calculates the value of great-circle distance.
d = 6359.83 * math.acos(expr)

# Displays d, the great-circle distance as output.
stdio.writeln(d)
