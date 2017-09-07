## alarm_clock.py
## Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and
## a boolean indicating if we are on vacation,
## return a string of the form "7:00" indicating when the alarm clock should ring.
## Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
## Unless we are on vacation
## -- then on weekdays it should be "10:00" and weekends it should be "off".
##

## import sys module for graceful data input handling
import sys

## alarm_clock module definition
def alarm_clock(day, onVacation):    
    if not onVacation : ## Not on vacation
        if day in range(1,6) :
            alarm = "7:00"
        else:
            alarm = "10:00"
    elif onVacation : ## On vacation
        if day in range(1,6):
            alarm = "10:00"
        else:
            alarm = "Off"
    
    return alarm

## Get input of speed and birthday
while True:
    try:
        dayValue = int(input("Enter the day of the week (0=Sun, 1=Mon, 2=Tue,..,6=Sat) : "))
        vacation = input("Are you on vacation (True or False): ").title()
        if (vacation != 'True' and vacation != 'False') :
            raise ValueError("Input data format is incorrect")

        if(vacation == 'True'): vacationFlag = True
        elif(vacation == 'False'): vacationFlag = False

        break
    except:
        print("Error in data entered", sys.exc_info())

## Print the alarm setting
print( "Alarm setting : ", alarm_clock( dayValue, vacationFlag) )
