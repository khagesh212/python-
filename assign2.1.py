# Write a program input any 2 numbers and check it was positive or negative numbers ?

k=int(input("1st no:"))
l=int(input("2nd no:"))

if k>0 and l>0:
    print(k,l," are positive numbers")
elif k<0 and l>0:
    print(k,"is negative",l,"is positive")
elif k>0 and l<0:
    print(k,"is positive",l,"is negative")
else:
    print(k,l,"are negative numbers")
print("Thanks")