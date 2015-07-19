#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the #'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. #Note that the autograder does not have support for 
#the sorted() function.
fhand=open('mbox-short.txt')
count=dict()
for line in fhand:
    if line.startswith('From '):
        atpos=line.find(':')
        hr=line[atpos-2:atpos]
        count[hr]=count.get(hr,0)+1
lst=list()
for key,value in count.items():
    lst.append((key,value))
lst.sort()
for key,value in lst[:]:
	print key,value