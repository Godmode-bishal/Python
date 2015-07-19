#Write a program that prompts for a file name, then opens that file and reads through
#the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and 
#compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
#you are testing below enter mbox-short.txt as the file name.
filename=raw_input("Enter the file name::")
fhand=open(filename)
count=0
sum=0.0
for text in fhand:
    if 'X-DSPAM-Confidence:' in text:
        text=text.strip()
        pos=text.find(':')
        sum=sum+float(text[pos+1:])
        count=count+1
print "Average spam confidence:",(sum/count)