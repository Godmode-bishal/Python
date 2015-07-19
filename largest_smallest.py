#find the largest and smallest numbers 
largest=None
smallest=None
for val in [50,40,30,20,10]:
    if smallest is None:
        smallest=val
    elif val<smallest:
        smallest=val
for value in [10,20,40,60,100]:
    if largest is None:
        largest=value
    elif value>largest:
        largest=value
print "The smallest and largest values are",smallest,"and",largest