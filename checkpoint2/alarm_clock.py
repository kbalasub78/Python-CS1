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
        if day in range(1,6) : ## Weekdays
            alarm = "7:00"
        else: ## Week-ends
            alarm = "10:00"
    elif onVacation : ## On vacation
        if day in range(1,6): ## Weekdays
            alarm = "10:00"
        else: ## Week-ends
            alarm = "Off"
    
    return alarm

## Get input of speed and birthday
while True:
    try:
        dayValue = int(input("Enter the day of the week (0=Sun, 1=Mon, 2=Tue,..,6=Sat) : "))
        if (dayValue not in range(0,7) ) :
            raise ValueError()
        break
    except ValueError:
        print("Day of the week input should be in range of 0 to 6")

while True:
    try:
        vacation = input("Are you on vacation (True or False): ").title()
        if (vacation != 'True' and vacation != 'False') :
            raise ValueError()

        if(vacation == 'True'): vacationFlag = True
        elif(vacation == 'False'): vacationFlag = False

        break
    except ValueError:
        print("Vacation input should be True or False")

## Print the alarm setting
print( "Alarm setting : ", alarm_clock( dayValue, vacationFlag) )

## Following is test the function code for various input values
##print( alarm_clock( 1, False)) ## 7:00
##print( alarm_clock( 5, False)) ## 7:00
##print( alarm_clock( 0, False)) ## 10:00
##print( alarm_clock( 6, False)) ## 10:00
##print( alarm_clock( 0, True)) ## Off
##print( alarm_clock( 6, True)) ## Off
##print( alarm_clock( 1, True)) ## 10:00
##print( alarm_clock( 3, True)) ## 10:00
##print( alarm_clock( 5, True)) ## 10:00
