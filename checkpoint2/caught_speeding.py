## caught_speeding.py
## You are driving a little too fast, and a police officer stops you.
## Write code to compute the result, encoded as an int value:
## 0=no ticket, 1=small ticket, 2=big ticket.
## If speed is 60 or less, the result is 0.
## If speed is between 61 and 80 inclusive, the result is 1.
## If speed is 81 or more, the result is 2.
## Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
##
## import sys module for graceful data input handling
import sys

## caught_speeding function definition
def caught_speeding(speed, is_birthday):
    speedRange1 = 60 # Speed of 60
    speedRange2 = 80 # Speed of 80

    ## Speed range relaxed by 5 if it is driver's birthday
    if is_birthday == True:
        speedRange1 = speedRange1 + 5
        speedRange2 = speedRange2 + 5
        
    ## Check the ticket issuance by validating the speed range
    if speed <= speedRange1:
        ticket = 0
    elif (speed > speedRange1 and speed <= speedRange2):
        ticket = 1
    elif speed > speedRange2:
        ticket = 2
    
    return ticket

## Get input of speed and birthday
while True:
    try:
        vehicleSpeed = float(input("Enter the speed of the vehicle : "))
        break
    except:
        print("Enter speed as numeric number")
        
while True:
    try:
        bdayFlag = input("Is today driver birthday (True or False): ").title()
        if (bdayFlag != 'True' and bdayFlag != 'False') :
            raise ValueError()
        
        if(bdayFlag == 'True'): bdayFlag = True
        elif(bdayFlag == 'False'): bdayFlag = False
        
        break
    except ValueError:
        print("Birthday information input should be True or False")

print( "Ticket is : ", caught_speeding(vehicleSpeed, bdayFlag) )

