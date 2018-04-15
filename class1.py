#Bad Way


class Employee:
	pass



emp1 = Employee()
emp2 = Employee()


emp1.first = 'Yuvansh'
emp1.last = 'Bhardwaj'
emp1.email = 'Yuvansh.Bhardwaj@gmail.com'
emp1.pay = 50000

emp2.first = 'Rahul'
emp2.last = 'Sharma'
emp2.email = 'Rahul.Sharma@gmail.com'
emp2.pay = 40000

print(emp1.first)
print(emp1.last)
print(emp2.first)
print(emp2.last)
print(emp1.pay)
print(emp2.pay)






#Good Way


class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@gmail.com"
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp1 = Employee('Yuvansh', 'Bhardwaj', 50000)		
emp2 = Employee('Rahul', 'Sharma', 40000)		


print(emp1.first)
print(emp2.first)
print(emp1.last)
print(emp2.last)
print(emp1.pay)
print(emp2.pay)



print(emp1.fullname())


#or 

print(Employee.fullname(emp1))