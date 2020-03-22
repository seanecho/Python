#Author: Sean Gao

name = input("name:")
age = int(input("age:"))     #integer
print(type(age))
job = input("job:")
salary = input("salary:")

info = '''
-------Info of %s-------
Name:%s
Age:%d
Job:%s
Salary:%s
''' %(name,name,age,job,salary)

print(info)

