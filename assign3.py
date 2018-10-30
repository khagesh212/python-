# Write a program input positive number and check it is even or odd ?

k=int(input("Enter number:"))
if k>0 and k%2==0:
    print(k,"is even")
elif k<0:
    print(k,"is negative")
else:
    print(k,"is odd")
print("Thanks")