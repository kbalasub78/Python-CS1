## monkey_trouble.py
## We have two monkeys, a and b. Accept the input telling if each is smiling.
## We are in trouble if they are both smiling or if neither of them is smiling.
## Return True if we are in trouble.

## import sys module for graceful data input handling
import sys

## Get user input telling if monkeys are smiling
while True:
    try:
        monkeyA_smiling = input("Is monkey A smiling (True or False): ").lower()
        monkeyB_smiling = input("Is monkey B smiling (True or False): ").lower()
        if( (monkeyA_smiling != 'true' and monkeyA_smiling != 'false') or \
            (monkeyB_smiling != 'true' and monkeyB_smiling != 'false')) :
            raise ValueError("Input data format is incorrect")
        else:
            break
    except:
        print("Error in data entered", sys.exc_info())
##        sys.exit()

## Check if both monkeys are smiling or if both monkeys are not smiling
## If so, print 'we are in trouble'

##if( (monkeyA_smiling == 'true' and monkeyB_smiling == 'true') or \
##    (monkeyA_smiling == 'false' and monkeyB_smiling == 'false') ) :
## Below line simplifies the if check
if( monkeyA_smiling == monkeyB_smiling):
    print("We are in trouble.. Returning True")
else:
    print("We are out of trouble. One of the monkey is not smiling..")
    
