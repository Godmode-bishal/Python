#Tuple.
#Tuples use () while lists use []
#from quiz
x,y=3,4
print y
y=(1,9,2)
print y
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print y
#y[1]=10
#print y
#x=list()
#print dir(x)
#print ""
#print dir(y)
#this can also be done (x,y)=(10,20)
x,y=(10,20)      
print x,y
#quiz
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print days[2]

#Comparision of tuples
print (7,0,2)<(5,1,2)

#Sorting list of tuples.Can't sort tuples and dictionaries, but can sort lists.
d={'c':10,'b':1,'a':22}
t =(d.items())
t.sort()
# I had a doubt that why (d.items()).sort() or t.sort() returns None? The answer is when you do a function on a variable, it will print only if the function returns #something.
print t

#Using sorted() function.
q=sorted(d.items())
print q

#Sort by values instead of keys
l=list()
for key,value in d.items():
    l.append((value,key))
l=sorted(l)
print l

#printing the top 10 common words
fhand=open('romeo.txt')
dictionary=dict()
lst=list()
for lines in fhand:
#making a loop within a loop to read the file word by word.
    for words in lines.split():
        dictionary[words]=dictionary.get(words,0)+1
for key,value in dictionary.items():
    lst.append((value,key))
lst.sort(reverse=True)
#print lst
#printing value . can do "for tuple in list[:10]:" for iterating through tuple as a whole.
for key,value in lst[:10]:
    print value