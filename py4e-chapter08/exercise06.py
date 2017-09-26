## Exercise 6: Rewrite the program that prompts the user for a list of numbers
## and prints out the maximum and minimum of the numbers at the end when the user
## enters "done". Write the program to store the numbers the user enters in a
## list and use the max() and min() functions to compute the maximum and
## minimum numbers after the loop completes.
##

num_list = list()
while True:
    try:
        user_input = input('Enter a number: ')
        if user_input.lower() == 'done':
            break
        number = float(user_input)
    except:
        print('Enter a valid number')
        continue
    num_list.append(number)

print(num_list)
print('Maximum of all numbers entered:', max(num_list) )
print('Minimum of all numbers entered:', min(num_list) )

print('Total numbers entered:', len(num_list))
print('Sum of all numbers entered:', sum(num_list))
print('Average of all numbers entered:', sum(num_list)/len(num_list) )
