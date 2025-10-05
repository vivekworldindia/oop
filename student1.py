def main():
    student = get_student()
    if student["name"] == "vivek":
        student["house"] = "world"

    print(f"{student['name']} from {student['house']}")
    
    
    
# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return name,house


# tupel ##
 
# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return (name,house)

#### list 
    
# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return [name,house]

#### dict 

def get_student():
 name = input("Name: ")
 house = input("House: ")
 student = {"name":name,"house":house}
 return student

 
if __name__ == "__main__":
    main()