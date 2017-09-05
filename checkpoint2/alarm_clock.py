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

def alarm_clock(dayValue, vacationFlag):
    ## Find alarm time by validating the condition
    if(dayValue == 0 or dayValue == 6):
        weekendFlag = True
    else:
        weekendFlag = False
    
    if vacationFlag == 'false' : ## Not on vacation
        if not weekendFlag :
            alarmValue = "7:00"
        else:
            alarmValue = "10:00"
    elif vacationFlag == 'true' : ## On vacation
        if not weekendFlag:
            alarmValue = "10:00"
        else:
            alarmValue = "Off"
    
    return alarmValue

## Get input of speed and birthday
while True:
    try:
        dayValue = int(input("Enter the day of the week (0=Sun, 1=Mon, 2=Tue,..,6=Sat) : "))
        vacationFlag = input("Are you on vacation (True or False): ").lower()
        if (vacationFlag != 'true' and vacationFlag != 'false') :
            raise ValueError("Input data format is incorrect")
        break
    except:
        print("Error in data entered", sys.exc_info())

## Print the alarm setting
print( "Alarm setting : ", alarm_clock( dayValue, vacationFlag) )

## alarm_clock function validation for different inputs
##print( alarm_clock( 1, 'false')) ## 7:00
##print( alarm_clock( 5, 'false')) ## 7:00
##print( alarm_clock( 0, 'false')) ## 10:00
##print( alarm_clock( 6, 'false')) ## 10:00
##print( alarm_clock( 0, 'true')) ## Off
##print( alarm_clock( 6, 'true')) ## Off
##print( alarm_clock( 1, 'true')) ## 10:00
##print( alarm_clock( 3, 'true')) ## 10:00
##print( alarm_clock( 5, 'true')) ## 10:00
