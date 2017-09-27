## Exercise 2: Write a program that categorizes each mail message by which day
## of the week the commit was done. To do this look for lines that start with
## "From", then look for the third word and keep a running count of each of
## the days of the week. At the end of the program print out the contents of
## your dictionary (order does not matter).
##

while True:
    fname = input('Enter the file name: ')
    ## fname = 'mbox-short.txt'
    try:
        fhand = open(fname)
        break
    except:
        print('File cannot be opened:', fname)
        ## exit()


mail_day = dict()
for line in fhand:
    if not line.startswith('From '): continue

    words = line.split()
    if len(words) > 2:
        day = words[2]
        ## print(day)
        mail_day[day] = mail_day.get(day,0) + 1
        
print('Mails per day is as follows')
for key in mail_day:
    print(key, mail_day[key])
