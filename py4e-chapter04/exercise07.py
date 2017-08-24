## Chapter 4 - Exercise 7
## Rewrite the grade program from the previous chapter
## using a function called computegrade that takes a score as its parameter
## and returns a grade as a string.

## import sys module for graceful data input handling
import sys

## computegrade function definition
def computegrade(score):
    if (score < 0.0 or score > 1.0) : grade='Bad score'
    elif score >= 0.9 : grade='A'
    elif score >= 0.8 : grade='B'
    elif score >= 0.7 : grade='C'
    elif score >= 0.6 : grade='D'
    elif score < 0.6 : grade='F'
    return grade

def main():
    # Get user input for score
    try:
        score = float( input('Enter score (range from 0.0 to 1.0): ') )
    except:
        print('Bad score..out of range')
        sys.exit()
    
    ## Invoke computegrade function to check the grade for the score inputted
    print(computegrade(score))

main()
