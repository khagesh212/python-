# Write a program input 3 numbers and find out the big number ?

a=int(input("1st no:"))
b=int(input("2nd no:"))
c=int(input("3rd no:"))

if a>b and a>c:
    print(a,"is big number")
elif b>a and b>c:
    print(b,"is big number")
else:
    print(c,"is big number")
print("Thanks")