#WAP which reads list of numbers until "done" is entered. Once "done" is entered , print out the total,count and average of the numbers.If the user enters anything
# other than a number, print an error message and skip to the next number.
sum=0
av=0.0
count=0
while(1):
    n=raw_input("Enter number:")
    if(n!='done'):
        try:
            num=int(n)
            sum=sum+num
            count=count+1
        except:
            print 'Invalid number'
            continue
    else:
        print 'Sum =',sum
        print 'Count =',count
        if count==0:
            print 'Average =',av
        else:
            print "Average =",sum/float(count)
        exit()