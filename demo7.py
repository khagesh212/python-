E_name=input("Enter Employee Name:")
sal=int(input("Enter salary:"))
deg=input("Enter designation:")
if deg=="m":
    salary=sal+(sal*(20/100))
if deg=="a":
    salary=sal+(sal*(10/100))
if deg=="c":
    salary=sal+(sal*(5/100))
print("Salary of the employee:",salary)