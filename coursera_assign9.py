#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail #messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent #the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number #of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using #a maximum loop to find the most prolific committers, sorted by hour as shown below. Note that the autograder #does not have support for the #sorted() function.

sender=dict()
largest=None
filename=raw_input('Enter file name:')
fhandle=open(filename)
for line in fhandle:
    if line.startswith('From '):
        words=line.split()
        sender[words[1]]=sender.get(words[1],0)+1
for key in sender:
    if largest is None:
        largest=sender[key]
        email=key
    elif largest<sender[key]:
        largest=sender[key]
        email=key
print email,largest
