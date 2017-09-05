## Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess.
## If the user guesses wrong then the prompt appears again until the guess is correct.
## On successful guess, user will get a "Well guessed!" message,
## and the program will exit
##

## import random module
import random

## Initialize guess number
guessNum = None

## Get the target guess number using randint function
targetNum = random.randint(1, 9)
print(targetNum); ## Printing just for debugging

while True:
    ## Check if guess number matches the target number
    if (targetNum != guessNum):
        ## Guessed number did not matach the target number, ask user to guess
        try:
            guessNum = int(input('Guess a number between 1 and 9 : '))
        except:
            ## Most likely exception due to integer conversion
            print('Invalid entry')
    else :
        ## Guessed number mataches the target number
        print('Well guessed!')
        break
