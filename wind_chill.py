# Import all necessary modules for the code.
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
t = float(sys.argv[1])
v = float(sys.argv[2])

# Calculates the value of wind chill.
w = 35.74 + (0.6215 * t) + (0.4275 * t - 35.75) * (v ** 0.16)

# Displays the value of wind chill as output.
stdio.writeln(w)
