class Employee:
	Department="Account"
	def __init__(self, name, salary, age):
		self.Name=name
		self.Salary=salary
		self.Age=age
Akshay=Employee("Akshay", 20000, 27)
Vijay=Employee("Vijay", 21000, 28)

print(Akshay.Name, Akshay.Age, Akshay.Salary)
"""def statement():
	print("My name is", Employee.Name)
	return statement
statement()"""
