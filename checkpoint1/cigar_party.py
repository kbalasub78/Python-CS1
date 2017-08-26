## cigar_party.py
## When squirrels get together for a party, they like to have cigars.
## A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
## Unless it is the weekend, in which case there is no upper bound on the number of cigars.
## Return True if the party with the given values is successful, or False otherwise.
##
## import sys module for graceful data input handling
import sys

## Get input of current hour and if parrot is talking
while True:
    try:
        weekendFlag = input("Is it a weekend (True or False): ").lower()
        if (weekendFlag != 'true' and weekendFlag != 'false') :
            raise ValueError("Input data format is incorrect")
        cigarCount = int(input("Enter the number of cigars : "))
        break
    except:
        print("Error in data entered", sys.exc_info())

## Check if the squirrel party was successful by validating the condition
if( (weekendFlag == 'false' and (cigarCount >= 40 and cigarCount <= 60)) or \
    (weekendFlag == 'true' and cigarCount >= 40) ):
    print("Squirrel party is successful")
else:
    print("Squirrel party is NOT successful")

