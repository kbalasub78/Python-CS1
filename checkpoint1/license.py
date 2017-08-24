## Write a python program simulating driver's license provision.
## Accept the age of the driver and his total number of practice hours.
## If driver’s age is below 16, do not issue license.
## if 16 or above then check if number of practice hours is more than(ie. >) 200.
## if > 200, issue license otherwise don’t.

## Get user input for Age and practice hours
try:
    age = int( input ("Enter your age: ") )
    practice_hours = float( input ("Enter your practice hours: ") )
except:
    print('Error in data entered')
    sys.exit()

if (age < 16):
    print("License cannot be granted - age is less than 16")
else:
    if ( practice_hours > 200 ):
        print("License can be granted - age and practice hours conditions are met")
    else:
        print("License cannot be granted - practice hours is less than 200")
