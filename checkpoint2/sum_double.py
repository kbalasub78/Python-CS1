## sum_double.py
## Given two int values, return their sum.
## Unless the two values are the same, then return double their sum.
##
## import sys module for graceful data input handling
import sys

def sum_double(num1, num2):
    ## Calculate the sum. If integers are equal, double the sum
    sum = num1 + num2
    if num1 == num2:
        sum = 2 * sum
    return sum

## Get two integer numbers as user input
while True:
    try:
        number1 = int(input("Enter first integer number: "))
        break
    except:
        print("Number should be an integer")

while True:
    try:
        number2 = int(input("Enter second integer number: "))
        break
    except:
        print("Number should be an integer")
        
print( "Sum is : ", sum_double(number1, number2) )


#### Following is to check the function with different input values
##print(sum_double(1,2) ) ## 3
##print(sum_double(3,2) ) ## 5
##print(sum_double(2,2) ) ## 8
##print(sum_double(-1,0) ) ## -1
##print(sum_double(3,3) ) ## 12
##print(sum_double(0,0) ) ## 0
##print(sum_double(0,1) ) ## 1
##print(sum_double(3,4) ) ## 7

