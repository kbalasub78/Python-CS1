## Exercise 2: Write a program to prompt for a file name, and then read through
## the file and look for lines of the form:
## X-DSPAM-Confidence:0.8475
##
## When you encounter a line that starts with "X-DSPAM-Confidence:"
## pull apart the line to extract the floating-point number on the line.
## Count these lines and then compute the total of the spam confidence values
## from these lines.
## When you reach the end of the file, print out the average spam confidence.
##
import sys

spam_match_count = 0
spam_conf_total = 0
spam_conf_average = 0
fname = None

## Get a file handle to the input file
while True:
    try:
        fname = input('Enter file name: ')
        if('quit' == fname):
            raise RuntimeError('quit program')
        fhand = open(fname)
        break
    except RuntimeError as err:
        print(err)
        sys.exit()
    except:
        print('Incorrect file name')
        
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence'):
        continue

    spam_match_count = spam_match_count + 1
    
    line = line.rstrip()
    spam_conf_value = round( float( line[ line.find(':')+1: ] ), 2 )
    spam_conf_total = spam_conf_total + spam_conf_value
    print(spam_conf_value, spam_conf_total)

spam_conf_average = spam_conf_total/spam_match_count
print('Spam match count :', spam_match_count)
print('Spam confidence total :', spam_conf_total)
print('Spam confidence average : {:.2f}'.format(spam_conf_average) )
## print('Spam confidence average : ', spam_conf_average)
