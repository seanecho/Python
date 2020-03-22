#Author: Sean Gao

name = input("name:")
age = int(input("age:"))  # int
print(type(age))
job = input("job:")
salary = input("salary:")

info = '''                       
-------Info of {_name}-------         
Name:{_name}                          
Age:{_age}                          
Job:{_job}                           
Salary:{_salary}                        
'''.format(_name = name,
           _age = age,
           _job = job,
           _salary = salary)
print(info)

info2 = '''                       
-------Info of {0}-------         
Name:{0}                          
Age:{1}                          
Job:{2}                           
Salary:{3}                        
'''.format(name,age,job,salary)
print(info2)

