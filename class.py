class Employee:
	Department="Account"
	def __init__(self, name, salary, age):
		self.Name=name
		self.Salary=salary
		self.Age=age
def Emp(self):
	print("My name is", self.Name, "and I am", self.Age,"years old.") 
	print("My salary is", str(self.Salary)+",", "My Department is", Employee.Department+".")
	print("=====================================================================")
	#return Emp
Akshay=Employee("Akshay", 20000, 27)
Vijay=Employee("Vijay", 21000, 28)
Karan=Employee("Karan", 30000, 30)
Ajay=Employee("Ajay", 15000, 18)
print("=====================================================================")
print(Akshay.Name, Akshay.Age, Akshay.Salary)
print(Vijay.Name, Vijay.Age, Vijay.Salary)
print("=====================================================================")
Emp(Akshay)
Emp(Vijay)
Emp(Karan)
Emp(Ajay)
