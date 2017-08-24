## Write a program to accept the temperature value and
## to tell a person to bring heavy jacket if temperature is < 20,
## if temperature is between 20 and 30, bring light jacket.
## if temperature > 30, do not bring any jacket.
##

## import sys module for graceful error handling
import sys

#### Get user input for temperature
try:
    temperature = float( input ("Enter the temperature: ") )
except:
    print('Error in data entered')
    sys.exit()

if (temperature < 20):
    print("Bring a heavy jacket")
elif ( temperature >= 20 and temperature < 30):
    print("Bring a light jacket")
elif(temperature >= 30):
    print("No need of a jacket")
