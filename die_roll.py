# Import all necessary modules for the code.
import stdio
import stdrandom
import sys

# Variables defined via Command-line Argument input from the terminal.
n = int(sys.argv[1])

# Simulates two die rolls and then computes the sum value of both rolls
roll_1 = stdrandom.uniformInt(1, n + 1)
roll_2 = stdrandom.uniformInt(1, n + 1)
roll_sum = roll_1 + roll_2

# Displays the sum value of both die rolls as output
stdio.writeln(roll_sum)
