## jacket.py
## Write a program to accept the temperature value and
## to tell a person to bring heavy jacket if temperature is < 20,
## if temperature is between 20 and 30, bring light jacket.
## if temperature > 30, do not bring any jacket.
##

## import sys module for graceful error handling
import sys

def check_jacket_type(temp):
    ## Check the range of temperature and suggest the type of jacket to wear
    if (temp < 20):
        return("Bring a heavy jacket")
    elif ( temp >= 20 and temp < 30):
        return("Bring a light jacket")
    elif(temp >= 30):
        return("No need of a jacket")

## Get user input for temperature
while True:
    try:
        temperature = float( input ("Enter the temperature: ") )
        break
    except:
        print('input temperature is not valid')

print( check_jacket_type(temperature) )

#### Following is to check the function with different input values
##print( check_jacket_type(20) ) ## Bring a light jacket
##print( check_jacket_type(30) ) ## No need of a jacket
##print( check_jacket_type(-20) ) ## Bring a heavy jacket
##print( check_jacket_type(10) ) ## Bring a heavy jacket
