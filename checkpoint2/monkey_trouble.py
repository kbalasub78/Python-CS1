## monkey_trouble.py
## We have two monkeys, a and b. Accept the input telling if each is smiling.
## We are in trouble if they are both smiling or if neither of them is smiling.
## Return True if we are in trouble.

## import sys module for graceful data input handling
import sys

def monkey_trouble(monkeyA_smile, monkeyB_smile):
    ## Check if both monkeys are smiling or if both monkeys are not smiling
    ## If so, print 'we are in trouble'

    ##if( (monkeyA_smile == 'true' and monkeyB_smile == 'true') or \
    ##    (monkeyA_smile == 'false' and monkeyB_smile == 'false') ) :
    ## Below line simplifies the if check
    if( monkeyA_smile == monkeyB_smile):
        return True
    else:
        return False

## Get user input telling if monkeys are smiling
while True:
    try:
        monkeyA_smiling = input("Is monkey A smiling (True or False): ").title()
        monkeyB_smiling = input("Is monkey B smiling (True or False): ").title()

        if( (monkeyA_smiling != 'True' and monkeyA_smiling != 'False') or \
            (monkeyB_smiling != 'True' and monkeyB_smiling != 'False')) :
            raise ValueError()
        
        if(monkeyA_smiling == 'True'): monkeyA_smiling = True
        elif(monkeyA_smiling == 'False'): monkeyA_smiling = False
    
        if(monkeyB_smiling == 'True'): monkeyB_smiling = True
        elif(monkeyB_smiling == 'False'): monkeyB_smiling = False

        break
    except:
        print("Error in data entered")

if( monkey_trouble(monkeyA_smiling, monkeyB_smiling) ):
    print("We are in trouble.. Returning True")
else:
    print("We are out of trouble. One of the monkey is not smiling..")


## Following is to check the function with different input values
print( monkey_trouble(True, True) ) ## True
print( monkey_trouble(False, False) ) ## True
print( monkey_trouble(True, False) ) ## False
print( monkey_trouble(False, True) ) ## False
