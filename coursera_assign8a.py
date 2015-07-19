#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. 
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fhand=open('romeo.txt')
new_list=list()
n_list=list()
for text in fhand:
    list_of_words=text.split()
    for i in range(len(list_of_words)):
        #print list_of_words[i] 
        if (list_of_words[i] not in new_list):
            #print list_of_words[i]
            new_list.append(list_of_words[i])
new_list.sort()
print new_list