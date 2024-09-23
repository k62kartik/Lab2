#!/usr/bin/env python3

import sys  # Import sys module to access command-line arguments

# Check if exactly 2 arguments (plus the script name) are provided
if len(sys.argv) != 3:
    # If the number of arguments is not 3, print a usage message and exit with code 0
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Exit with a status code of 0 instead of 1

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument after script name
age = sys.argv[2]  # Second argument after script name (kept as a string for simplicity)

# Output the exact message as per the sample runs
print(f'Hi {name}, you are {age} years old.')
