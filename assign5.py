# Write a program for ATM withdraw process:

Balance=8900
print("Welcome to ATM")
Pin=input("Enter Pin Number:")
if Pin=="1234":
    Amt=int(input("Enter Amount:"))
    if (Amt%100)==0:
        if Amt<20000:
            if Amt<Balance:
                Balance=Balance-Amt
                print("Available Balance:",Balance)
            else:
                print("Insufficient Balance")
        else:
            print("Maximum Amount is 20000/-")
    else:
        print("Invalid Amount")
else:
    print("Invalid Pin Number Please Check")
print("Thanks for using ATM")