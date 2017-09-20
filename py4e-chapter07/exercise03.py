## Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
## they add a harmless Easter Egg to their program Modify the program that prompts
## the user for the file name so that it prints a funny message when the user types
## in the exact file name "na na boo boo".
## The program should behave normally for all other files which exist and
## don't exist.
## 
import sys

subject_match_count = 0 ## Variable for storing the matching lines
fname = None ## File name

## Get a file handle to the input file
while True:
    try:
        fname = input('Enter file name: ')

        if('quit' == fname):
            ## Quit the program
            raise RuntimeError('quit program')
        elif('na na boo boo' == fname):
            ## Insert Easter egg
            raise RuntimeError("NA NA BOO BOO TO YOU - You have been punk'd!")
        
        ## Open the file provided by user
        fhand = open(fname)
        break
    except RuntimeError as err:
        print(err)
        sys.exit()
    except:
        ## Exception handling when file open has some issue
        print('File cannot be opened:', fname)
        
for line in fhand:
    ## Count the number of lines starting with 'Subject:'
    if not line.startswith('Subject:'):
        continue
    subject_match_count = subject_match_count + 1

print('There were', subject_match_count, 'subject lines in', fname)
