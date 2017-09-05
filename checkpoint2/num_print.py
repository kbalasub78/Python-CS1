## Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
## Note : Use 'continue' statement. 
## Expected Output : 0 1 2 4 5 
##

## Use a for loop to go over list of 0 to 6
for num in range(0,7):
    if num in (3, 6):
        ## Proceed with next iteration without printing num value when num matches 3 or 6
        continue
    else:
        ## Print loop iteration num value
        print(num)
    
