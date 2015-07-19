#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use raw_input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.
try:
    hours=int(raw_input("Enter the number of hours:"))
    rate=float(raw_input("Enter the rate per hour:"))
except:
    print "Error, please enter numeric input!!"
    exit()
if hours<=40:
    gross_pay=hours*rate
else:
    extra=hours-40
    gross_pay=(40*rate)+(1.5*extra*rate)
print gross_pay

