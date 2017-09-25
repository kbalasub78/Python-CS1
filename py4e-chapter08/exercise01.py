## Exercise 1:
## Write a function called chop that takes a list and modifies it,
## removing the first and last elements, and returns None.
## Then write a function called middle that takes a list and
## returns a new list that contains all but the first and last elements.
##

## chop function modifies the input list by chopping the 1st and last element
def chop(inputlist):
    list_len = len(inputlist)
    if list_len == 1: del inputlist[0]
    elif list_len > 1:
        del inputlist[list_len - 1]
        del inputlist[0]

## middle function returns a new list containing all but the first and last element
def middle(inputlist):
    list_len = len(inputlist)

    ## Return an empty list, if the inputlist length is less than 3
    if list_len < 3: return []

    ## Create output list by slicing the input list
    ## with 1 as start index and last element as stop index
    outputlist = inputlist[1:list_len-1]
    return outputlist

count = 1
numlist = list(range(10,30,2))

while(len(numlist) > 0):
    print('Iteration #', count)
    count = count + 1

    ## chop function modifies the list directly
    print('original list is', numlist)
    chop(numlist)
    print('chopped list is', numlist)
    
    ## middle function returns a new list; input list is not modified
    print('middle list is', middle(numlist))
