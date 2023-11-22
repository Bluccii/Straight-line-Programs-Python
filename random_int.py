# Import all necessary modules for the code.
import stdio
import stdrandom
import sys

# Accept a (int) and b (int) as command-line arguments.
a = int(sys.argv[1]) # Saves first command-line argument as an integer var called "a"
b = int(sys.argv[2]) # Saves second command-line argument as an integer var called "b"

# Set r to a random integer between a and b, obtained by calling stdrandom.uniformInt().
r = stdrandom.uniformInt(a, b) # Setting r to a random number between [a, b)

# Write r to standard output.
stdio.writeln(r)
