#Create a class Student with name and age attributes. Create one object and print both.
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = student('rohan',34)
print(s1.name,s1.age)