

#11th mini project
#Employee Record Manager 

employees = {}

while True:
    print("====== EMPLOYEES RECORD ======")
    print("1. Add Employee ")
    print("2. View Employee ")
    print("3. Search Employee ")
    print("4. Update Employee ")
    print("5. Delete Employee ")
    print("6. Exit ")
    print("--------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee_id = input("Enter your id: ")
        employee_name = input("Enter your name: ")
        department = input("Enter your department: ")
        salary = input("Enter your salary: ")
        employees[employee_id]={ "Name":employee_name,
                                "Department":department,
                                "Salary":salary          
        }
    elif choice == "2":
        for employee_id, Details in employees.items():
            print("Employee id:", employee_id )
            print("Employee name:", Details["Name"])
            print("Department:", Details["Department"])
            print("Salary:", Details["Salary"])

    elif choice == "3":
        search = input("Enter Employee id to Search: ")
        if search in employees:
            print("Employee id:", search)
            Details = employees[search]
            print("Employee name:", Details["Name"])
            print("Department:", Details["Department"])
            print("Salary:", Details["Salary"])
        else:
            print("No Employee Found with this id!")

    elif choice == "4":
        old_employee = input("search employee id to update: ")

        if old_employee in employees:
            new_employee_id = input("Enter your new employee id: ")
            employee_name = input("Enter your name: ")
            department = input("Enter your department: ")
            salary = input("Enter your salary: ")
            employees.pop(old_employee)
            employees[new_employee_id]={ "Name":employee_name,
                                    "Department":department,
                                    "Salary":salary          
            }
            print("Employee details updated Successfully")
        else:
            print("No Employee Found with this id!")

    elif choice == "5":
        delete_employee = input("Search Employee id to Delete: ")
        if delete_employee in employees:
            employees.pop(delete_employee)
            print("Deleted Successfully")
        else:
            print("No Employee Found with this id!")

    elif choice == "6":
        print("Exit Successfully")
        break
    else:
        print("Invalid Choice")
