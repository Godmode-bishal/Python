# Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce 
#the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
filename=raw_input('Enter the file name:')
fhand=open(filename)
#for text in fhand:
#    text=text.upper()
#    print text
text=((fhand.read()).rstrip()).upper()
print text
