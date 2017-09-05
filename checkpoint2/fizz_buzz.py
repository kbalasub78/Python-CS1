## Write a Python program which iterates the integers from 1 to 50.
## For multiples of three print "Fizz" instead of the number.
## For the multiples of five print "Buzz".
## For numbers which are multiples of both three and five print "FizzBuzz".
## Sample Output : 
## 1
## 2
## fizz
## 4 
## Buzz
##

## Loop through number list of 1 to 50
for num in range(51):
    if ( (0 == num % 3) and (0 == num % 5) ):
        ## Print FizzBuzz if num is a multiple of both 3 and 5
        print('FizzBuzz')
    elif (0 == num % 3):
        ## Print Fizz if num is a multiple of 3
        print('Fizz')
    elif (0 == num % 5):
        ## Print Buzz if num is a multiple of 5
        print('Buzz')
    else:
        ## Print num if it is neither a multiple of 3 or 5
        print(num)

