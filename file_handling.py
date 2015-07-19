#printing the handle
fhand=open('hello.txt')
print fhand
#reading file via for loop and printing,and removing blank line by rstrip.
for text in fhand:
    text=text.rstrip()
    print text
#count number of lines
fhand=open('hello.txt')
count=0
for text in fhand:
    count=count+1
print count
#reading the file via read() function
fhand=open('hello.txt')
count=0
while(fhand.read()):
    count=count+1
    print count
#printing out lines starting with hello
fhand=open('hello.txt')
for text in fhand:
    if text.startswith('Hello'):
        print text
#using in to select line and use of 'if not'.
print ""
fhand=open('hello.txt')
for text in fhand:
    text=text.rstrip()
    if not 'hello' in text:
        print text