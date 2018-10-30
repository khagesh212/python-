# Write a program give an int called N, return the absolute difference between N and 21, except return double the absolute difference if N is over 21 ?

N=int(input("Enter number:"))
if N>21:
    print((N-21)*2)
else:
    print(21-N)
print("Thanks")