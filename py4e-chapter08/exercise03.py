## Exercise 3: Rewrite the guardian code in the above example without two if statements.
## Instead, use a compound logical expression using the and logical operator
## with a single if statement.
##
fhand = open('mbox-short1.txt')
linecount = 0

for line in fhand:
    linecount += 1

    words = line.split()
    ## print('Debug:', words)
    
    ## Print the third word if the first word matches 'From'
    ## Guard the access by checking if the number of words in the line is more than 2
    if( (len(words) > 2) and (words[0] == 'From')):
        print(linecount, words[2])
