## Write a program to read through a file and print the contents of the file
## (line by line) all in upper case.
## 
import sys

##fname = 'mbox-short.txt'
line_count = 0
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

## Print the contents of the file in Upper character set
for line in fhand:
    ## Call rstrip function to remove newline character at the end
    ## Call upper function to conver to upper characters
    line = line.rstrip().upper()
    print(line)
    
    ## Added below code to limit the number of lines printed in output for test purpose
    line_count = line_count + 1
    if(25 == line_count):
        sys.exit()

