##Dictionaries##
# An example

purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print purse
print purse['candy']
purse['candy']=purse['candy']+2
print purse

#Dictionary literals (constants)
jjj={'chuck':1,'fred':42,'jan':100}
print jjj

#Empty dictionary
iii={}
print iii

#Dictionary traceback when trying to access an element not there and use of IN
ccc=dict()
#print ccc['csev']
print 'csev' in ccc

#counting names
counts=dict()
names=['csev','cwen','rsev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print counts

#General pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word 
#independently
counts=dict()
print 'Enter a line of text:'
line=raw_input() 
words=line.split()
for word in words:
    counts[word]=counts.get(word,0)+1
print 'Counts',counts

#Retrieving list of keys and values
jjj={'chuck':1,'fred':42,'jan':100}
print list(jjj)
print jjj.keys()
print jjj.values()
print jjj.items()