## Exercise 2: Figure out which line of the above program is still not properly guarded.
## See if you can construct a text file which causes the program to fail and
## then modify the program so that the line is properly guarded and
## test it to make sure it handles your new text file.
## 

## Created a new file by name mbox-short1.txt and broke few lines 
## whose first word matches 'From', such that there is no word at index 2
fhand = open('mbox-short1.txt')

linecount = 0
for line in fhand:
    linecount += 1

    words = line.split()
    ## print('Debug:', words)
    
    if len(words) == 0 : continue
    if words[0] != 'From' : continue

    ## check if the line has 3rd word before accessing it
    ## if not print the line number that started with 'From'
    if len(words) < 3 :
        print(linecount) 
        continue

    ## Print the day along with the line number
    print(linecount, words[2])
