# Import all necessary modules for the code.
import stdio
import sys

# Accept name1 (str), name2 (str), and name3 (str) as command-line arguments.
name1 = str(sys.argv[1]) # Saves first command-line argument as a string variable called "name1"
name2 = str(sys.argv[2]) # Saves second command-line argument as a string variable called "name2"
name3 = str(sys.argv[3]) # Saves third command-line argument as a string variable called "name3"

# Write 'Hi name3, name2, and name1.' to standard output.
stdio.writeln(f"Hi {name3}, {name2}, and {name1}. ")
