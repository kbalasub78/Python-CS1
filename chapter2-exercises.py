print('Chapter 2 - Excerise 2')
# Get user input for name
name = input('Enter your name: ')
print('Hello ' + name )
print()

print('Chapter 2 - Excerise 3')
# Get user input for hours and rate
hours = float( input('Enter Hours: ') )
rate = float( input('Enter Rate: ') )
pay = hours * rate
print('Pay: ' + str(pay) )
print()

print('Chapter 2 - Exercise 4')
width = 17
height = 12.0

print(width//2) # Answer should be quotient which is 8
print(width/2.0) # Answer should be 8.5 (floating number)
print(height/3) # Answer should be 4.0 (floating number)

# Answer should be 11, assuming enter is done after \
print(1 + 2 \
  * 5)
print()


#T(°F) = T(°C) × 1.8 + 32
print('Chapter 2 - Exercise 5')
# Get user input for temperature in celsius
temp_cels = float( input('Enter Temperature in Celsius: ') )
temp_fahr = (temp_cels * 1.8) + 32
print('Temperature in Fahrenheit is: ' + str(temp_fahr) )
print()
