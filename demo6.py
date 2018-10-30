Name=input("Enter customer name:")
S_type=input("Enter slab type:")
Units=int(input("Enter number of units consumed:"))
if S_type=="i":
    units_consumed=Units*5.25
if S_type=="c":
    units_consumed=Units*4.00
if S_type=="r":
    units_consumed=Units*3.08
print("Total bill:",units_consumed)


