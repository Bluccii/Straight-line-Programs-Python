# Import all necessary modules for the code.
import stdio
import sys

# Accept name (str) and age (str) as command-line arguments.
name = str(sys.argv[1]) # Saves first command-line argument as a string variable called "name"
age = int(sys.argv[2]) # Saves second command-line argument as a integer variable called "age"

# Write the message 'name is age years old.' to standard output.
stdio.writeln(f"{name} is {age} year(s) old.")
