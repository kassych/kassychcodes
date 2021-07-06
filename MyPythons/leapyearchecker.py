year = int (input("Enter the year you wish to check:  "))
if year < 1582:
    print ("Not Within the Gregorian Calendar period..")
    exit()
a = year % 4
b= year % 100
c = year % 400

if a != 0:
    print ("Common Year")
elif b !=0:
    print ("Leap Year")
elif c !=0:
    print ("Common Year")
else:
    print ("End of Program")



