import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.
expr = None
if x + y <= z:
    expr = False
elif y + z <= x:
    expr = False
elif x + z <= y:
    expr = False
else:
    expr = True
# If statements determining the status of "expr" based on the values of x, y and z.

# Write expr to standard output.
stdio.writeln(expr)
