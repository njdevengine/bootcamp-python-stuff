# define three lists

employeeIds = [123, 456, 789, 1001, 1002]
empNames = ["Ashish", "Bruno", "Khoon", "Babla", "Mohammad"]
deptNames = ["Sales", "Marketing", "Administration", "Finance", "IT"]
# zip lists together
empRegister = zip(employeeIds, empNames, deptNames)
# print the consolidated List
print(empRegister)
for aRow in empRegister:
    print(aRow)
