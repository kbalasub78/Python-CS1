## Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt
## Write a program to open the file romeo.txt and read it line by line.
## For each line, split the line into a list of words using the split function.
## For each word, check to see if the word is already in a list.
## If the word is not in the list, add it to the list.
## When the program completes, sort and print the resulting words
## in alphabetical order.
##
fhand = open('romeo.txt')
linecount = 0
wordcount = 0

## initialize words_list
words_list = list()

for line in fhand:
    ## Go over each line in the file
    linecount += 1
    words = line.split()
    
    for word in words:
        wordcount += 1
        ## Scan through each word and check if it is already part of words_list
        if word.lower() not in words_list: words_list.append(word.lower())

## Sort and print the words list
print('List before sorting:')
print(words_list)
print('')

words_list.sort()
print('List after sorting:')
print(words_list)
print('')

## Print the words in the file and unique words as captured in the words list
print('Total words in the file is :', wordcount)
print('Total unique words in the list is:', len(words_list))
