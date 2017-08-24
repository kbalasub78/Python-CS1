## Chapter 4 - Exercise 6
## Rewrite your pay computation with time-and-a-half for overtime and
## create a function called computepay which takes two parameters (hours and rate).

## import sys module for graceful data input handling
import sys

## computepay function definition
def computepay(hours, rate):
    if hours <= 40 :
        pay = hours * rate
    else :
        pay = (40 * rate) + ( (hours - 40) * (rate * 1.5) )

    return pay

# Get user input for hours and rate
try:
    hours = float( input("Enter Hours: ") )
    rate = float( input("Enter Rate: ") )
except:
    print("Error in data entered")
    sys.exit()

pay = computepay(hours, rate)
print('Pay: ' + str(pay) )
