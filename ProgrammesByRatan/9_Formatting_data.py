eid = int(input("Enter Employee ID :"))
ename = input("Enter Employee name :")
esal = float(input("Enter Employee Salary :"))

print("Employee id : %d ,Employee name : %s ,Employee Salary : %g" %(eid, ename, esal))  # order is important.

print("************ By using Parantehsis(old approach) *************")

print("Employee id : {},Employee name : {},Employee Salary :{}" .format(eid, ename, esal))  # order is not important.