# Import all necessary modules for the code.
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal.
n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
p = float(sys.argv[3])

# Declaring variable "q" which is used in calculations
q = 1 - p

# Calculations of the probabilities of p1 and p2
p1 = (1 - ((p/q) ** n2)) / (1 - ((p/q) ** (n1 + n2)))
p2 = (1 - ((q/p) ** n1)) / (1 - ((q/p) ** (n1 + n2)))

# Displays the probabilities of p1 and p2 as output
stdio.writeln(f"{p1} {p2}")
