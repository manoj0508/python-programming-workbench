class Student:
    id : int
    name: str
    age : int
    name = "Kumar"

    def __init__(self, id, name,age):
        self.id = id
        self.name = name
        self.age = age


    def display(self):
        print("Student Id : {},name : {},age : {}".format(self.id, self.name, self.age))



def main():
    p = Student(1,"Manoj","34")
    p.display()
    print(str(True))

if __name__=="__main__":
    main()