# Import all necessary modules for the code
import stdio
import sys

# Variables defined via Command-line Argument input from the terminal
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Calculation for the day of the week (as a number)
# 0 = Sunday, 1 = Monday, 2 = Tuesday, etc
y0 =  y - (14-m)//12
x0 = y0 + (y0//4) - (y0//100) + (y0//400)
m0 = m + 12 * ((14 - m)// 12) - 2
dow = (d + x0 + 31 * m0//12) % 7

# If statements to determine the string representation of the day of the week
dow_string = None # Creates an Empty String
if dow == 0:
    dow_string = "Sunday"
elif dow == 1:
    dow_string = "Monday"
elif dow == 2:
    dow_string = "Tuesday"
elif dow == 3:
    dow_string = "Wednesday"
elif dow == 4:
    dow_string = "Thursday"
elif dow == 5:
    dow_string = "Friday"
elif dow == 6:
    dow_string = "Saturday"

# Displays the day of the week as the output
stdio.writeln(f"The date, {m}/{d}/{y}, falls on a {dow_string}.")