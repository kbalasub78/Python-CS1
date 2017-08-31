## Chapter 5 - Exercise 01
## Write a program which repeatedly reads numbers until the user enters "done".
## Once "done" is entered, print out the total, count, and average of the numbers.
## If the user enters anything other than a number, detect their mistake using
## try and except and print an error message and skip to the next number.
##
## import sys module for graceful data input handling
import sys

numTotal = 0
numCount = 0
numAverage = 0

## Get numbers as input from user
while True:
    userInput = input("Enter a number: ")
    if(userInput == 'done'):
        break

    try:
        ## Convert the input into number. This will implicitly validate if entered input is a number
        numInput = int(userInput)
    except:
        print("Invalid input")
        continue

    numCount += 1 ## Increment numbers count for valid number entries
    numTotal += numInput ## Add input number to Total

numAverage = numTotal / numCount

print("Total: ", numTotal, " Count: ", numCount, " Average: ", numAverage)
