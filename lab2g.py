#!/usr/bin/env python3

# Author: Kartik
# Author ID: k62
# Date Created: 2024/09/22

import sys  # Import sys to handle command-line arguments

# Check if a command-line argument was provided
if len(sys.argv) > 1:
    # If an argument is provided, assign it to timer (convert to integer)
    timer = int(sys.argv[1])
else:
    # If no argument is provided, default timer to 3
    timer = 3

# While loop to count down until timer reaches 0
while timer > 0:
    print(timer)  # Print the current value of the timer
    timer -= 1  # Decrease timer by 1

# Print blast off when the countdown ends
print('blast off!')

