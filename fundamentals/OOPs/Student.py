class Student:
    id : int
    name: str
    age : int

    def __init__(self, id, name,age):
        self.id = id
        self.name = name
        self.age = age


    def display(self):
        print("Student Id : {},name : {},age : {}".format(self.id, self.name, self.age))
