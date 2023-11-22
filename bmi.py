import stdio
import sys

# Accept weight (float) and height (float) as command-line arguments.
weight = float(sys.argv[1]) # Saves first command-line argument as a float var called "weight"
height = float(sys.argv[2]) # Saves second command-line argument as a float var called "height"

# Set bmi to weight divided by square of height.
bmi = weight/(height ** 2) # Calculates the Body-Mass Index using weight and height.

# Write bmi to standard output.
stdio.writeln(bmi)
