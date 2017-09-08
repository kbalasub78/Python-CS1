## parrot_trouble.py
## We have a loud talking parrot.
## The "hour" input is the current hour time in the range 0..23.
## We are in trouble if the parrot is talking (input True if talking and False if not)
## and the hour is before 7 or after 20.
## Return True if we are in trouble.
##
## import sys module for graceful data input handling
import sys

def parrot_trouble(talking, hour):
    ## Check if we are in trouble by validating the condition
    if( (hour < 7 or hour > 20) and (talking == True) ) :
        return("True - We are in trouble")
    else :
        return("False - We are fine")

## Get input of current hour and if parrot is talking
while True:
    try:
        parrotTalking = input("Is the parrot talking now (True or False): ").title()
        if( (parrotTalking != 'True' and parrotTalking != 'False') ):
            raise ValueError()
        
        if(parrotTalking == 'True'): parrotTalking = True
        elif(parrotTalking == 'False'): parrotTalking = False
        break
    except:
        print("Error in data entered")
   
while True:
    try:
        currHour = int(input("Enter the current hour (Range 0 to 23) : "))
        if(currHour < 0 or currHour > 23):
            raise ValueError()
        break
    except:
        print("Error in data entered")

print( parrot_trouble(parrotTalking, currHour) )

#### Following is to check the function with different input values
##print( parrot_trouble(True, 6) ) ## True
##print( parrot_trouble(True, 7) ) ## False
##print( parrot_trouble(False, 6) ) ## False
##print( parrot_trouble(True, 21) ) ## True
##print( parrot_trouble(False, 21) ) ## False
##print( parrot_trouble(False, 20) ) ## False
##print( parrot_trouble(True, 23) ) ## True
##print( parrot_trouble(False, 23) ) ## False
##print( parrot_trouble(True, 20) ) ## False
##print( parrot_trouble(False, 12) ) ## False
