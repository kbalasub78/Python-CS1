## cigar_party.py
## When squirrels get together for a party, they like to have cigars.
## A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
## Unless it is the weekend, in which case there is no upper bound on the number of cigars.
## Return True if the party with the given values is successful, or False otherwise.
##
## import sys module for graceful data input handling
import sys

def cigar_party(cigars, is_weekend):
    ## Check if the squirrel party was successful by validating the condition
    if( (is_weekend == False and (cigars >= 40 and cigars <= 60)) or \
        (is_weekend == True and cigars >= 40) ):
        return True
    else:
        return False
    
## Get input of current hour and if parrot is talking
while True:
    try:
        weekendFlag = input("Is it a weekend (True or False): ").title()
        if (weekendFlag != 'True' and weekendFlag != 'False') :
            raise ValueError()
        
        if(weekendFlag == 'True'): weekendFlag = True
        elif(weekendFlag == 'False'): weekendFlag = False
        
        break
    except ValueError:
        print("Weekend input should be True or False")
    
while True:
    try:
        cigarCount = int(input("Enter the number of cigars : "))
        break
    except:
        print("Cigar count shoud be an integer number")

if( cigar_party(cigarCount, weekendFlag) ):
    print("Squirrel party is successful")
else:
    print("Squirrel party is NOT successful")

#### Following is to check the function with different input values
##print( cigar_party(30, False) ) ## False
##print( cigar_party(50, False) ) ## True
##print( cigar_party(70, True) ) ## True
##print( cigar_party(30, True) ) ## False
##print( cigar_party(50, True) ) ## True
##print( cigar_party(60, False) ) ## True
##print( cigar_party(61, False) ) ## False
##print( cigar_party(40, False) ) ## True
##print( cigar_party(39, False) ) ## False
##print( cigar_party(40, True) ) ## True
##print( cigar_party(39, True) ) ## False
