#Create a program name “employee.py” and implement the 
#functions DA, HRA, PF, and ITAX. Create another program 
#that uses the function of employee module and calculates gross 
#and net salaries of an employee.
import employee

name=input("Enter Name:")
basic=float(input("Enter salary:"))

da=employee.DA(basic)
hra=employee.HRA(basic)
pf=employee.PF(basic)

gross=basic+da+hra
itex=employee.ITEX(gross)
net=gross-(pf+itex)

print("Employee Name:",name)
print("Basic Salary",basic)
print("DA(10%)",da)
print("HRA(15%)",hra)
print("PF(12%)",pf)
print("ITEX(8%)",itex)
print("GROSS Salary",gross)
print("NET Salary",net)