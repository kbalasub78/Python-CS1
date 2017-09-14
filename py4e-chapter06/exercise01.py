## Exercise 1: Write a while loop that starts at the last character in the string
## and works its way backwards to the first character in the string,
## printing each letter on a separate line, except backwards.
##

def reverse_string(input_str):
    ## Get the length of input string and use it as initial index to work backwards
    index = len(input_str) - 1
    reverse_str = '' ## Trying to get reverse string additionally
    
    while index >= 0 :
        print(index, input_str[index]) ## print index and character at the index
        reverse_str = reverse_str + input_str[index] ## Keep appending characters to the reverse sting
        index = index -1
    return reverse_str

## Get two integer numbers as user input
name = ''
while not ( len(name) > 0 ):
    name = input("Enter the string to be reversed: ")
    if (len(name) == 0):
        print('Not a valid string input')

print( reverse_string(name) )
