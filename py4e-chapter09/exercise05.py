## Exercise 5: This program records the domain name (instead of the address) 
## where the message was sent from instead of who the mail came from (i.e., the 
## whole email address). At the end of the program, print out the contents 
## of your dictionary.
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
for line in fhand:
    if not line.startswith('From '): continue

    words = line.split()
    if len(words) > 2:
        if '@' in words[1]:
            domain = words[1].split('@')[1]
        ## print(domain)
        ## Update mail_count dictionary based on domain
        mail_count[domain] = mail_count.get(domain,0) + 1

## Print mail_count dictionary after completing parsing of file        
print(mail_count)

## Find the domain from where maximum number of mails were sent

max_mail_domain = None
for domain in mail_count:
    if mail_count[domain] > mail_count.get(max_mail_domain, 0):
        max_mail_domain = domain

##print(max_mail_domain, mail_count[max_mail_domain])
print(max_mail_domain, 'sent maximum number of', mail_count[max_mail_domain], 'mails')
