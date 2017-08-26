## sum_double.py
## Given two int values, return their sum.
## Unless the two values are the same, then return double their sum.
##
## import sys module for graceful data input handling
import sys

## Get two integer numbers as user input

while True:
    try:
        num1 = int(input("Enter first integer number: "))
        num2 = int(input("Enter second integer number: "))
        break
    except:
        print("Error in data entered", sys.exc_info())

## Calculate the sum. If integers are equal, double the sum
sum = num1 + num2
if num1 == num2:
    sum = 2 * sum

print("Sum is : ", sum)
