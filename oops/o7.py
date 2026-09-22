class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):
        if self.marks >= 40:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")
s1 = Student("Hema", 75)
s1.display_result()