## Exercise 3:
## Encapsulate this code in a function named count,
## and generalize it so that it accepts the string and the letter as arguments.
## 
## word = 'banana'
## count = 0
## for letter in word:
##     if letter == 'a':
##         count = count + 1
## print(count)

## Definition of count function
def count(word, search_letter):
    count = 0
    for letter in word:
        if letter == search_letter:
            count = count + 1
    return count

## Get input of the word
input_word = ''
while not ( len(input_word) > 0 ):
    input_word = input("Enter the string: ")
    if (len(input_word) == 0):
        print('Not a valid string input')

## Get input of the input letter to search within the word
input_letter = ''
while ( len(input_letter) != 1 ):
    input_letter = input("Enter the string: ")
    if (len(input_letter) != 1):
        print('Not a valid string input')

## print the count of occurence of letter in the input word
print( count(input_word, input_letter), 'occurences of letter', input_letter, 'found in word', input_word )
