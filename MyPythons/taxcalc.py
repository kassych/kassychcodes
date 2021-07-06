inc = float(input("Enter Income Amount to calculate PIT ; "))
std = 85528

if inc < std :
    a = (18/100) * inc - 556.2
    tax = round (a, 0)
    if tax < 0:
            print ("PIT payable for this amount is 0.0 Thalers")
    else:
         print ("The PIT payable is :", tax , "Thalers.")
       
elif inc > std :
    b = (32/100) * (inc - std) + 14839.2
    tax1 = round (b, 0)
    print ("The PIT payable is :",tax1, "Thalers")

        

