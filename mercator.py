# Import all necessary modules for the code
import math
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal
φ = float(sys.argv[1])
λ = float(sys.argv[2])
φ_rad = math.radians(φ)

# Sets x to longitude (λ) and calculates the value for y
x = λ
y = math.log(((1 + math.sin(φ_rad))/(1 - math.sin(φ_rad)))) / 2

# Displays the x and y values as output, separated by a line
stdio.writeln(f"{x} {y}")
