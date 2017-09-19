## Write a program to read through a file and print the contents of the file
## (line by line) all in upper case.
## 
import sys

fname = 'mbox-short.txt'
line_count = 0

## Get a file handle to the input file
fhand = open(fname)

for line in fhand:
    ## Call rstrip function to remove newline character at the end
    ## Call upper function to conver to upper characters
    line = line.rstrip().upper()
    print(line)
