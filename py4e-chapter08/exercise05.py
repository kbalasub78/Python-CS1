## Exercise 5: Write a program to read through the mail box data and
## when you find line that starts with "From", you will split the line
## into words using the split function.
## We are interested in who sent the message, which is the second word
## on the From line.
##

fhand = open('mbox-short.txt')
from_count = 0

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    if len(words) > 1:
        print(words[1])
        from_count += 1

print('There were', from_count, 'lines in the file with From as the first word')
