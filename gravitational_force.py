# Import all necessary modules for the code.
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
G = 6.674e-11

# Calculates the value of gravitational force
f = G * m1 * m2 / (r ** 2)

# Displays the value of gravitational force as output
stdio.writeln(f)
