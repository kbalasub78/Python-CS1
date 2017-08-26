## parrot_trouble.py
## We have a loud talking parrot.
## The "hour" input is the current hour time in the range 0..23.
## We are in trouble if the parrot is talking (input True if talking and False if not)
## and the hour is before 7 or after 20.
## Return True if we are in trouble.
##
## import sys module for graceful data input handling
import sys

## Get input of current hour and if parrot is talking
while True:
    try:
        parrotTalking = input("Is the parrot talking now (True or False): ").lower()
        currHour = int(input("Enter the current hour (Range 0 to 23) : "))
        if( (currHour < 0 or currHour > 23) or \
            (parrotTalking != 'true' and parrotTalking != 'false')) :
            raise ValueError("Input data format is incorrect")
        else:
            break
    except:
        print("Error in data entered", sys.exc_info())

## Check if we are in trouble by validating the condition
if( (currHour < 7 or currHour > 20) and \
     (parrotTalking == 'true') ) :
    print("We are in trouble")
else :
    print("We are fine")
    
