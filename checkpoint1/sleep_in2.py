## Write a program to accept Weekday and Vacation values.
## Weekday is True if it is a weekday and
## the vacation is True if we are on vacation.
## We sleep in if it is not a weekday or we're on vacation.
## Return True if we sleep in.
##

## function to check if sleep_in conditions are met and return values accordingly
def sleep_in(wkday, vacation_flag):
    if ( wkday != 'true' or vacation_flag == 'true' ):
        return('Sleep-in is True')
    else:
        return('Sleep-in is False')

## Invoking sleep_in function to check for all possible values of weekday and vacation arguments
print(sleep_in('true', 'true'))
print(sleep_in('true', 'false'))
print(sleep_in('false', 'true'))
print(sleep_in('false', 'false'))
