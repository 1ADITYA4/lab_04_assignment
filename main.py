class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(employees, key=lambda x: x.age)
    elif sorting_parameter == 2:
        return sorted(employees, key=lambda x: x.name)
    elif sorting_parameter == 3:
        return sorted(employees, key=lambda x: x.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def print_employees(employees):
    print("Name\tAge\tSalary")
    for employee in employees:
        print(f"{employee.name}\t{employee.age}\t{employee.salary}")

if __name__ == "__main__":
    employees = [
        Employee("Alice", 30, 50000),
        Employee("Bob", 25, 60000),
        Employee("Charlie", 35, 45000),
        Employee("David", 28, 55000),
    ]

    print("Select a sorting parameter:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")

    try:
        sorting_parameter = int(input("Enter your choice: "))
        sorted_employees = sort_employees(employees, sorting_parameter)
        print("\nSorted Employee Data:")
        print_employees(sorted_employees)
    except ValueError as e:
        print(f"Error: {e}")


