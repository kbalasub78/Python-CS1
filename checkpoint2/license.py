## license.py
## Write a python program simulating driver's license provision.
## Accept the age of the driver and his total number of practice hours.
## If driver’s age is below 16, do not issue license.
## if 16 or above then check if number of practice hours is more than(ie. >) 200.
## if > 200, issue license otherwise don’t.

## import sys module for error handling
import sys

def grant_license(age, practice_hours):
    ## Check if the drivers age is above 16 and has practiced for more than 200 hours
    if (age < 16):
        return("License cannot be granted - age is less than 16")
    else:
        if ( practice_hours > 200 ):
            return("License can be granted - age and practice hours conditions are met")
        else:
            return("License cannot be granted - practice hours is less than 200")

## Get user input for Age and practice hours
while True:
    try:
        age = int( input ("Enter your age: ") )
        practice_hours = float( input ("Enter your practice hours: ") )
        break
    except:
        print('Error in data entered')

print( grant_license(age, practice_hours) )

#### Following is to check the function with different input values
##print( grant_license(15, 300) ) ## License cannot be granted - age is less than 16
##print( grant_license(14, 50) ) ## License cannot be granted - age is less than 16
##print( grant_license(16, 300) ) ## License can be granted - age and practice hours conditions are met
##print( grant_license(20, 190) ) ## License cannot be granted - practice hours is less than 200
