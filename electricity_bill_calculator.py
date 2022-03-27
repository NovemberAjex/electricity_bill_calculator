units_input = float(input("Please enter your units:  "))
if units_input<=100:
    bill = units_input*25
    print("your bill is ",bill)
elif units_input<=200:
    bill = units_input*35
    print("your bill is ",bill)
elif units_input<=300:
    bill = units_input*45
    print("your bill is ",bill)
elif units_input<=400:
    bill = units_input*55
    print("your bill is ",bill)
elif units_input<=500:
    bill = units_input*65
    print("your bill is ",bill)
else:
    bill = units_input*75
    print("Your bill is ",bill)