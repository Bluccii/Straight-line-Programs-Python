# Import all necessary modules for the code.
import math
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
λ = float(sys.argv[1])
t = float(sys.argv[2])

# Calculates the probability
p = math.exp(-λ * t)

# Displays "the probability that one has to wait longer than t" as output
stdio.writeln(p)
