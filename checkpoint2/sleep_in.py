## sleep_in.py
## Write a program to accept Weekday and Vacation values.
## Weekday is True if it is a weekday and
## the vacation is True if we are on vacation.
## We sleep in if it is not a weekday or we're on vacation.
## Return True if we sleep in.
##

## import sys module for graceful data input handling
import sys

def sleep_in(wkday, vacation):
    ## Sleep in condition is met if it is not a weekday or if user is on vacation
    if ( vacation or not wkday ):
        return("Sleep-in is True")
    else:
        return("Sleep-in is False")

## Get user input if it is a weekday or on vacation
while True:
    try:
        weekday = input ("Is it a weekday? (True or False) :").title()
        if(weekday != 'True' and weekday != 'False'):
            raise ValueError()
        
        if(weekday == 'True'): weekday = True
        elif(weekday == 'False'): weekday = False
        break
    except:
        print("Weekday input should be True or False")

while True:
    try:
        vacation = input ("Are you on a vacation? (True or False) :").title()
        if (vacation != 'True' and vacation != 'False'):
            raise ValueError()

        if(vacation == 'True'): vacation = True
        elif(vacation == 'False'): vacation = False
        break
    except:
        print("Vacation input should be True or False")

print( sleep_in(weekday, vacation) )

#### Invoking sleep_in function to check for all possible values of weekday and vacation arguments
##print(sleep_in(True, True))   ## True
##print(sleep_in(True, False))  ## False
##print(sleep_in(False, True))  ## True
##print(sleep_in(False, False)) ## True
##
