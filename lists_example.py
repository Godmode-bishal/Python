#List concept of Python. Some examples.
#In python, you can't change the contents of the strings by assignment individual index, but you can do it in strings.
fruit='Banana'
#fruit[0]='b'
#print fruit 
#range function in python.
friends=['Bishal','Akhil','Neeraj']
for i in range(3):
    friend=friends[i]
    print 'Happy new Year',friend
    
#Concatenate lists using +
numbers=[1,2,3]
combine=friends+numbers
print combine

#We can declare a list and then initialise it, which can't be done in PHP.We list the allowed attributes of a list by dir.We can add to a list by append.
x=list()
type(x)
#print dir(x)
x.append('Hello')
print x
print ('hello' in x)
print (9 not in x)

#functions
friends.sort()
print friends
print len(numbers)
print max(numbers)
print sum(numbers)
print min(numbers)

#split function.
string="Let us split."
list=string.split()
print list
