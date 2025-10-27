class Wizard:
    def __init__(self,name):
        if not name :
            raise ValueError("Name is missing")
        self.name = name

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        
        
wizaed = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Ddfens Against the Dark Arts")
print(professor)
