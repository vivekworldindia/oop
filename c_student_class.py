
## use class 

# class Student:
#     ...
      
# def main():
#     student = get_student()
#     print(f"Student name {student.name} from {student.house}")
    
    
    
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

### class method
# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("Value is missing")
#         if house not in ["Gryffindor","Hufflepuff","Ravenclaw","slytherin"]:
#             raise ValueError("Invalide house")
#         self.name = name
#         self.house= house
        

        
      
# def main():
#     student = get_student()
#     print(f"Student name {student.name} from {student.house}")
    
    
    
# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name,house)

# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self,name,house,patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor","Hufflepuff","vivekworld"]:
#             raise ValueError("Invalid house")
#         self.name = name 
#         self.house = house
#         self.patrouns = patronus
        
#     def __str__(self):
#         return f"student name {self.name} and house {self.house}"
    
#     def charm(self):
#         match self.patrouns:
#             case "Stag":
#                 return "🐴"
#             case "Other":
#                 return "java"
#             case _:
#                 return "thanks"
                
    
# def main():
#     student = get_student()
#     print("Expecto Patrouns!")
#     print(student.charm())
#     # print(student)
    
# def get_student():
#     name = input('Name: ')
#     house = input("House: ")
#     patrouns = input("Prtouns:")
#     return Student(name,house,patrouns)
# if __name__ == "__main__":
#     main()



# class Student:
#     def __init__(self,name,house):
#         self.name = name 
#         self.house = house
        
#     def __str__(self):
#         return f"student name {self.name} and house {self.house}"
    
#     @property
#     def house(self):
#         return self._house
#     @house.setter
#     def house(self,house):
#         if house not in ["Gryffindor","Hufflepuff","vivekworld"]:
#             raise ValueError("Invalid house")
#         self._house = house
        
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,name):
#         if not name:
#           raise ValueError('name is missing')
#         self._name = name
    
# def main():
#     student = get_student()
#     student._house = "Vivekworld bro"
#     print(student)
    
# def get_student():
#     name = input('Name: ')
#     house = input("House: ")
#     return Student(name,house)
# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self,name,house):
        self.name = name 
        self.house = house
        
    def __str__(self):
        return f"student name {self.name} and house {self.house}"
    
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","vivekworld"]:
            raise ValueError("Invalid house")
        self._house = house
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
          raise ValueError('name is missing')
        self._name = name

    @classmethod
    def get(cls):
      name = input('Name: ')
      house = input("House: ")
      return cls(name,house)
    
def main():
    student = Student.get()
    print(student)

   
if __name__ == "__main__":
    main()