## Write a program to accept Weekday and Vacation values.
## Weekday is True if it is a weekday and
## the vacation is True if we are on vacation.
## We sleep in if it is not a weekday or we're on vacation.
## Return True if we sleep in.
##

## import sys module for graceful data input handling
import sys

## Get user input if it is a weekday or on vacation
try:
    weekday = input ("Is it a weekday? (True or False) :").lower()
    vacation = input ("Is it a vacation? (True or False) :").lower()
    if( (weekday != 'true' and weekday != 'false') or \
        (vacation != 'true' and vacation != 'false') ):
        raise ValueError("Input data format is incorrect")
except:
    print("Input data format is incorrect")
    sys.exit()

if ( weekday != 'true' or vacation == 'true' ):
    print("Sleep-in is True")
else:
    print("Sleep-in is False")
