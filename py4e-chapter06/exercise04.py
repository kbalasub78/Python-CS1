## Exercise 4:
## There is a string method called count that is similar to the function
## in the previous exercise.
## Read the documentation of this method at
## https://docs.python.org/3.5/library/stdtypes.html#string-methods
## and write an invocation that counts the number of times
## the letter 'a' occurs in "banana".

fruit = 'banana'

## 3 occurences of 'a' in the string 'banana'
print( fruit.count('a'), 'occurences of letter a found in word', fruit )
print( fruit.count('a',0,len(fruit)) ) ## This is same as above with start and end index given

## No error thrown even if start or end index is out of bounds
print( fruit.count('a',len(fruit)+2) ) ## output is 0
print( fruit.count('a',0,len(fruit)+2) ) ## output is 3

print( fruit.count('a', 3) ) ## output is 2 --> start search from index 2
print( fruit.count('a', 4) ) ## output is 1 --> start search from index 4
print( fruit.count('a',0,2) ) ## output is 1 --> start search from index 0 upto 2 (not including)

