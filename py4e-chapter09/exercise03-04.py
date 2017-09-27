## Exercise 3: Write a program to read through a mail log, build a histogram
## using a dictionary to count how many messages have come from each email address,
## and print the dictionary.
##
## Exercise 4: Add code to the above program to figure out who has the most
## messages in the file.
## After all the data has been read and the dictionary has been created,
## look through the dictionary using a maximum loop (see Section [maximumloop])
## to find who has the most messages and print how many messages the person has.
## 
while True:
    ## fname = input('Enter the file name: ')
    fname = 'mbox-short.txt'
    ## fname = 'mbox.txt'
    try:
        fhand = open(fname)
        break
    except:
        print('File cannot be opened:', fname)

mail_count = dict()

## Parse the file to get mail senders list and count of their mails
for line in fhand:
    if not line.startswith('From '): continue

    words = line.split()
    if len(words) > 2:
        sender = words[1]
        ## print(sender)
        
        ## Update mail_count dictionary based on sender
        mail_count[sender] = mail_count.get(sender,0) + 1

## Print mail_count dictionary after completing parsing of file        
print(mail_count)

## Find who has sent the maximum number of mails by iterating the dictionary and checking values
max_mail_sender = None
for sender in mail_count:
    if mail_count[sender] > mail_count.get(max_mail_sender, 0):
        max_mail_sender = sender

print(max_mail_sender, mail_count[max_mail_sender])
