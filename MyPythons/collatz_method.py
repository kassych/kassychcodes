c0 = int(input("Enter a Number to check for Collatz hypotheis ;"))
while c0 > 0:
    
    if c0 % 2 == 0:
        c0 = c0/2
        print (c0)      
    else:
        c0 = 3 * c0 +1
        print (c0)
        c0 = int(input("Enter a Number to check for Collatz hypotheis ;"))

else:
        print (c0, "This number is neg or zero. Please enter another number.")
        c0 = int(input("Enter a Number to check for Collatz hypotheis ;"))


    
    
