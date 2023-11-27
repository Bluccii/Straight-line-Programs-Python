# Import all necessary modules for the code.
import math
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
angle_1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])
angle_1_rad = math.radians(angle_1)

# Calculates the angle of refract,
# and then converts the radian value into a degrees
angle_2 = (n1 * (math.sin(angle_1_rad))) / n2
angle_asin = math.asin(angle_2)
angle_of_refract = math.degrees(angle_asin)

# Displays the value for the angle of refraction as output
stdio.writeln(angle_of_refract)
