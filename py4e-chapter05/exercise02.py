## Chapter 5 - Exercise 02
## Write another program that prompts for a list of numbers as above and at the
## end prints out both the maximum and minimum of the numbers instead of the average.
##
## import sys module for graceful data input handling
import sys

numTotal = 0
numCount = 0
numMax = None
numMin = None

## Get numbers as input from user
while True:
    userInput = input("Enter a number: ")
    if(userInput == 'done'):
        break

    try:
        numInput = int(userInput)
    except:
        print("Invalid input")
        continue

    numCount += 1 ## Increment numbers count for valid number entries
    numTotal += numInput ## Add input number to Total

    # Check if input number is bigger than the max number
    if(numMax is None or numInput > numMax):
        numMax = numInput

    # Check if input number is smaller than the min number
    if(numMin is None or numInput < numMin):
        numMin = numInput

# Print Total, Count, Maximum and Minimum numbers
print("Total: ", numTotal, " Count: ", numCount, " Max number: ", numMax, " Min number: ", numMin )
