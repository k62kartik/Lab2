#!/usr/bin/env python3

import sys  # Import the sys module to access command-line arguments

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument after script name
age = int(sys.argv[2])  # Second argument after script name (converted to integer)

# Output the exact message as per the sample runs
print('Hi ' + name + ', you are ' + str(age) + ' years old.')
