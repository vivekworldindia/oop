# class Wizard:
#   def __init__(self,name):
#     if not name:
#       raise ValueError("Value is missing")
#     self.name = name
    
# class student(Wizard):
#   def __init__(self,name,age):
#     super().__init__(name)
#     self.age = age
    
#   def __str__(self):
#     return f"student name is {self.name} and age {self.age}"
  
# class vivekworld(Wizard):
#   def __init__(self,name,age,founder):
#     super().__init__(founder)
#     self.founder = founder
    
#   def __str__(self):
#     return f"student founder {self.founder}"
  
# x = student("vivek",19)
# y = vivekworld("vivek",19,"vivelworld")
# print(y)


import random 

list = [10,20,34,90]

def sord(name):
  print(f"{name} and {random.choice(list)}")
   
sord("vivek")